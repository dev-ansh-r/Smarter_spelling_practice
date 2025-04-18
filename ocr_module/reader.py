from PIL import Image
import pytesseract

def extract_text(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    words = text.strip().split()
    return words[0] if words else ""
