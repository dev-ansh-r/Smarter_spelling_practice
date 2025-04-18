from ocr_module.reader import extract_text
from srs_engine.sm2 import update_schedule, get_due_words, is_word_valid
from ai_helper.gemma_wrapper import get_feedback
from dashboard.app import run_dashboard
import datetime

if __name__ == '__main__':
    print("[INFO] Starting Smarter Spelling Practice")
    # word = extract_text('sample_input.png')
    # print(f"[OCR] Detected: {word}")

    # correct = input(f"Is '{word}' correct? (y/n): ") == 'y'
    
    # if is_word_valid(word):
    #     print(f"[DICTIONARY] '{word}' is a valid English word.")
    # else:
    #     print(f"[DICTIONARY] '{word}' is NOT found in dictionary.")

    # schedule = update_schedule(word, correct)
    # print(f"[SRS] Next due: {schedule['next_due']}")

    # if not correct and not is_word_valid(word):
    #     feedback = get_feedback(word)
    #     print(f"[Gemini AI] Help: {feedback}")

    run_dashboard()
