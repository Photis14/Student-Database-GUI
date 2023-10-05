from tkinter import *
import tkinter as tk
from tkinter import ttk
from cgitb import text
from turtle import bgcolor, width
import random


#----------------------------------------------------------------------------------------
#tkinter gui setup
tkmaster = tk.Tk()
col = ('i_d', 'first_name', 'last_name', 'ssn', 'major', 'dob', 'address', 'gpa')
c = ttk.Treeview(tkmaster, col=col, show='headings')
cnames = ["-", "First Name", "Last Name", 'SSN', 'Major', 'Date Of Birth', 'Address', 'GPA']
c.column('i_d', width=90)
c.column('first_name', width=110)
c.column('last_name', width=110)
c.column('ssn', width=100)
c.column('major', width=110)
c.column('dob', width=100)
c.column('address', width=350)
c.column('gpa', width=60)

#----------------------------------------------------------------------------------------
#variables
id_add = tk.StringVar()
id_update = tk.StringVar()
id_delete = tk.StringVar()
first_name_ = tk.StringVar()
last_name_ = tk.StringVar()
s_s_n_ = tk.StringVar()
_major_ = tk.StringVar()
_dob_ = tk.StringVar()
_address_ = tk.StringVar()
_gpa_ = tk.StringVar()
_newData_ = tk.StringVar()
_updateDataSel_ = tk.StringVar()
_filter_gpa_ = tk.StringVar()
filter_gpa__ = tk.StringVar()
_filter_dob_ = tk.StringVar()
_filter_dob__ = tk.StringVar()
# _filter_ID = tk.StringVar()
# _filter_ID_ = tk.StringVar()

#----------------------------------------------------------------------------------------
#basic functions
#read
def read_txt_f():
    txt_f = open("Student_Database.txt", "r")
    lines = txt_f.readlines()
    list_students = []
    for i in lines:
        x = i.split("|")
        list_students.append(x)
    return list_students

#clear
def table_clear():
    for item in c.get_children():
        c.delete(item)
    students = read_txt_f()
    for s in students:
        c.insert('', tk.END, values=s)

#clear sort
def table_clearSort(list_):
    for item in c.get_children():
        c.delete(item)
    for s in list_:
        c.insert('', tk.END, values=s)

#add to file
def addStudentTotxt_f(id, firstname, lastname, ssn, major, dob, address, gpa):
    studentinfo = id+"|"+firstname+"|"+lastname+"|"+ssn+"|"+major+"|"+dob+"|"+address+"|"+gpa
    f = open("Student_Database.txt", "a")
    f.write(studentinfo + "\n")
    f.close()

#del from file
def delStudentFromtxt_f(id):
    id_todelete = str(id)
    txt_f = open("Student_Database.txt", "r")
    lines = txt_f.readlines()
    list_students = []
    for i in lines:
        x = i.split("|")
        list_students.append(x)
    for i in list_students:
        for j in i:
            if (j == id_todelete):
                print(i)
                list_students.remove(i)
    txt_f.close()
    f = open("Student_Database.txt", "w")
    for i in list_students:
        studentinfo = i[0]+"|"+i[1]+"|"+i[2]+"|"+i[3]+"|"+i[4]+"|"+i[5]+"|"+i[6]+"|"+i[7]
        f.write(studentinfo)
    f.close()

#----------------------------------------------------------------------------------------
#techinical functions
#update
def updateStudent(id, newData, position):
    id_todelete = str(id)
    txt_f = open("Student_Database.txt", "r")
    lines = txt_f.readlines()
    list_students = []
    for i in lines:
        x = i.split("|")
        list_students.append(x)
    for i in list_students:
        if (i[0] == id_todelete):
            if (position == "First Name"):
                i[1] = newData
            elif (position == "Last Name"):
                i[2] = newData
            elif (position == "SSN"):
                i[3] = newData
            elif (position == "Major"):
                i[4] = newData
            elif (position == "Date Of Birth"):
                i[5] = newData
            elif (position == "Address"):
                i[6] = newData
            else:
                i[7] = newData + "\n"
    txt_f.close()
    f = open("Student_Database.txt", "w")
    for i in list_students:
        studentinfo = i[0]+"|"+i[1]+"|"+i[2]+"|"+i[3]+"|"+i[4]+"|"+i[5]+"|"+i[6]+"|"+i[7]
        f.write(studentinfo)
    f.close()

#----------------------------------------------------------------------------------------
#query functions
def filter_GPA_(from_, to_):
    list_students = read_txt_f()
    filtered_student_list = []
    for i in list_students:
        if (float(i[7]) >= float(from_) and float(i[7]) <= float(to_)):
            filtered_student_list.append(i)
    return filtered_student_list

def filterB_DOB(from_, to_):
    list_students = read_txt_f()
    filtered_student_list = []
    for i in list_students:
        if ((i[5] >= from_) and (i[5] <= to_)):
            filtered_student_list.append(i) 
    return filtered_student_list

#----------------------------------------------------------------------------------------
#click functions
#add backend
def addStudent_c():
    id = str(id_add.get())
    firstname = str(first_name_.get())
    lastname = str(last_name_.get())
    ssn = str(s_s_n_.get())
    major = str(_major_.get())
    dob = str(_dob_.get())
    address = str(_address_.get())
    gpa = str(_gpa_.get())
    addStudentTotxt_f(id, firstname, lastname, ssn, major, dob, address, gpa)
    id_add.set("")
    first_name_.set("")
    last_name_.set("")
    s_s_n_.set("")
    _major_.set("")
    _dob_.set("")
    _address_.set("")
    _gpa_.set("")
    table_clear()

#delete backend
def delStudent_c():
    id = str(id_delete.get())
    delStudentFromtxt_f(id)
    id_delete.set("")
    table_clear()

#update backend
def upStudent_c():
    id= str(id_update.get())
    newData = str(_newData_.get())
    position= str(_updateDataSel_.get())
    updateStudent(id,newData, position)
    id_update.set("")
    _newData_.set("")
    _updateDataSel_.set("")
    table_clear()


#----------------------------------------------------------------------------------------
#query backend
def filter_GPA_c():
    from_ = float(_filter_gpa_.get())
    to_ = float(filter_gpa__.get())
    filtered_list = filter_GPA_(from_, to_)
    _filter_gpa_.set("")
    filter_gpa__.set("")
    table_clearSort(filtered_list)


def filterB_DOB_c():
    from_ = str(_filter_dob_.get())
    to_ = str(_filter_dob__.get())
    filtered_list = filterB_DOB(from_, to_)
    _filter_dob_.set("")
    _filter_dob__.set("")
    table_clearSort(filtered_list)
    
      
#----------------------------------------------------------------------------------------
#clear backend
def unsort_Table_c():
    table_clear()

#----------------------------------------------------------------------------------------
#main function
def main() :
#Section titles 
#MAIN TITLE  
    ADD_Student_Frame = LabelFrame(tkmaster, text=" STUDENT INPUT ",font='Lato 12 bold', fg='blue',highlightbackground="blue", highlightthickness=3, padx=30, pady=10)
    ADD_Student_Frame.grid(row=0, column=0)

#STUDENT INPUT SUB
    Student_Input_Frame = LabelFrame(ADD_Student_Frame, text="ADD NEW STUDENT",font='Lato 10 bold', fg='blue',highlightbackground="blue", highlightthickness=2, padx=20, pady=10)
    Student_Input_Frame.grid(row=0, column=0, padx=10)

#STUDENT UPDATE TITLE
    Student_UpdateFrame = LabelFrame(ADD_Student_Frame, text= "UPDATE STUDENT",font='Lato 10 bold', fg='blue',highlightbackground="blue", highlightthickness=2, padx=20, pady=19)
    Student_UpdateFrame.grid(row=0, column=1, padx=10)

#STUDENT DELELTE TITLE
    Delete_StudentFrame = LabelFrame(ADD_Student_Frame, text= "DELETE STUDENT",font='Lato 10 bold', fg='blue',highlightbackground="blue", highlightthickness=2, padx=20, pady=68)
    Delete_StudentFrame.grid(row=0, column=2, padx=10)


#SORT FUNCTIONS SUB
    Sort_ButtonsFrame = LabelFrame(text="Sort By :",font='Lato 10 bold', fg='blue',highlightbackground="blue", highlightthickness=2, padx=10, pady=2)
    Sort_ButtonsFrame.grid(row=0, column=1)

#QUERY SUB
    queryFrame = LabelFrame(text="Query:",font='Lato 10 bold', fg='blue',highlightbackground="blue", highlightthickness=2, padx=10, pady=1)
    queryFrame.grid(row=2, column=0)

#DATA TABLE
    c.grid(row=3 ,column=0, padx=50)
    c.heading('i_d', text='ID')
    c.heading('first_name', text='FIRST NAME')
    c.heading('last_name', text='LAST NAME')
    c.heading('ssn', text='SSN')
    c.heading('major', text='MAJOR')
    c.heading('dob', text='DOB')
    c.heading('address', text='ADDRESS')
    c.heading('gpa', text='GPA')

#----------------------------------------------------------------------------------------
#Widgets
    AddButton = tk.Button(Student_Input_Frame, text="ADD STUDENT", font='Lato 12 bold',command=addStudent_c, padx=10, pady= 20, bg = 'blue' )
    IDLableInput =  Label(Student_Input_Frame, text = "ID", pady=10)
    FirstNameLabelInput = Label(Student_Input_Frame, text = "First Name", pady=10)
    LastNameLabelInput = Label(Student_Input_Frame, text = "Last Name", pady=10)
    SSNLabelInput = Label(Student_Input_Frame, text = "SSN ", pady=10)
    MajorLabelInput = Label(Student_Input_Frame, text = "Major", pady=10)
    DOBLabelInput = Label(Student_Input_Frame, text = "Date of Birth", pady=10)
    AddressLabelInput = Label(Student_Input_Frame, text = "Address", pady=10)
    GPALabelInput = Label(Student_Input_Frame, text = "GPA", pady=10)

    IDEntryInput = tk.Entry(Student_Input_Frame, textvariable= id_add, width =50)
    FirstNameEntryInput = Entry(Student_Input_Frame, textvariable=first_name_, width =50)
    LastNameEntryInput = Entry(Student_Input_Frame, textvariable=last_name_, width =50)
    SSNEntryInput = Entry(Student_Input_Frame, textvariable= s_s_n_, width =50)
    MajorEntryInput = Entry(Student_Input_Frame, textvariable= _major_, width =50)
    DOBEntryInput = Entry(Student_Input_Frame, textvariable= _dob_, width =50)
    AddressEntryInput = Entry(Student_Input_Frame, textvariable= _address_, width =50)
    GPAEntryInput = Entry(Student_Input_Frame, textvariable= _gpa_, width =50)
#INPUT TEXT LOCATIONS
    IDLableInput.grid(row =1  ,column = 0)
    FirstNameLabelInput.grid(row =2 ,column = 0)
    LastNameLabelInput.grid(row =3 ,column = 0)
    SSNLabelInput.grid(row = 4, column=0)
    MajorLabelInput.grid(row = 5, column=0)
    DOBLabelInput.grid(row = 6, column=0)
    AddressLabelInput.grid(row = 7, column=0)
    GPALabelInput.grid(row = 8, column=0)
#INPUT ENTRY LOCATIONS
    IDEntryInput.grid(row = 1, column=1)
    FirstNameEntryInput.grid(row = 2, column=1)
    LastNameEntryInput.grid(row = 3, column=1)
    SSNEntryInput.grid(row =4  ,column = 1)
    MajorEntryInput.grid(row =5  ,column = 1)
    DOBEntryInput.grid(row =6  ,column = 1)
    AddressEntryInput.grid(row =7  ,column = 1)
    GPAEntryInput.grid(row = 8 ,column = 1)
#ADD STUDENT BUTTON LOCATION
    AddButton.grid(row= 1, column= 3)
#----------------------------------------------------------------------------------------
#Update Widgets
    UpdateIDLabel = Label(Student_UpdateFrame, text =  "ID", pady=10)
    UpdateIDLabel.grid(row=0, column=0)
    UpdateInputLabel = Label(Student_UpdateFrame, textvariable=_updateDataSel_)
    UpdateInputLabel.grid(row=2, column=0)
    
    UpdateOptionMenuLabel = Label(Student_UpdateFrame, text =  "Data to Update ", pady=25)
    UpdateOptionMenuLabel.grid(row=1, column=0, padx=10)
    
    DataEntryLabel = Label(Student_UpdateFrame, text =  "Enter Data", pady=10)
    DataEntryLabel.grid(row=2, column=0)
 
#----------------------------------------------------------------------------------------
#Update Boxes
    UpdateIDEntry = tk.Entry(Student_UpdateFrame, textvariable= id_update, width =20)
    UpdateIDEntry.grid(row = 0,column = 1)
    UpdateNewData = tk.Entry(Student_UpdateFrame, textvariable=_newData_, width = 20)
    UpdateNewData.grid(row =2, column=1)

    UpdateComboBox = ttk.Combobox(Student_UpdateFrame, width = 20,textvariable= _updateDataSel_ )
    UpdateComboBox['values'] = ('First Name', 'Last Name', 'SSN', 'Major', 'Date Of Birth', 'Address', 'GPA')
    UpdateComboBox.grid(row=1, column=1)
    
    UpdateButton = tk.Button(Student_UpdateFrame, text="UPDATE STUDENT", font='Lato 12 bold', command=upStudent_c, padx=10, pady= 20, bg = 'blue' )
    UpdateButton.grid(row=3, column=1, pady = 5)
#----------------------------------------------------------------------------------------
#Delete Widgets
    DeleteButton = tk.Button(Delete_StudentFrame, text="DELETE STUDENT", font='Lato 12 bold', command=delStudent_c, padx=10, pady= 20, bg = 'blue' )
    DeleteIDLabel = Label(Delete_StudentFrame, text =  "ID", pady=10)
    DeleteIDEntry = tk.Entry(Delete_StudentFrame, textvariable= id_delete, width =20)
    DeleteIDLabel.grid(row = 0,column = 0)
    DeleteIDEntry.grid(row = 0,column = 1)
    DeleteButton.grid(row =1, column=1)

#Unsort Button
    unsort_table_button = tk.Button(tkmaster, text="UNSORT TABLE", font= 'Lato 12 bold', command= unsort_Table_c, padx=1, pady=2, height=8, width=50, bg= 'blue')                                      
    unsort_table_button.grid(row=3, column=1, padx = 0)

#FilterBy Frame Widgets
#GPA Filter
    GPALabel = Label(queryFrame, text =  "GPA", pady=10)
    GPALabel.grid(row=0, column=1)
    LabelFromGPA = Label(queryFrame, text = "Start" , pady=10)
    LabelFromGPA.grid(row=1, column=0)
    LabelToGPA = Label(queryFrame, text = "Stop" , pady=10)
    LabelToGPA.grid(row=2, column=0)
    
    FilterFromEntryGPA = tk.Entry(queryFrame, textvariable= _filter_gpa_, width =20)
    FilterFromEntryGPA.grid(row=1, column=1)
    FilterToEntryGPA = tk.Entry(queryFrame, textvariable= filter_gpa__, width =20)
    FilterToEntryGPA.grid(row=2, column=1)   
    
    GPAButton = tk.Button(queryFrame, text="FIND", font='Lato 12 bold', command=filter_GPA_c, padx=10, pady= 20, height=1, width=12, bg = 'blue' )
    GPAButton.grid(row=3, column=1)
    
#DOB Filter    
    DOBLabel = Label(queryFrame, text =  "Date of Birth", pady=10)
    DOBLabel.grid(row=0, column=3)
    LabelFromDOB = Label(queryFrame, text = "Start" , pady=10)
    LabelFromDOB.grid(row=1, column=2)
    LabelToDOB = Label(queryFrame, text = "Stop" , pady=10)
    LabelToDOB.grid(row=2, column=2)
    
    FilterFromEntryDOB = tk.Entry(queryFrame, textvariable= _filter_dob_, width =20)
    FilterFromEntryDOB.grid(row=1, column=3)
    FilterToEntryDOB = tk.Entry(queryFrame, textvariable= _filter_dob__, width =20)
    FilterToEntryDOB.grid(row=2, column=3)
    
    DOBButton = tk.Button(queryFrame, text="FIND", font='Lato 12 bold', command=filterB_DOB_c, padx=10, pady= 20, height=1, width=12, bg = 'blue' )
    DOBButton.grid(row=3, column=3)
    
#----------------------------------------------------------------------------------------
#text loop
    students = read_txt_f()
    for s in students:
        c.insert('', tk.END, values=s)

    tkmaster.mainloop()

main()