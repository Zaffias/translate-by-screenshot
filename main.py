
from tkinter import *
from window.windowmanager import textWindow
from text.text import getText, translate
from cortaimagenxd.draw import Application
#Clipboard image


def main():
	root = Tk()
	app = Application(root)
	text = getText()
	textWindow(text=text)
	

if __name__ == '__main__':
	main()
