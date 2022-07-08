
from window.windowmanager import textWindow
from text.text import getText, translate
#Clipboard image


def main():

	text = getText()
	textWindow(text=text)
	

if __name__ == '__main__':
	main()
