from pathlib import Path
import pytesseract

TESSDATA_DIR = Path("tessdata").resolve()

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

print("Tessdata folder:", TESSDATA_DIR)
print("Folder exists:", TESSDATA_DIR.exists())

print("English:", (TESSDATA_DIR / "eng.traineddata").exists())
print("Tamil:", (TESSDATA_DIR / "tam.traineddata").exists())

languages = pytesseract.get_languages(
    config=f'--tessdata-dir "{TESSDATA_DIR}"'
)

print("Available languages:", languages)