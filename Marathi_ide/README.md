STEP 1: Install Python

STEP 2: pip install -r requirements.txt

STEP 3: Run CLI
python -m marathi_lang.cli examples/hello.mr --run

STEP 4: Run Online IDE
uvicorn server:app --reload

Open browser:
http://127.0.0.1:8000/static/index.html

STEP 5: Run Streamlit IDE
streamlit run streamlit_app.py