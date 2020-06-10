from tkinter import *

def button_Click(numbers):
	global operator
	operator   = operator + str(numbers)
	text_Input.set(operator)

def button_Clear():
	global operator
	operator = ""
	text_Input.set("")

def button_Result():
	global operator
	sum = str(eval(operator))
	text_Input.set(sum)
	operator = ""

cal = Tk()
cal.title("Calc")
operator=""
text_Input = StringVar()


txtDisplay = Entry(cal,font=('arial',20,'bold'), textvariable = text_Input, bd = 30, insertwidth = 4,
	bg = "white",justify = 'right').grid(columnspan=4)

#Row 1
btn7 = Button(cal,padx = 20, pady = 16, bd = 8, fg = 'black', font =("arial",20, 'bold'),text = "7",command = lambda:button_Click(7)).grid(row = 1, column = 0)
btn8 = Button(cal,padx = 20, pady = 16, bd = 8, fg = 'black', font =("arial",20, 'bold'),text = "8",command = lambda:button_Click(8)).grid(row = 1, column = 1)
btn9 = Button(cal,padx = 20, pady = 16, bd = 8, fg = 'black', font =("arial",20, 'bold'),text = "9",command = lambda:button_Click(9)).grid(row = 1, column = 2)
add  = Button(cal,padx = 20, pady = 16, bd = 8, fg = 'black', font =("arial",20, 'bold'),text = "+",command = lambda:button_Click("+")).grid(row = 1, column = 3)
#Row 2
btn4 = Button(cal,padx = 20, pady = 16, bd = 8, fg = 'black', font =("arial",20, 'bold'),text = "4",command = lambda:button_Click(4)).grid(row = 2, column = 0)
btn5 = Button(cal,padx = 20, pady = 16, bd = 8, fg = 'black', font =("arial",20, 'bold'),text = "5",command = lambda:button_Click(5)).grid(row = 2, column = 1)
btn6 = Button(cal,padx = 20, pady = 16, bd = 8, fg = 'black', font =("arial",20, 'bold'),text = "6",command = lambda:button_Click(6)).grid(row = 2, column = 2)
nakis= Button(cal,padx = 20, pady = 16, bd = 8, fg = 'black', font =("arial",20, 'bold'),text = "-",command = lambda:button_Click("-")).grid(row = 2, column = 3)
#Row 3
btn1 = Button(cal,padx = 20, pady = 16, bd = 8, fg = 'black', font =("arial",20, 'bold'),text = "1",command = lambda:button_Click(1)).grid(row = 3, column = 0)
btn2 = Button(cal,padx = 20, pady = 16, bd = 8, fg = 'black', font =("arial",20, 'bold'),text = "2",command = lambda:button_Click(2)).grid(row = 3, column = 1)
btn3 = Button(cal,padx = 20, pady = 16, bd = 8, fg = 'black', font =("arial",20, 'bold'),text = "3",command = lambda:button_Click(3)).grid(row = 3, column = 2)
mul  = Button(cal,padx = 20, pady = 16, bd = 8, fg = 'black', font =("arial",20, 'bold'),text = "*",command = lambda:button_Click("*")).grid(row = 3, column = 3)

btn0     = Button(cal,padx = 20, pady=  16, bd = 8, fg = 'black', font =("arial",20,'bold'),text = "0",command = lambda:button_Click(0)).grid(row = 4, column = 0)
btnClear = Button(cal,padx = 20, pady = 16,bd = 8, fg = 'black', font =("arial",20, 'bold'),text = "C",command = button_Clear).grid(row = 4, column = 1)
btnEq    = Button(cal,padx = 20, pady = 16,bd = 8, fg = 'black', font =("arial",20, 'bold'),text = "=",command = button_Result ).grid(row = 4, column = 2)
Division = Button(cal,padx = 20, pady = 16,bd = 8, fg = 'black', font =("arial",20, 'bold'),text = "/",command =lambda:button_Click("/")).grid(row = 4, column = 3)

cal.mainloop()
