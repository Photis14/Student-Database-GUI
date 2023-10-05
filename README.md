# Student-Database-GUI
This code provides a simple interface for managing a student database using the Tkinter library. The database stores student information such as ID, First Name, Last Name, SSN, Major, Date of Birth, Address, and GPA.

# Libraries Used:
Tkinter: For the graphical user interface.
random: (imported but not utilized in the provided code).
cgitb: (imported but not utilized in the provided code).
turtle: (imported but not utilized in the provided code).
Application Structure:
GUI Setup:

A main window is initialized using tk.Tk().
A table (ttk.Treeview) is created with columns for each student attribute.

Variables:
StringVar variables are set up for each student attribute to store and manage the data input by the user.

Basic Functions:
read_txt_f(): Reads the Student_Database.txt file and returns a list of student records.
table_clear(): Clears the table and then refills it with the updated data.
table_clearSort(): Clears the table and fills it with a specific sorted list of students.
addStudentTotxt_f(): Appends a new student's information to the Student_Database.txt file.
delStudentFromtxt_f(): Deletes a student's information from the Student_Database.txt file based on the provided ID.
Technical Functions:

updateStudent(): Updates a specific student's attribute in the Student_Database.txt file based on the provided ID.

Query Functions:
filter_GPA_(): Returns a list of students based on a GPA range.
filterB_DOB(): Returns a list of students based on a Date of Birth range.

Click Functions:
These are functions that are triggered when buttons are clicked.
addStudent_c(): Adds a student using the data entered by the user.
delStudent_c(): Deletes a student based on the entered ID.
upStudent_c(): Updates a student's information.
filter_GPA_c() and filterB_DOB_c(): Filters the students based on GPA and Date of Birth, respectively.
unsort_Table_c(): Clears any sorting or filtering and reloads the original data.

Main Function:
Sets up the main sections of the GUI such as the input frames, update frames, delete frames, sort, and query sections.
Also, places widgets like labels, entry boxes, and buttons on the frames.

#Usage:
To add a student, fill in all the details in the "ADD NEW STUDENT" section and click "ADD STUDENT".
To update a student's detail, input the student's ID and select the detail you want to update, then provide the new data and click the update button.
To delete a student, input the student's ID in the "DELETE STUDENT" section and confirm the deletion.
You can also filter the displayed students based on GPA or Date of Birth ranges.

#Note:
This code snippet is not the complete application and may require additional pieces to function properly. Additionally, ensure that the Student_Database.txt file exists and is accessible to prevent any file operation errors.
