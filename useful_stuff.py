import os
import os.path
from tkinter import *
import numpy as np
from tkinter import ttk
from tkinter import messagebox
import random

global workoutDict
global kgWeight
global calTarget



def calculate_BMI_signup(weight,height):
	BMI=(weight/height/height)*703
	return float(f"{BMI:.2f}")	

def calculate_BMR_signup(height,weight,sex,age,activity):
	if sex=="Male":
		BMR=float((4.536*weight)+(15.88*height)-(5*age)+5)
	else:
		BMR=float((4.536*weight)+(15.88*height)-(5*age)-161)
	if activity==1:
		BMR=float(BMR*1.2)
	elif activity==2:
		BMR=float(BMR*1.375)
	elif activity==3:
		BMR=float(BMR*1.55)
	else:
		BMR=float(BMR*1.725)
	return float(f"{BMR:.2f}")	



def createAccount(arrayInfo):
	username=arrayInfo[0]
	arrayInfo[1] = str(arrayInfo[1], "utf-8")
	with open(username+'.txt', 'w') as f:
		for element in arrayInfo:
			f.write(str(element)+"\n")



def METcalc(MET,kgWeight):
	calPerMin=MET*3.5*kgWeight/200
	return (int(calPerMin))

def giveCustomerData(username):
		filename = username+".txt"
		file=open(filename)
		arr = file.read().splitlines()
		arr[3]=int(arr[3])
		arr[5]=int(arr[5])
		arr[6]=float(arr[6])
		arr[7]=int(arr[7])
		arr[8]=int(arr[8])
		arr[9]=float(arr[9])
		arr[10]=float(arr[10])
		arr[11]=int(arr[11])
		return(arr)




class Customer:
	global user
	user=""
	name=""
	age=0
	sex=""
	height=0
	weight=0
	day=1
	BMI=0
	active=1
	netcal=0
	netcaloriginal=0
	BMR=0
	global poundcal
	poundcal=3500
	kgWeight= 0
	calTarget=0
	global focus
	focus=""

	def __init__(self,username):
		self.user=username
		global filename
		filename = self.user+".txt"
		file=open(filename)
		arrayInfo = file.read().splitlines()
		self.name = arrayInfo[2]
		self.age = int(arrayInfo[3])
		self.sex = arrayInfo[4]
		self.height = int(arrayInfo[5])
		self.weight = float(arrayInfo[6])
		self.day = int(arrayInfo[7])
		self.BMI = self.calculate_BMI()
		self.active = int(arrayInfo[8])
		self.BMR = self.calculate_BMR()
		self.netcal = int(arrayInfo[11])
		self.netcaloringal = int(arrayInfo[11])
		self.kgWeight= float(f"{(float(arrayInfo[6])*0.45359237):.2f}")
		self.calTarget=float(f"{self.calculate_BMR():.2f}")

	def calculate_BMI(self):
		self.BMI=(self.weight/self.height/self.height)*703
		return float(f"{self.BMI:.2f}")		

	def calculate_BMR(self):
		if self.sex=="Male":
			self.BMR=(4.536*self.weight)+(15.88*self.height)-(5*self.age)+5	
		else:
			self.BMR=(4.536*self.weight)+(15.88*self.height)-(5*self.age)-161
		return (float(f"{self.BMR:.2f}"))		

	def update_file(self,updateInfoArray):
		#[weight, day]
		with open(filename, 'r') as file:
			arrayInfo = file.readlines()
		arrayInfo[6] = str(updateInfoArray[0])+'\n'
		arrayInfo[7] = str(updateInfoArray[1])+'\n'
		arrayInfo[9] = str(self.calculate_BMI())+'\n'
		arrayInfo[10] = str(self.calculate_BMR())+'\n'
		arrayInfo[11] = str(self.netcal)+'\n'
		with open(filename, 'w') as file:
			file.writelines(arrayInfo)
		file.close()

	def update_day(self):
		self.day+=1
		return(self.day)

	def update_netcal_file(self,changedcal):

		with open(filename, 'r') as file:
			arrayInfo = file.readlines()
		arrayInfo[11] = str(changedcal)+'\n'
		with open(user+'.txt', 'w') as file:
			file.writelines(arrayInfo)
		file.close()

	def update_netcal(self,changedcal):
		if focus=="lose":
			self.netcal-=2*self.netcal
		self.netcal=self.netcal+changedcal
		if self.netcal<=-poundcal:
			self.netcal=self.netcal%-poundcal
			self.weight-=1
			self.update_file([self.weight,self.update_day()])
			self.update_netcal_file(self.netcal)
		elif self.netcal>=poundcal:
			self.netcal=self.netcal%poundcal
			self.weight+=1
			self.update_file([self.weight,self.update_day()])
			self.update_netcal_file(self.netcal)
		else:
			self.update_netcal_file(self.netcal)

	def getDay(self):
		return(self.day)

	def getname(self):
		return(self.user)

	def getcalTarget(self):
		return(self.calTarget)

	def getNetCal(self):
		return(self.netcal)

	def getBMI(self):
		return(self.BMI)

	def getBMR(self):
		return(self.BMR)

	def getweight(self):
		return(self.weight)

	def getKgWeight(self):
		return(self.kgWeight)

	def getFocus(self):
		return(self.focus)

	def getcalTarget(self):
		return(self.calTarget)

	def BMI_presenter(self):
		if (self.BMI<18.5):
			messagebox.showinfo('BMI Results', "Your current BMI is "+str(self.BMI)+". This considered underweight. Let's see how we can raise it.")
			self.focus="gain"
			return(self.focus)
		elif (18.5<self.BMI<24.9):
			messagebox.showinfo('BMI Results', 'Your current BMI is '+str(self.BMI)+". This considered normal weight. Let's maintain that BMI.")
			self.focus="maintain"
			return(self.focus)
		elif (25<self.BMI<29.9):
			messagebox.showinfo('BMI Results', 'Your current BMI is '+str(self.BMI)+". This considered overweight. Let's see how we can lower it.")
			self.focus="lose"
			return(self.focus)
		else:
			messagebox.showinfo('BMI Results', 'Your current BMI is '+str(self.BMI)+". This considered obese. Let's see how we can lower it.")
			self.focus="lose"
			return(self.focus)			

	def BMI_goal(self):
		if (self.focus=="gain"):
			return(18.5)
		elif (self.focus=="maintain"):
			return(21.7)
		else:
			return(24.9)

	def running(self,met,focus,intensity):
		self.calTarget=self.BMR
		self.netcal=self.netcaloriginal
		if (intensity==1 and focus=="gain"):
			self.calTarget-=200
			self.netcal-=200
		elif(intensity==2 and focus=="gain"):
			self.calTarget-=400
			self.netcal-=400
		elif (intensity==1 and focus=="lose"):
			self.calTarget+=200
			self.netcal+=200
		elif(intensity==2 and focus=="lose"):
			self.calTarget+=400
			self.netcal+=400
		else:
			self.calTarget=self.calTarget
		if(met==8.3):
			timeRunning=float(f"{(self.calTarget/self.BMR)*(24/met):.2f}")
			return("Light jog at 5 mph for "+str(timeRunning)+" hours.")
		else:
			timeRunning=float(f"{(self.calTarget/self.BMR)*(24/met):.2f}")
			return("Run at 6 mph for "+str(timeRunning)+" hours.")	


	def Workouts(self,num,focus,intensity,calTarget,kgWeight):
		global workoutMins
		global divCalTarget
		self.calTarget=self.BMR
		self.netcal=self.netcaloriginal
		if (intensity==1 and focus=="gain"):
			self.calTarget-=100
			self.netcal-=100
		elif(intensity==2 and focus=="gain"):
			self.calTarget-=400
			self.netcal-=400
		elif(intensity==3 and focus=="gain"):
			self.calTarget-=600
			self.netcal-=600
		elif (intensity==1 and focus=="lose"):
			self.calTarget+=100
			self.netcal+=100
		elif(intensity==2 and focus=="lose"):
			self.calTarget+=400
			self.netcal+=400
		elif(intensity==3 and focus=="lose"):
			self.calTarget+=600
			self.netcal+=600
		else:
			self.calTarget=self.calTarget
		workoutMins=[]
		divCalTarget=float(self.calTarget/num)
		self.getRandomWorkout(num)
		self.getMins(num,kgWeight)
		return(workoutComplete)


	def getRandomWorkout(self,Num):
		global workoutName
		global workoutMETs
		workoutName=[]
		workoutMETs=[]
		for i in range(Num): 
			workouts=random.choice(list(workoutDict.items()))
			workoutName.append(workouts[0])
			workoutMETs.append(workouts[1])

	def getMins(self,Num,kgWeight):
		global workoutComplete
		workoutComplete=[]
		for i in range(Num): 
			minPerWorkout=0
			calPerWorkout=METcalc(workoutMETs[i],kgWeight)
			while(calPerWorkout<=divCalTarget):
				minPerWorkout+=1
				calPerWorkout+=METcalc(workoutMETs[i],kgWeight)
			workoutMins.append(minPerWorkout)
		for i in range(Num):
			workoutComplete.append(str(workoutMins[i])+" minutes of "+workoutName[i])	

os.chdir(os.getcwd()+"\profiles")

workoutDict = dict()
allWorkouts=open("allworkouts.txt", "r", encoding='utf8') 
for line1 in allWorkouts:
	line1 = line1.strip().split("\t")
	workoutDict[line1[0]] = float(line1[1])