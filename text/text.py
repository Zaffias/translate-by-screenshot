from PIL import Image
import pytesseract
from googletrans import Translator


pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

def getText() -> str:
	image = Image.open('img\hola.png')
	try:
		result = pytesseract.image_to_string(image)
		print(result)
		image.close()
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
