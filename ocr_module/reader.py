from PIL import Image
import pytesseract

def extract_text(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    words = text.strip().split()
    return words[0] if words else ""

# import easyocr
# from PIL import Image
# import numpy as np

# # Initialize reader once to avoid reloading model every time
# reader = easyocr.Reader(['en'], gpu=False)

# def extract_text(image_path_or_array):
#     """
#     Accepts either a file path or a NumPy image array (from Streamlit camera).
#     Returns the most confident word detected, or an empty string.
#     """
#     if isinstance(image_path_or_array, str):
#         results = reader.readtext(image_path_or_array, detail=1)
#     elif isinstance(image_path_or_array, np.ndarray):
#         image = Image.fromarray(image_path_or_array)
#         results = reader.readtext(np.array(image), detail=1)
#     else:
#         return ""

#     if not results:
#         return ""

#     # Return the word with highest confidence
#     top_result = max(results, key=lambda x: x[2])  # x[2] is confidence
#     return top_result[1].strip()
