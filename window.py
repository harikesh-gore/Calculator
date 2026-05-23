from tkinter import *

window = Tk()
window.configure(bg="#1e1e1e")
window.title ="calculator"
window.geometry=(300*500)

display = Entry(window, width=20, borderwidth=5, justif="right", font=("Arial", 28),bg="#2d2d2d",fg="white")
result_label = Label(window, text="",font=("Arial", 18), bg="#1e1e1e",fg="white",anchor="e")
display.grid(row=0,column=0,columnspan=4,padx=7, pady=20)
result_label.grid(row=1,column=0, columnspan=4,sticky="we",padx=5,pady=5)
operator_clicked= False


def click(number):
    current = display.get()
    display.delete(0, END)
    display.insert(0, str(current) + str(number))

def backspace():
    current = display.get()
    display.delete(0, END)
    display.insert(0, current[:-1])   

def clear():
    display.delete(0,END)    

def add():
     display.insert(END,"+")    

def substract():
     display.insert(END,"-")

def multiply():
    display.insert(END,"*")  

def divide():
    display.insert(END,"/")   

def decimal():
  current = display.get()

  if "." not in current:
    display.insert(END, ".")


def total():

    try:
        expression = display.get()
        result = eval(expression)
        result_label.config(text=result)

    except:
     result_label.config(text="Error")

def Keypress (event):
   key=event.keysym

   if key in ["0","1","2","3","4","5","6","7","8","9","."]:
      click(key)

   elif key=="plus":
      add()
   elif key =="minus":
      substract()
   elif key=="asterisk":
      multiply()
   elif key == "slash":
      divide()
   elif key== "BackSpace":
      backspace()
   elif key=="Return":
      total()
   elif key=="Delete":
      clear()   
   elif key =="period":
      decimal()

window.bind("<Key>",Keypress)               

button1 = Button(
    window,
    text="1",
    width=5,
    height=2,
    font= ("arial",16, "bold"),
    bg="#2d2d2d",
    fg="white",
    borderwidth=0,
    relief="raised",
    activebackground="#333333",
    activeforeground="white",
    command= lambda: click(1)
)

button2 = Button(
    window,
    text="2",
    width=5,
    height=2,
    font= ("arial",16,"bold"),
    bg="#2d2d2d",
    fg="white",
    borderwidth=0,
    relief="raised",
    activebackground="#333333",
    activeforeground="white",
    command= lambda: click(2)
)

button3 = Button(
    window,
    text="3",
    width=5,
    height=2,
    font= ("arial",16, "bold"),
    bg="#2d2d2d",
    fg="white",
    borderwidth=0,
    relie="raised",
    activebackground="#333333",
    activeforeground="white",
    command= lambda: click(3)
)

button4 = Button(
    window,
    text="4",
    width=5,
    height=2,
    font= ("arial",16,"bold"),
    bg="#2d2d2d",
    fg="white",
    borderwidth=0,
    relief="raised",
    activebackground="#333333",
    activeforeground="white",
    command= lambda:click(4)
)

button5 = Button(
    window,
    text="5",
    width=5,
    height=2,
    font= ("arial",16, "bold"),
    bg="#2d2d2d",
    fg="white",
    borderwidth=0,
    relief="raised",
    activebackground="#333333",
    activeforeground="white",
    command= lambda:click(5)
) 

button6 = Button(
    window,
    text="6",
    width=5,
    height=2,
    font= ("arial",16, "bold"),
    bg="#2d2d2d",
    fg="white",
    borderwidth=0,
    relief="raised",
    activebackground="#333333",
    activeforeground="white",
    command= lambda:click(6)
)

button7 = Button(
    window,
    text="7",
    width=5,
    height=2,
    font= ("arial",16, "bold"),
    bg="#2d2d2d",
    fg="white",
    borderwidth=0,
    relief="raised",
    activebackground="#333333",
    activeforeground="white",
    command= lambda:click(7)
)

button8 = Button(
    window,
    text="8",
    width=5,
    height=2,
    font= ("arial",16, "bold"),
    bg="#2d2d2d",
    fg="white",
    borderwidth=0,
    relief="raised",
    activebackground="#333333",
    activeforeground="white",
    command= lambda:click(8)
) 

button9 = Button(
    window,
    text="9",
    width=5,
    height=2,
    font= ("arial",16, "bold"),
    bg="#2d2d2d",
    fg="white",
    borderwidth=0,
    relief="raised",
    activebackground="#333333",
    activeforeground="white",
    command= lambda:click(9)
)

button10 = Button(
    window,
    text="0",
    width=5,
    height=2,
    font= ("arial",16, "bold"),
    bg="#2d2d2d",
    fg="white",
    borderwidth=0,
    relief="raised",
    activebackground="#333333",
    activeforeground="white",
    command= lambda:click(0)
)

button_dot = Button(
    window,
    text=".",
    width=5,
    height=2,
    font= ("arial",16,"bold"),
    bg="#2d2d2d",
    fg="white",
    borderwidth=0,
    relief="raised",
    activebackground="#333333",
    activeforeground="white",
    command=decimal
)

button_backspace = Button(
    window,
    text="⌫",
    width=5,
    height=2,
    font= ("arial",16,"bold"),
    bg="#2d2d2d",
    fg="green",
    borderwidth=0,
    relief="raised",
    activebackground="#333333",
    activeforeground="green",
    command=backspace
)

button_clear= Button (
    window,
    text="C",
    width=5,
    height=2,
    font= ("arial",16,"bold"),
    bg="#2d2d2d",
    fg="red",
    borderwidth=0,
    relief="raised",
    activebackground="#333333",
    activeforeground="red",
    command=clear 
)

button_brackets= Button (
    window,
    text="()",
    width=5,
    height=2,
    font= ("arial",16,"bold"),
    bg="#2d2d2d",
    fg="green",
    borderwidth=0,
    relief="raised",
    activebackground="#333333",
    activeforeground="green"
)

button_total = Button(
    window,
    text="=",
    width=5,
    height=2,
    font= ("arial",16, "bold"),
    bg="green",
    fg="white",
    borderwidth=0,
    relief="raised",
    activebackground="#333333",
    activeforeground="green",
    command=total
)

button_add = Button(
    window,
    text="+",
    width=5,
    height=2,
    font= ("arial",16,"bold"),
    bg="#2d2d2d",
    fg="green",
    borderwidth=0,
    relief="raised",
    activebackground="#333333",
    activeforeground="green",
    command=add
)

button_substract = Button(
    window,
    text="-",
    width=5,
    height=2,
    font= ("arial",16, "bold"),
    bg="#2d2d2d",
    fg="green",
    borderwidth=0,
    relief="raised",
    activebackground="#333333",
    activeforeground="green",
    command=substract
)

button_multiply = Button(
    window,
    text="*",
    width=5,
    height=2,
    font= ("arial",16,"bold"),
    bg="#2d2d2d",
    fg="green",
    borderwidth=0,
    relief="raised",
    activebackground="#333333",
    activeforeground="green",
    command=multiply
)
button_divide = Button(
    window,
    text="/",
    width=5,
    height=2,
    font= ("arial",16, "bold"),
    bg="#2d2d2d",
    fg="green",
    borderwidth=0,
    relief="raised",
    activebackground="#333333",
    activeforeground="green",
    command=divide
)

button1.grid(row=2,column=0, padx=5, pady=5)
button2.grid(row=2,column=1, padx=5, pady=5)
button3.grid(row=2,column=2, padx=5, pady=5)
button4.grid(row=3,column=0, padx=5, pady=5)
button5.grid(row=3,column=1, padx=5, pady=5)
button6.grid(row=3,column=2, padx=5, pady=5)
button7.grid(row=4,column=0, padx=5, pady=5)
button8.grid(row=4,column=1, padx=5, pady=5)
button9.grid(row=4,column=2, padx=5, pady=5)
button10.grid(row=5,column=1,padx=5, pady=5)
button_dot.grid(row=5,column=2,padx=5, pady=5)
button_backspace.grid(row=5, column=0,padx=5,pady=5)
button_clear.grid(row=1,column=0,padx=5,pady=5)
button_brackets.grid(row=1,column=1,padx=5,pady=5)
button_total.grid(row=1,column=2,padx=5,pady=5)
button_add.grid(row=5,column=3,padx=5,pady=5)
button_substract.grid(row=4,column=3,padx=5,pady=5)
button_multiply.grid(row=3,column=3,padx=5,pady=5)
button_divide.grid(row=2,column=3,padx=5,pady=5)


window.mainloop()

