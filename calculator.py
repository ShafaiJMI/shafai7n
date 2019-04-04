from tkinter import*


root =Tk()
root.geometry("399x477")
root.title("Shafai's calculator")

f2 = Frame(root, width =440, height =650, bd =5, relief="raise")
f2.pack(side=TOP)
text_Input =StringVar(value = 'Programmer : Shafai')
operator=""

def btnClick(numbers):
          global operator
          operator = operator + str(numbers)
          text_Input.set(operator)

def btnClearDisplay():
         global operator
         operator ="" 
         text_Input.set("")

def btnEqualsInput():
       global operator
       try:
           sumup = str(eval(operator))
       except ZeroDivisionError:
                 sumup = str("Can't divide by zero")
       except SyntaxError:
                 sumup = str('Invalid calculation!') 
                 
       text_Input.set(sumup)
       operator =""
txtDisplay = Entry(f2, font=('arial',20,'bold'), textvariable=text_Input, bd=40, insertwidth=6, justify='right')
txtDisplay.grid(columnspan=4)
btn0 = Button(f2, padx=29, pady=18, bd=1, bg="white", fg="black", font=('arial', 20, 'bold'), text="0", command=lambda:btnClick(0)).grid(row=1, column=0)
btnClear = Button(f2, padx=29, pady=18, bd=1,bg="white", fg="black", font=('arial', 20, 'bold'), text="C",command=lambda:btnClearDisplay()).grid(row=1, column=1)
btnEquals = Button(f2, padx=29, pady=18, bd=1, bg="black", fg="white", font=('arial', 20, 'bold'), text="=",command=lambda:btnEqualsInput()).grid(row=1, column=2)
Division = Button(f2, padx=29, pady=18, bd=1, bg="white", fg="black", font=('arial', 20, 'bold'), text="/",command=lambda:btnClick("/")).grid(row=1, column=3)
btn7 = Button(f2, padx=29, pady=18, bd=1, bg="white", fg="black", font=('arial', 20, 'bold'), text="7",command=lambda:btnClick(7)).grid(row=2, column=0)
btn8 = Button(f2, padx=29, pady=18, bd=1, bg="white", fg="black", font=('arial', 20, 'bold'), text="8",command=lambda:btnClick(8)).grid(row=2, column=1)
btn9 = Button(f2, padx=29, pady=18, bd=1, bg="white", fg="black", font=('arial', 20, 'bold'), text="9",command=lambda:btnClick(9)).grid(row=2, column=2)
Multiply = Button(f2, padx=29, pady=18, bd=1, bg="white", fg="black", font=('arial', 20, 'bold'), text="*",command=lambda:btnClick("*")).grid(row=2, column=3)
btn4 = Button(f2, padx=29, pady=18, bd=1, bg="white", fg="black", font=('arial', 20, 'bold'), text="4",command=lambda:btnClick(4)).grid(row=3, column=0)
btn5 = Button(f2, padx=29, pady=18, bd=1, bg="white", fg="black", font=('arial', 20, 'bold'), text="5",command=lambda:btnClick(5)).grid(row=3, column=1)
btn6 = Button(f2, padx=29, pady=18, bd=1, bg="white", fg="black", font=('arial', 20, 'bold'), text="6",command=lambda:btnClick(6)).grid(row=3, column=2)
Subtraction = Button(f2, padx=29, pady=18, bd=1, bg="white", fg="black", font=('arial', 20, 'bold'), text="-",command=lambda:btnClick("-")).grid(row=3, column=3)
btn1 = Button(f2, padx=29, pady=18, bd=1, bg="white", fg="black", font=('arial', 20, 'bold'), text="1",command=lambda:btnClick(1)).grid(row=4, column=0)
btn2 = Button(f2, padx=29, pady=18, bd=1, bg="white", fg="black", font=('arial', 20, 'bold'), text="2",command=lambda:btnClick(2)).grid(row=4, column=1)
btn3 = Button(f2, padx=29, pady=18, bd=1, bg="white", fg="black", font=('arial', 20, 'bold'), text="3",command=lambda:btnClick(3)).grid(row=4, column=2)
Addition = Button(f2, padx=29, pady=18, bd=1, bg="white", fg="black", font=('arial', 20, 'bold'), text="+",command=lambda:btnClick("+")).grid(row=4, column=3)



root.mainloop()
