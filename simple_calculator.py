from tkinter import *

def button_clicked(value):
    current_text=display.get()
    if current_text == "0":
        display.set(value)
    else:
        display.set(current_text+value)



# Create main window
window = Tk()
window.title("Simple Calculator")
window.geometry("400x400")

# Create a variable to store the current display value
display = StringVar()
display.set("0")

# Create display label
display_label = Label(window, textvariable=display,height=3,width=40,bg="lightblue",anchor="e")
display_label.grid(row=0,column=0,columnspan=11)


# Create buttons
button_1 = Button(window,text="1",padx=30,pady=20,command=lambda :button_clicked("1"))
button_1.grid(row=1,column=0)

button_2 = Button(window,text="2",padx=30,pady=20,command=lambda :button_clicked("2"))
button_2.grid(row=1,column=1)


button_3 = Button(window,text="3",padx=30,pady=20,command=lambda :button_clicked("3"))
button_3.grid(row=1,column=2)

plus_button = Button(window,text="+",padx=30,pady=20,command=lambda :button_clicked("+"))
plus_button.grid(row=1,column=3)

button_4 = Button(window,text="4",padx=30,pady=20,command=lambda :button_clicked("4"))
button_4.grid(row=2,column=0)

button_5 = Button(window,text="5",padx=30,pady=20,command=lambda :button_clicked("5"))
button_5.grid(row=2,column=1)

button_6 = Button(window,text="6",padx=30,pady=20,command=lambda :button_clicked("6"))

button_6.grid(row=2,column=2)

minus_button = Button(window,text="-",padx=30,pady=20,command=lambda :button_clicked("-"))
minus_button.grid(row=2,column=3)

button_7 = Button(window,text="7",padx=30,pady=20,command=lambda :button_clicked("7"))
button_7.grid(row=3,column=0)

button_8 = Button(window,text="8",padx=30,pady=20,command=lambda :button_clicked("8"))
button_8.grid(row=3,column=1)

button_9 = Button(window,text="9",padx=30,pady=20,command=lambda :button_clicked("9"))
button_9.grid(row=3,column=2)

mul_button = Button(window,text="*",padx=30,pady=20,command=lambda :button_clicked("*"))
mul_button.grid(row=3,column=3)

zero_button = Button(window,text="0",padx=30,pady=20,command=lambda :button_clicked("0"))
zero_button.grid(row=4,column=0)

clear_button = Button(window,text="clear",padx=20,pady=20)
clear_button.grid(row=4,column=1)
clear_button.config(command=lambda :display.set("0"))

dot_button = Button(window,text=".",padx=30,pady=20,command=lambda :button_clicked("."))
dot_button.grid(row=4,column=2)

div_button = Button(window,text="/",padx=30,pady=20,command=lambda :button_clicked("/"))
div_button.grid(row=4,column=3)







window.mainloop()