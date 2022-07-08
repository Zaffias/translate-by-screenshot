import tkinter

window = tkinter.Tk()

def textWindow(text):
    if text == None:
        text = 'Error parsing the text'
    def move_window(event):
        window.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

    window.overrideredirect(True)
    window.geometry('200x100+200+200')

    # Makes a frame for the title bar
    title_bar = tkinter.Frame(window, bg='black', relief='raised', bd=2, borderwidth=0)

    # Add a close window on the widget
    close_button = tkinter.Button(title_bar, text='X', command=window.destroy, borderwidth=0, bg='black', fg='white')

    # Adding canvas to the window

    canvas = tkinter.Canvas(window, bg='black')

    # Makes a label to attach the text
    
    label = tkinter.Label(canvas, bg='black', fg='white', text=text)

    # Makes the window semitransparent
    window.attributes('-alpha',0.7)

    # packing

    title_bar.pack(expand=1, fill=tkinter.X)
    close_button.pack(side=tkinter.RIGHT)
    canvas.pack(expand=1, fill=tkinter.BOTH)
    label.place(x=93, y = 35, anchor='center')

    window.mainloop()