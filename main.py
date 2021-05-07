import os 
import base64
import os.path
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import useful_stuff as US
import numpy as np

username=""

def main():
	global loginGui
	loginGui = Tk()
	loginGui.geometry("350x125")
	loginGui.title("Fitness Program Demo")
	global check
	check=0
	myLabel_1 = Label(loginGui, text="Login ")
	loginInfo_1 = Label(loginGui, text="Username: ")
	global loginInput_1
	loginInput_1= Entry(loginGui, width=20)
	loginInfo_2 = Label(loginGui, text="Password: ")
	global loginInput_2
	loginInput_2= Entry(loginGui,show="*", width=20)
	loginButton = Button(loginGui, text="Login", command=authLogin)
	signUpButton= Button(loginGui, text="Sign Up", command=signUp)

	myLabel_1.grid(row=0,column=0)
	loginInfo_1.grid(row=1,column=0)
	loginInput_1.grid(row=1,column=1)
	loginInfo_2.grid(row=2,column=0)
	loginInput_2.grid(row=2,column=1)
	loginButton.grid(row=3,column=0)
	signUpButton.grid(row=4,column=0)

	loginGui.mainloop()


def authLogin():
	global username
	username=loginInput_1.get()
	filename = loginInput_1.get()+".txt"
	if os.path.isfile(filename):
		file=open(filename)
		content = file.read().splitlines()
		filepass= bytes(content[1], 'utf-8')
		password=base64.b64encode(bytes(loginInput_2.get(), 'utf-8'))
		if password==filepass:
			loginGui.destroy()
			print("login successful")
			global check
			check=1
		else:
			messagebox.showerror('error', 'Login unsuccessful.')
	else:
		messagebox.showerror('error', 'Username does not exist')


def signUp():
	loginGui.destroy()
	global sexvar
	global clicked
	global signUpGui
	signUpGui = Tk()
	signUpGui.geometry("750x425")
	signUpGui.title("Fitness Program Demo")

	agenums = np.arange(18,71,1).tolist()
	feetnums = np.arange(1,9,1).tolist()
	inchesnums = np.arange(0,12,1).tolist()
	clicked = StringVar()
	clicked.set("----")
	sexvar=IntVar()
	global usernameInput,passwordInput,nameInput,ageCombo,feetCombo,inchesCombo,weightInput

	signUpLabel = Label(signUpGui, text="Sign-Up ")
	usernameLabel = Label(signUpGui, text="Username: ") 
	usernameInput= Entry(signUpGui, width=20)#something
	passwordLabel = Label(signUpGui, text="Password: ") 
	passwordInput= Entry(signUpGui, width=20) #something
	nameLabel = Label(signUpGui, text="Name: ") 
	nameInput= Entry(signUpGui, width=20)#something
	ageLabel= Label(signUpGui, text="Age: ") 
	ageCombo = ttk.Combobox(signUpGui, state="readonly", values = agenums)#something
	MaleBttn = Radiobutton(signUpGui, text = "Male", variable = sexvar,value = 1)#something
	FemaleBttn = Radiobutton(signUpGui, text = "Female", variable = sexvar,value = 2)#something
	heightLabel = Label(signUpGui, text="Height: ")
	feetLabel = Label(signUpGui, text="feet ")
	feetCombo = ttk.Combobox(signUpGui, state="readonly", values = feetnums) #something
	inchesLabel = Label(signUpGui, text="inches ")
	inchesCombo = ttk.Combobox(signUpGui, state="readonly", values = inchesnums) #something
	weightLabel = Label(signUpGui, text="Weight: ")
	weightInput= Entry(signUpGui, width=20) #something
	lbsLabel = Label(signUpGui, text="lbs ")
	AskQuestionLabel = Label(signUpGui, text="How active do you consider yourself to be?: ")
	QuestionAnsMenu= OptionMenu(signUpGui,clicked, "Sedentary","Lightly Active","Moderatly Active", "Very Active") #something
	SubmitButton = Button(signUpGui, text="Sign-up", command=checkSignUp)#something

	signUpLabel.grid(row=0,column=0)
	usernameLabel.grid(row=1,column=0)
	usernameInput.grid(row=1,column=1)
	passwordLabel.grid(row=2,column=0)
	passwordInput.grid(row=2,column=1)
	nameLabel.grid(row=3,column=0)
	nameInput.grid(row=3,column=1)
	ageLabel.grid(row=4,column=0)
	ageCombo.grid(row=4,column=1)
	MaleBttn.grid(row=5,column=0)
	FemaleBttn.grid(row=5,column=1)
	heightLabel.grid(row=6,column=0)
	feetLabel.grid(row=6,column=2)
	feetCombo.grid(row=6,column=1)
	inchesLabel.grid(row=6,column=4)
	inchesCombo.grid(row=6,column=3)
	weightLabel.grid(row=7,column=0)
	weightInput.grid(row=7,column=1)
	lbsLabel.grid(row=7,column=2)
	AskQuestionLabel.grid(row=8,column=0)
	QuestionAnsMenu.grid(row=8,column=1)
	SubmitButton.grid(row=10,column=0)

	signUpGui.mainloop()

	

def checkSignUp():
	choice=sexvar.get()
	global username
	username=usernameInput.get()
	try:
		weight=int(weightInput.get())
		if (weightInput.index("end") == 0) or (weight<=80):
			messagebox.showerror('error', 'Please correct the weight field. You have to be more than 80 pounds.')
	except Exception:
		messagebox.showerror('error', 'Weight has to be a number.')
	if len(usernameInput.get()) == 0:
		messagebox.showerror('error', 'Please put in a username.')
	elif (os.path.isfile("./"+username+".txt")):
		messagebox.showerror('error', 'Username alreasy exists.')
	elif len(passwordInput.get()) == 0:
		messagebox.showerror('error', 'Please put in a password.')
	elif len(nameInput.get()) == 0:
		messagebox.showerror('error', 'Please put in a name*.')
	elif ageCombo.index("end") == 0:
		messagebox.showerror('error', 'Please enter an age.')
	elif (choice != 1) and (choice != 2):
		messagebox.showerror('error', 'Please enter your sex.')
	elif (feetCombo.index("end") == 0) or (inchesCombo.index("end") == 0):
		messagebox.showerror('error', 'Please enter your height.')
	elif clicked.get() == "----":
		messagebox.showerror('error', 'Please enter your activity level.')
	else:
		password=base64.b64encode(bytes(passwordInput.get(), 'utf-8'))
		name=nameInput.get()
		age=int(ageCombo.get())
		if choice==1:
			choice="Male"
		else:
			choice="Female"
		feet=int(feetCombo.get())
		inches=int(inchesCombo.get())
		height=(feet*12) + inches
		click=clicked.get()
		activity=switch_activity(click)
		arrayInfo=[username,password,name,age,choice,height,weight,1,activity,US.calculate_BMI_signup(weight,height),US.calculate_BMR_signup(height,weight,choice,age,activity),0]
		US.createAccount(arrayInfo)
		signUpGui.destroy()
		print("account created")
		global check
		check=1


def switch_activity(phrase):
	switcher = {
		"Sedentary":1,
		"Lightly Active":2,
		"Moderatly Active":3,
		"Very Active":4
	}
	return switcher.get(phrase, "invalid")






main()
if(check==0):
	exit()

customerobj= US.Customer(username)
customerInfo=US.giveCustomerData(customerobj.getname())
mainWindow = Tk()
mainWindow.title("Fitness Program Demo")
messagebox.showinfo('Thank you', 'Thank you for using my demo.\nPlease consider that I am not a medical professional. All research for this project is limited.')
focus=customerobj.BMI_presenter()
global var

def nextday():
	var=IntVar(0)
	DayLabel.config(text="Day: "+str(customerobj.update_day()))
	natcalchanged=int(customerobj.getNetCal())
	customerobj.update_netcal(natcalchanged)
	customerobj.update_file([float(customerobj.getweight()),int(customerobj.getDay())])
	calIntakeNumLabel.config(text=customerobj.getBMR())
	netCalNumLabel.config(text=0)
	calBurnNumLabel.config(text=0)
	BMRNumLabel.config(text=customerobj.getBMR())
	BMINumLabel.config(text=customerobj.getBMI())
	BMIGoalNumLabel.config(text=customerobj.BMI_goal())

DayLabel = Label(mainWindow, text="Day: "+str(customerobj.getDay()),font=("Helvetica",18),bd=1,justify="left")
DayLabel.grid(row=0,column=1)
nextDayButton= Button(mainWindow,text="Next Day-->",command=nextday)
nextDayButton.grid(row=0,column=3)

CalSummary = LabelFrame(mainWindow, text="CalSummary", padx=100, pady=150)
CalSummary.grid(row=1,column=2)

calIntakeLabel = Label(CalSummary, text="Calorie Intake:",font=("Helvetica",14),justify="left")
calIntakeLabel.grid(row=0,column=0)
calIntakeNumLabel = Label(CalSummary, text=str(customerobj.getBMR()),font=("Helvetica",12),justify="left")
calIntakeNumLabel.grid(row=1,column=0)

calBurnLabel = Label(CalSummary, text="Calorie Burnt:",font=("Helvetica",14),justify="left")
calBurnLabel.grid(row=0,column=2)
calBurnNumLabel = Label(CalSummary, text=0,font=("Helvetica",12),justify="left")
calBurnNumLabel.grid(row=1,column=2)

netCalLabel = Label(CalSummary, text="Net Calories:",font=("Helvetica",14),justify="left")
netCalLabel.grid(row=2,column=1)
netCalNumLabel = Label(CalSummary, text=customerobj.getNetCal(),font=("Helvetica",12),justify="left")
netCalNumLabel.grid(row=3,column=1)


BMRLabel = Label(CalSummary, text="BMR: ",font=("Helvetica",14),justify="left")
BMRLabel.grid(row=7,column=0)
BMRNumLabel = Label(CalSummary, text=customerobj.getBMR(),font=("Helvetica",12),justify="left")
BMRNumLabel.grid(row=8,column=0)

BMILabel = Label(CalSummary, text="BMI: ",font=("Helvetica",14),justify="left")
BMILabel.grid(row=9,column=0)
BMINumLabel = Label(CalSummary, text=customerobj.getBMI(),font=("Helvetica",12),justify="left")
BMINumLabel.grid(row=10,column=0)

BMIGoalLabel = Label(CalSummary, text="BMI Goal: ",font=("Helvetica",14),justify="left")
BMIGoalLabel.grid(row=11,column=0)
BMIGoalNumLabel = Label(CalSummary, text=customerobj.BMI_goal(),font=("Helvetica",12),justify="left")
BMIGoalNumLabel.grid(row=12,column=0)

WorkoutSummary = LabelFrame(mainWindow, text="Workouts", padx=200, pady=150)
WorkoutSummary.grid(row=1,column=3)
my_ListBox=Listbox(WorkoutSummary,width=50)
my_ListBox.grid(row=5,column=0)	
var = IntVar()


def presentWorkouts():
	choice = var.get()
	if choice==1:
		my_ListBox.delete('0','end')
		my_List=my_ListBox.insert(END, customerobj.running(8.3,customerobj.getFocus(),1))
		calBurnNumLabel.config(text=customerobj.calTarget)
		netCalNumLabel.config(text=customerobj.getNetCal())	
	if choice==2:
		my_ListBox.delete('0','end')
		my_List=my_ListBox.insert(END, customerobj.running(9.8,customerobj.getFocus(),2))
		calBurnNumLabel.config(text=customerobj.calTarget)
		netCalNumLabel.config(text=customerobj.getNetCal())	
	if choice==3:
		my_ListBox.delete('0','end')
		my_List=customerobj.Workouts(10,customerobj.getFocus(),1,customerobj.calTarget,customerobj.getKgWeight())
		for item in my_List:
			my_ListBox.insert("end", item)
		calBurnNumLabel.config(text=customerobj.calTarget)
		netCalNumLabel.config(text=customerobj.getNetCal())	
	if choice==4:
		my_ListBox.delete('0','end')
		my_List=customerobj.Workouts(8,customerobj.getFocus(),2,customerobj.calTarget,customerobj.getKgWeight())
		for item in my_List:
			my_ListBox.insert("end", item)
		calBurnNumLabel.config(text=customerobj.calTarget)	
		netCalNumLabel.config(text=customerobj.getNetCal())	
	if choice==5:
		my_ListBox.delete('0','end')
		my_List=customerobj.Workouts(6,customerobj.getFocus(),3,customerobj.calTarget,customerobj.getKgWeight())
		for item in my_List:
			my_ListBox.insert("end", item)
		calBurnNumLabel.config(text=customerobj.calTarget)
		netCalNumLabel.config(text=customerobj.getNetCal())	
	my_ListBox.grid(row=5,column=0)	





option1=Radiobutton(WorkoutSummary, text="Light Jog", variable=var, value=1,command=presentWorkouts)
option1.grid(row=0,column=0)
option2=Radiobutton(WorkoutSummary, text="Running", variable=var, value=2,command=presentWorkouts)
option2.grid(row=1,column=0)
option3=Radiobutton(WorkoutSummary, text="Light Workout", variable=var, value=3,command=presentWorkouts)
option3.grid(row=2,column=0)
option4=Radiobutton(WorkoutSummary, text="Moderate Workout", variable=var, value=4,command=presentWorkouts)
option4.grid(row=3,column=0)
option5=Radiobutton(WorkoutSummary, text="Intense Workout", variable=var, value=5,command=presentWorkouts)
option5.grid(row=4,column=0)


mainWindow.mainloop()

