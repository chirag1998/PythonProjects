from tkinter import *
def clear_all() : 


	principle_field.delete(0, END) 
	rate_field.delete(0, END) 
	time_field.delete(0, END) 
	compound_field.delete(0, END) 
	principle_field.focus_set() 

 
def Compoundinterest():  
	principle = int(principle_field.get()) 
	
	rate = float(rate_field.get()) 

	time = int(time_field.get()) 

	CI = principle * (pow((1 + rate / 100), time)) 
	compound_field.insert(10, CI) 
    
def Simpleinterest():  
	principle = int(principle_field.get()) 
	
	rate = float(rate_field.get()) 

	time = int(time_field.get()) 

	SI = (principle * rate * time) /100
	simple_field.insert(10, SI)

if __name__ == "__main__" : 

	root = Tk() 
	root.configure(background = 'light green') 
	root.geometry("500x300") 
	root.title("Compound Interest Calculator") 
	label1 = Label(root, text = "Principle Amount(Rs) : ", 
				fg = 'black') 
	label2 = Label(root, text = "Rate(%) : ", 
				fg = 'black') 
	label3 = Label(root, text = "Time(years) : ", 
				fg = 'black') 
	label4 = Label(root, text = "Compound Interest : ", 
				fg = 'black') 
	label5 = Label(root, text = "Simple Interest : ", 
				fg = 'black') 
	label1.grid(row = 1, column = 0, padx = 10, pady = 10) 
	label2.grid(row = 2, column = 0, padx = 10, pady = 10) 
	label3.grid(row = 3, column = 0, padx = 10, pady = 10) 
	label4.grid(row = 5, column = 0, padx = 10, pady = 10) 
	label5.grid(row = 6, column = 0, padx = 10, pady = 10)
	principle_field = Entry(root) 
	rate_field = Entry(root) 
	time_field = Entry(root) 
	compound_field = Entry(root)
	simple_field = Entry(root)
	principle_field.grid(row = 1, column = 1, padx = 10, pady = 10) 
	rate_field.grid(row = 2, column = 1, padx = 10, pady = 10) 
	time_field.grid(row = 3, column = 1, padx = 10, pady = 10) 
	compound_field.grid(row = 5, column = 1, padx = 10, pady = 10) 
	simple_field.grid(row = 6, column = 1, padx = 10, pady = 10) 
	button1 = Button(root, text = "CompoundInterest", bg = "red", 
					fg = "black", command = Compoundinterest) 
	button2 = Button(root, text = "SimpleInterest", bg = "red", 
					fg = "black", command = Simpleinterest)
	button3 = Button(root, text = "Clear", bg = "red", 
					fg = "black", command = clear_all) 
	
	button1.grid(row = 4, column = 1, pady = 10) 
	button2.grid(row = 4, column = 2, pady = 10) 
	button3.grid(row = 7, column = 1, pady = 10) 
	root.mainloop() 
	
	
