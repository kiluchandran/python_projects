from tkinter import *

def button_clicked(value):
    current_text=display.get()
    if current_text == "0":
        display.set(value)
    else:
        display.set(current_text+value)


def clear_display():
    display.set("0")

def calculate_display():
    try:
        expression=display.get()
        result =eval(expression)
        display.set(result)



    except:
        display.set("Error")





# Create main window
window = Tk()
window.title("Simple Calculator")


# Create a variable to store the current display value
display = StringVar()
display.set("0")

# Create display label
display_label = Label(window, textvariable=display,font=("Arial",24),anchor="ne",bg="lightgray",width=15,height=1)
display_label.grid(row=0,column=0,columnspan=4)


# Define button_layout
button_layout = [("1",1,0),("2",1,1),("3",1,2),("+",1,3),
                 ("4",2,0),("5",2,1),("6",2,2),("-",2,3),
                 ("7",3,0),("8",3,1),("9",3,2),("*",3,3),
                 (".",4,0),("0",4,1),("%",4,2),("/",4,3),
                 ("(",5,1),(")",5,2),("=",5,3)]

# Create buttons
for (text,row,column) in button_layout:
    button=Button(window,text=text,padx=30,pady=20,command=lambda t=text:button_clicked(t) if t != "=" else calculate_display())
    button.grid(row=row,column=column)

clear_button = Button(window,text="c",padx=30,pady=20,command= clear_display)
clear_button.grid(row=5,column=0)

window.mainloop()