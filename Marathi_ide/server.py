from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from marathi_lang.transpiler import transpile_source

import io
import sys

app = FastAPI()

# serve static IDE files
app.mount("/static", StaticFiles(directory="static"), name="static")


# open IDE on root URL
@app.get("/")
def home():
    return FileResponse("static/index.html")


# run Marathi code
@app.post("/run")
async def run_code(data: dict):

    code = data.get("code", "")

    old_stdout = sys.stdout   # save stdout first

    try:
        py_code = transpile_source(code)

        sys.stdout = mystdout = io.StringIO()

        exec(py_code, {})   # fresh scope every run

        output = mystdout.getvalue()

        return {
            "python": py_code,
            "output": output
        }

    except Exception as e:
        return {"error": str(e)}

    finally:
        sys.stdout = old_stdout   # VERY IMPORTANT restore