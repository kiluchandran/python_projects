from tkinter import *

#Create main window
window=Tk()
window.title("Simple Calculator")
window.geometry("400x400")

#Create a variable to store the current display value
display=StringVar()
display.set("0")

#Create display label
display_label = Label(window, textvariable=display,height=3,width=40,bg="lightblue",anchor="e")
display_label.grid(row=0,column=0,columnspan=11)

#create button
button1=Button(window,text="1",padx=30,pady=20)
button1.grid(row=1,column=0)

button2=Button(window,text="2",padx=30,pady=20)
button2.grid(row=1,column=1)


button3=Button(window,text="3",padx=30,pady=20)
button3.grid(row=1,column=2)

button4=Button(window,text="+",padx=30,pady=20)
button4.grid(row=1,column=3)

button5=Button(window,text="4",padx=30,pady=20)
button5.grid(row=2,column=0)

button6=Button(window,text="5",padx=30,pady=20)
button6.grid(row=2,column=1)

button7=Button(window,text="6",padx=30,pady=20)
button7.grid(row=2,column=2)

button8=Button(window,text="-",padx=30,pady=20)
button8.grid(row=2,column=3)

button9=Button(window,text="7",padx=30,pady=20)
button9.grid(row=3,column=0)

button10=Button(window,text="8",padx=30,pady=20)
button10.grid(row=3,column=1)

button11=Button(window,text="9",padx=30,pady=20)
button11.grid(row=3,column=2)

button12=Button(window,text="*",padx=30,pady=20)
button12.grid(row=3,column=3)

button13=Button(window,text="0",padx=30,pady=20)
button13.grid(row=4,column=0)

button14=Button(window,text="clear",padx=20,pady=20)
button14.grid(row=4,column=1)

button15=Button(window,text=".",padx=30,pady=20)
button15.grid(row=4,column=2)

button16=Button(window,text="/",padx=30,pady=20)
button16.grid(row=4,column=3)







window.mainloop()