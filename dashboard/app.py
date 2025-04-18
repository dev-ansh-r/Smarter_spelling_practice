import streamlit as st
import sqlite3
import pandas as pd
from ocr_module.reader import extract_text
from srs_engine.sm2 import update_schedule, is_word_valid
from ai_helper.gemma_wrapper import get_feedback
import tempfile
from PIL import Image

def run_dashboard():
    st.set_page_config(page_title="Spelling Practice App", layout="wide")

    page = st.sidebar.radio("Navigation", ["📊 Progress Tracker", "🧠 Practice Spelling"])

    if page == "📊 Progress Tracker":
        run_progress_dashboard()
    elif page == "🧠 Practice Spelling":
        run_spelling_practice()


def run_progress_dashboard():
    st.title("📊 Spelling Progress Tracker")

    conn = sqlite3.connect('data/user_db.sqlite')
    df = pd.read_sql_query("SELECT * FROM word_logs", conn)

    if df.empty:
        st.write("No spelling data yet.")
        return

    df['next_due'] = pd.to_datetime(df['next_due'])
    st.dataframe(df)

    st.bar_chart(df.set_index('word')[['interval']])
    st.line_chart(df.set_index('word')[['easiness']])
    conn.close()


def run_spelling_practice():
    st.title("🧠 Practice Spelling from Image")

    uploaded_file = st.file_uploader("Upload a spelling image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Save to a temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
            image.save(tmp.name)
            word = extract_text(tmp.name)

        st.write(f"🔍 OCR Detected Word: **{word}**")

        if is_word_valid(word):
            st.success(f"✅ '{word}' is a valid English word!")
        else:
            st.warning(f"⚠️ '{word}' is not in dictionary.")

        correct = st.radio("Did the student spell it correctly?", ["Yes", "No"])
        if st.button("📚 Submit and Get Feedback"):
            schedule = update_schedule(word, correct == "Yes")
            st.info(f"📅 Next Practice Due: {schedule['next_due']}")

            if correct == "No" and not is_word_valid(word):
                feedback = get_feedback(word)
                st.error(f"💡 AI Suggestion: {feedback}")

