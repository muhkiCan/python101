from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk()
GUI.title('คำนวน BMI')
GUI.geometry('360x200')

text_header = Label(GUI, text='คำนวน BMI',font=('Angsana New',30),fg='green')
text_header.grid(row=0, column=0)

Label(GUI,text='height (cm) : ',font=('Angsana New',18)).grid(row=1)
Label(GUI,text='weight (Kg) :',font=('Angsana New',18)).grid(row=2)

entry_height = Entry(GUI,font=('Angsana New',18))
entry_weight = Entry(GUI,font=('Angsana New',18))

entry_height.grid(row=1, column=1)
entry_weight.grid(row=2, column=1)

def CheckNum(height, weight): 

        try : 
             float(height) and float(weight)
        except : 
                show_messagebox("Error","Plase input number only")

        h,w  = float(height),float(weight)

        if h < 1 or w  < 1: 
                show_messagebox("Error","Plase input more than 0")
        elif h > 300 and  w > 500: 
                show_messagebox("Error","Error, maximum number")
        else : 
                return float(height), float(weight)

             

def CAL_BMI() : 
    height, weight = CheckNum(entry_height.get(), entry_weight.get())

    BMI = round(weight/pow((height/100),2),2)

    if BMI > 30 : 
            message = 'BMI : {} \nอยู่ในเกณฑ์ อ้วนมาก'.format(str(BMI))
    elif BMI > 25 : 
            message = 'BMI : {} \nอยู่ในเกณฑ์ อ้วน'.format(str(BMI))
    elif BMI > 23 : 
            message = 'BMI : {} \nอยู่ในเกณฑ์ ท้วม'.format(str(BMI))
    elif BMI > 18.50 : 
            message = 'BMI : {} \nอยู่ในเกณฑ์ น้ำหนักปกติ'.format(str(BMI))
    else : 
            message = 'BMI : {} \nอยู่ในเกณฑ์ น้ำหนักน้อยกว่ามาตรฐาน'.format(str(BMI))
    
    show_messagebox('Result',message)

def show_messagebox(status,message) : 
    messagebox.showinfo(status,message)

button_cal =  Button(GUI,text='Calculate', command=CAL_BMI, font=('Angsana New',16)).grid(
    row=4,column=0,sticky='ew',pady=4)

button_exit = Button(GUI,text='Exit', command=GUI.quit, font=('Angsana New',16)).grid(
    row=4,column=1,sticky='ew',pady=4)

GUI.mainloop()