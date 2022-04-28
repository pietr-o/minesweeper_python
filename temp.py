from tkinter import *

if __name__ == "__main__":
    root = Tk()


    def on_button(event):
        print(event.state)

    button = Button(root, text='test')
    button.bind("<Double-1>", on_button)
    button.pack()

    root.mainloop()
