from tkinter import *                 # importing the tkinter module
root = Tk()         
root.config(background='ivory2')
root.geometry("440x380")     # setting the width and height of the gui
root.resizable(0,0)
root.wm_iconbitmap("Pelfusion-Long-Shadow-Ios7-Calculator.ico")  #importing an icon 
root.title("Calculator by CSE -Aman kr shah" ) 

expression = ""       #globally declaring an empty variable
def entry(num):         # defining function to update expression in the text entry box
    global expression
    expression+=num        # concatenation of string
    value.set(expression)

def clear():              # function to clear last entered expression
    global expression
    expression= expression[0:len(expression)-1]
    value.set(expression)

def allclear():          # function to clear everything and reset 
    global expression
    expression = ""
    value.set("")

def calculate():        # eval function evaluate the expression , and str function convert the result into string
    try:
        global expression
        answer = eval(expression)
        value.set(answer)
    except:
        value.set("Enter correct expression")
        expression = ""

value = StringVar(value="0")         # declaring variable to take value of expression 

Entry(root,justify=RIGHT,textvariable=value, font="bold" , bg="ghost white").grid(row=0,  
    column=0, columnspan=6, ipadx=100 , ipady=10)   #bar for entering value

Button(root, text="7",font="bold",bg="light blue", command=lambda:entry("7"), borderwidth=22).grid(row=1,column=0)
Button(root, text="8",font="bold",bg="light blue", command=lambda:entry("8"), borderwidth=22).grid(row=1,column=1)
Button(root, text="9",font="bold",bg="light blue", command=lambda:entry("9"), borderwidth=22).grid(row=1,column=2)
Button(root, text="/",font="bold",bg="linen" ,     command=lambda:entry("/"), borderwidth=22).grid(row=1,column=3)

Button(root, text="4",font="bold" ,bg="light blue", command=lambda:entry("4"),  borderwidth=22).grid(row=2,column=0)
Button(root, text="5",font="bold" ,bg="light blue", command=lambda:entry("5"),  borderwidth=22).grid(row=2,column=1)
Button(root, text="6",font="bold" ,bg="light blue", command=lambda:entry("6"),  borderwidth=22).grid(row=2,column=2)
Button(root, text="-",font="bold" ,bg="linen",      command=lambda:entry("-"),  borderwidth=22).grid(row=2,column=3)

Button(root, text="1",font="bold" ,bg="light blue", command=lambda:entry("1"),  borderwidth=22).grid(row=3,column=0)
Button(root, text="2",font="bold" ,bg="light blue", command=lambda:entry("2"),  borderwidth=22).grid(row=3,column=1)
Button(root, text="3",font="bold" ,bg="light blue", command=lambda:entry("3"),  borderwidth=22).grid(row=3,column=2)
Button(root, text="*",font="bold" ,bg="linen",      command=lambda:entry("*"),  borderwidth=22).grid(row=3,column=3)

Button(root, text="%",font="bold" ,command=lambda: 
entry("%"),bg="linen" ,borderwidth=22).grid(row=4, column=0)
Button(root, text="+",font="bold" ,command=lambda: 
entry("+"),bg="linen" ,borderwidth=22).grid(row=4, column=3)
Button(root, text=".",font="bold" ,command=lambda: 
entry("."),bg="linen" ,borderwidth=22).grid(row=4, column=2)  

Button(root, text="0",font="bold" , bg="light blue", command=lambda: 
entry("0"),  borderwidth=22).grid(row=4, column=1)
# "clear" button to call the clear function which will clear digit from last
Button(root, text="C", font="bold",bg="orange",command=clear, height=2,
    width=8).grid(row=1, column=5)
# "allclear" button to call the allclear function which will allclear the entry widget so that the user can start clculating again
Button(root, text="AC", font="bold",bg="orange",command=allclear, height=2, 
    width=8).grid(row=2, column=5)
# "=" button to call the calculate button which will return and entry the calculated value 
Button(root, text="=",font="bold",bg="light green", command=calculate, height=6,
    width=8).grid(row=3, column=5 , rowspan=2)
root.mainloop()  # .mainloop() is used when the code is ready to run









#EXPLAINATIONS--
#What is Lambda Function in Python?
#Lambda Function, also referred to as ‘Anonymous function’ is same as a regular python function 
# but can be defined without a name. 
# While normal functions are defined using the def keyword, anonymous functions are defined 
# using the lambda keyword. However,they are restricted to single line of expression.
#taking lamda so we dont have to define each expression in function bar...
#lambda functions reduce the number of lines of code when compared to normal python function defined using def keyword.

