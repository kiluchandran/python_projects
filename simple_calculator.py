from tkinter import *

window=Tk()
window.title("Simple Calculator")
window.geometry("500x500")
display=StringVar()
display.set("0")

display_label = Label(window, textvariable=display, font=("Arial", 24), anchor="e", background="white",width=28,height=1)
display_label.grid()





window.mainloop()