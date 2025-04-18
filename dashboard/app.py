import streamlit as st
import sqlite3
import pandas as pd
import tempfile
from PIL import Image
import numpy as np

from ocr_module.reader import extract_text
from srs_engine.sm2 import update_schedule, is_word_valid
from ai_helper.gemma_wrapper import get_feedback

def run_dashboard():
    st.set_page_config(page_title="Smarter Spelling Practice", layout="wide")
    st.title("📸 Live Spelling Practice with OCR + Gemini AI")

    st.sidebar.header("📥 Input Mode")
    tab = st.sidebar.radio("Choose Mode:", ["Live Camera OCR", "Progress Dashboard"])

    if tab == "Live Camera OCR":
        st.subheader("📷 Capture Image")
        image = st.camera_input("Take a photo for OCR")

        if image:
            img = Image.open(image).convert("RGB")
            img_np = np.array(img)
            with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
                temp_path = temp_file.name
                img.save(temp_path)

            word = extract_text(temp_path)
            st.write(f"🧠 **Detected Word:** `{word}`")

            is_valid = is_word_valid(word)
            st.write(f"📚 Valid Word: {'✅ Yes' if is_valid else '❌ No'}")

            correct = st.radio(f"Did the student spell `{word}` correctly?", ['Yes', 'No']) == 'Yes'

            schedule = update_schedule(word, correct)
            st.write(f"🕒 Next due: `{schedule['next_due']}`")

            if not correct and not is_valid:
                st.info("Getting feedback from Gemini AI...")
                feedback = get_feedback(word)
                st.success(f"💡 Suggestion: {feedback}")

    elif tab == "Progress Dashboard":
        st.subheader("📊 Spaced Repetition Progress")

        conn = sqlite3.connect('data/user_db.sqlite')
        df = pd.read_sql_query("SELECT * FROM word_logs", conn)

        if df.empty:
            st.warning("No spelling data found.")
        else:
            df['next_due'] = pd.to_datetime(df['next_due'])
            st.dataframe(df)
            st.bar_chart(df.set_index('word')[['interval']])
            st.line_chart(df.set_index('word')[['easiness']])
        conn.close()
