from PIL import ImageGrab
import pytesseract
from googletrans import Translator


pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

def getText() -> str:
	image = ImageGrab.grabclipboard()
	try:
		result = pytesseract.image_to_string(image)
		print(result)
		return result
	except:
		print("Image is not valid")
		return None

def translate(text: str) -> str:
	t = Translator()
	try:
		t_translate = t.translate(text, dest = 'es')
		translated = t_translate.text
		return translated
	except:
		return None
