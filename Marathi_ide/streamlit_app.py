import streamlit as st

from marathi_lang.lexer import tokenize
from marathi_lang.parser import Parser
from marathi_lang.runtime import Runtime
from marathi_lang.debugger import Debugger
from marathi_lang.ast_visual import draw_ast
from marathi_lang.syntax_checker import check_syntax


st.set_page_config(
    page_title="Marathi IDE",
    layout="wide"
)


st.title("🇮🇳 Marathi Programming Language IDE")


# ---------------- SESSION ----------------

if "code" not in st.session_state:
    st.session_state.code = ""


# ---------------- EDITOR ----------------

code = st.text_area(
    "✍ Write Marathi Code",
    value=st.session_state.code,
    height=350
)

st.session_state.code = code


col1, col2, col3, col4 = st.columns(4)


# ================= RUN =================

if col1.button("▶ Run"):

    try:

        check_syntax(code)

        tokens = tokenize(code)

        ast = Parser(tokens).parse()


        runtime = Runtime()

        runtime.execute(ast)


        st.success("Execution Completed")


        st.subheader("📤 Output")

        if runtime.output:

            st.code(
                "\n".join(runtime.output)
            )

        else:

            st.info("No output")


        st.subheader("🧠 Memory")

        st.json(runtime.env)



    except Exception as e:

        st.error(str(e))



# ================= DEBUG =================

if col2.button("🐞 Debug"):

    try:

        check_syntax(code)

        tokens = tokenize(code)

        ast = Parser(tokens).parse()


        runtime = Runtime()

        debugger = Debugger()


        debugger.execute(
            runtime,
            ast
        )


        st.subheader("📜 Execution Trace")


        for item in debugger.trace:

            st.write(item)


        st.subheader("👁 Variable Watch")

        st.json(
            debugger.clean_memory()
        )


    except Exception as e:

        st.error(str(e))



# ================= AST =================

if col3.button("🌳 AST Tree"):

    try:

        check_syntax(code)

        tokens = tokenize(code)

        ast = Parser(tokens).parse()


        graph = draw_ast(ast)


        st.graphviz_chart(graph)



    except Exception as e:

        st.error(str(e))



# ================= CLEAR =================

if col4.button("🗑 Clear"):

    st.session_state.code = ""

    st.rerun()



# ================= FILE SYSTEM =================

st.subheader("📂 File System")


uploaded = st.file_uploader(
    "Open Marathi File",
    type=["mr"]
)


if uploaded:

    loaded_code = uploaded.read().decode()

    st.session_state.code = loaded_code

    st.success("File Loaded")



st.download_button(

    label="💾 Save .mr File",

    data=code,

    file_name="program.mr",

    mime="text/plain"

)



# ================= COMPILER VIEW =================

with st.expander("⚙ Compiler Details"):


    st.write("Tokens")

    st.json(
        tokenize(code)
    )


    st.write("AST Data")

    st.json(
        Parser(tokenize(code)).parse()
    )