from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3

root=Tk()
root.title('Student Management System') 
root.iconbitmap("building.ico")
root.maxsize(width=1520, height=900)
root.minsize(width=1520, height=900)
root.config(bg='lightgrey')

#photo
image_background=ImageTk.PhotoImage(Image.open('homepage.jpg'))
label=Label(image=image_background)
label.place(x=0,y=0,width=1535)


#frame
frame = LabelFrame(root,relief='raised',bg='lightblue')
frame.place(x=320, y=60,width=900, height=680) 

#heading
Reg_name=Label(frame,text='Student Registration Form', bg='lightblue', font=("times new roman",24,"bold"))
Reg_name.place(x=280,y=10)

#using label, place for all the details
name=Label(frame,text="Name: ",bg='lightblue', font=("times new roman",14,"bold"))
name.place(x=35,y=120)   

f_name=Label(frame,text='Father Name: ',bg='lightblue',font=("times new roman",14,"bold"))
f_name.place(x=30,y=160)

m_name=Label(frame,text='Mother Name: ',bg='lightblue',font=('times new roman',14,'bold'))
m_name.place(x=30,y=200)

number=Label(frame, text='Phone number: ',bg='lightblue',font=("times new roman",14,"bold"))
number.place(x=30,y=240)   

email=Label(frame, text='Email:',bg='lightblue',font=("times new roman",14,"bold"))
email.place(x=30,y=280) 

gender=Label(frame, text='Gender: ',bg='lightblue',font=("times new roman",14,"bold"))
gender.place(x=30,y=320) 

dob=Label(frame, text='Date Of Birth: ',bg='lightblue',font=("times new roman",14,"bold"))
dob.place(x=30,y=360)

address=Label(frame, text='Address: ',bg='lightblue',font=("times new roman",14,"bold"))
address.place(x=30,y=400)

course=Label(frame, text='Course: ',bg='lightblue',font=("times new roman",14,"bold"))
course.place(x=30,y=440) 

emergency_contact=Label(frame, text='Emergency Contact: ',bg='lightblue',font=("times new roman",14,"bold"))
emergency_contact.place(x=30,y=480) 

blood_group=Label(frame, text='Blood Group: ',bg='lightblue',font=("times new roman",14,"bold"))
blood_group.place(x=30,y=520)


#using entry for the above details
entry_name = Entry(frame)
entry_name.place(x=250, y=125, width=430)  # entry for name

entry_fname = Entry(frame)
entry_fname.place(x=250, y=165, width=430)  # entry for father name

entry_mname = Entry(frame)
entry_mname.place(x=250, y=205, width=430)  # entry for mother name

entry_number = Entry(frame)
entry_number.place(x=250, y=245, width=430)  # entry for Phone number

entry_email = Entry(frame)
entry_email.place(x=250, y=285, width=430)  # entry for email

entry_dob_year = Entry(frame)
entry_dob_year.place(x=250, y=365, width=90)  # entry for date of birth
entry_dob_month = Entry(frame)
entry_dob_month.place(x=440, y=365, width=70)  # entry for date of birth
entry_dob_date = Entry(frame)
entry_dob_date.place(x=610, y=365, width=70)  # entry for date of birth

entry_address = Entry(frame)
entry_address.place(x=250, y=405, width=430)  # entry for address

entry_course = Entry(frame)
entry_course.place(x=250, y=445, width=430)  # entry for course

entry_emenum = Entry(frame)
entry_emenum.place(x=250, y=485, width=430)  # entry for emergency contact

entry_blood = Entry(frame)
entry_blood.place(x=250, y=525, width=430)  # entry for blood group 



#gender radiobutton
def gen():
    print(var.get())
var=IntVar()
r1=Radiobutton(frame,text="male",bg='lightblue',variable=var,value=1,command=gen)
r1.place(x=250,y=325)
r2=Radiobutton(frame,text="Female",bg='lightblue',variable=var,value=2,command=gen)
r2.place(x=370,y=325)
r3=Radiobutton(frame,text="Other",bg='lightblue',variable=var,value=3,command=gen)
r3.place(x=500,y=325)


#DOB
dob=Label(frame, text='Year',bg='lightblue',font=("times new roman",14))
dob.place(x=350,y=360) 
dob=Label(frame, text='Month ',bg='lightblue',font=("times new roman",14))
dob.place(x=520,y=360) 
dob=Label(frame, text='Date',bg='lightblue',font=("times new roman",14))
dob.place(x=690,y=360) 



# Function to validate form fields
def validate_fields():
    email=entry_email.get()             #email should contain @gmail.com
    
    if entry_name.get()=='' or entry_fname.get()=='' or entry_mname.get()=='' or entry_number.get()=='' or entry_email.get()=='' or var.get()==0 or entry_dob_year.get()=='' or entry_dob_month.get()=='' or entry_dob_date.get()=='' or entry_address.get()=='' or entry_course.get()=='' or entry_emenum.get()=='' or entry_blood.get()=='' :
        messagebox.showerror('Error!', 'Please fill up all the required details.')

    elif not entry_number.get().isdigit():
        messagebox.showerror("Error",'"Please enter a valid numeric phone number')
                                        
    elif '@gmail.com' not in email:                               #email should contain @gmail.com
        messagebox.showerror("Invalid Email", "Please enter a valid Gmail address")
    
    elif not entry_emenum.get().isdigit():
        messagebox.showerror("Error",'"Please enter a valid numeric emergency number')

    else:    
        add_student()
        messagebox.showinfo('success',"You have been registered!")
        root.destroy() # Close the registration window
        import login  # Navigate to the login window

# Function to add student details to the database
def add_student():
    # Retrieve data from entry widgets
    name = entry_name.get()
    father_name = entry_fname.get()
    mother_name = entry_mname.get()
    phone_number = entry_number.get()
    email = entry_email.get()
    gender = var.get()
    dob_year = entry_dob_year.get()
    dob_month = entry_dob_month.get()
    dob_date = entry_dob_date.get()
    address = entry_address.get()
    course = entry_course.get()
    emergency_contact = entry_emenum.get()
    blood_group = entry_blood.get()


    # Database connection
    conn = sqlite3.connect('Form.db')
    cursor = conn.cursor()

    # Create student details table if not exists
    cursor.execute("""CREATE TABLE IF NOT EXISTS students(
               ID INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               father_name TEXT,
               mother_name TEXT,
               phone_number TEXT,
               email TEXT,
               gender TEXT,
               dob_year INTEGER,
               dob_month INTEGER,
               dob_date INTEGER,
               address TEXT,
               course TEXT,
               emergency_contact TEXT,
               blood_group TEXT
    )""")

    # Insert student details into students table
    cursor.execute("INSERT INTO students (name, father_name, mother_name, phone_number, email, gender, dob_year, dob_month, dob_date, address, course, emergency_contact, blood_group) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (name, father_name, mother_name, phone_number, email, gender, dob_year, dob_month, dob_date, address, course, emergency_contact, blood_group))
    conn.commit()
    conn.close()
    


# Function to retrieve and display student information
def retrieve_info(student_id=None):
    # Connect to the database
    conn = sqlite3.connect('Form.db')
    cursor = conn.cursor()

    # If student_id is provided, retrieve information for that specific student
    if student_id:
        cursor.execute("SELECT * FROM students WHERE ID=?", (student_id,))
    else:
        # If student_id is not provided, retrieve information for all students
        cursor.execute("SELECT * FROM students")
    
    students = cursor.fetchall()

    # Close the connection
    conn.close()

    # Display retrieved student details
    info_message = "Registered Students:\n\n"
    for student in students:
        info_message += f"Name: {student[1]}\n"
        info_message += f"Father's Name: {student[2]}\n"
        info_message += f"Mother's Name: {student[3]}\n"
        info_message += f"Phone Number: {student[4]}\n"
        info_message += f"Email: {student[5]}\n"
        info_message += f"Gender: {student[6]}\n"
        info_message += f"Date of Birth: {student[7]}\n"
        info_message += f"Address: {student[8]}\n"
        info_message += f"Course: {student[9]}\n"
        info_message += f"Emergency Contact: {student[10]}\n"
        info_message += f"Blood group: {student[11]}\n\n"
    messagebox.showinfo("Registered Students", info_message)
   
# Function to delete all student records
def delete_all_students():
    # Connect to the database
    conn = sqlite3.connect('Form.db')
    cursor = conn.cursor()

    # Execute the DELETE statement to remove all records from the students table
    cursor.execute("DELETE FROM students")

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "All student records have been deleted.")

    #Clearing the entry fields after data insertion
    entry_name.delete(0,END)
    entry_fname.delete(0,END)
    entry_mname.delete(0,END)
    entry_number.delete(0,END)
    entry_email.delete(0,END)
    entry_dob_year.delete(0,END)
    entry_dob_month.delete(0,END)
    entry_dob_date.delete(0,END)
    entry_address.delete(0,END)
    entry_course.delete(0,END)
    entry_emenum.delete(0,END)
    entry_blood.delete(0,END)
    





#button for sign up
btn=Button(text='SIGN UP',relief='raised',font=("times new roman",12),command=validate_fields)
btn.place(x=700,y=680,width=90,height=30)

# INFO button
info_btn = Button(text='INFO', relief='raised', font=("times new roman", 12), command=retrieve_info)
info_btn.place(x=600, y=680, width=90, height=30)

# Button to delete all student records
delete_btn = Button(text='DELETE', relief='raised', font=("times new roman", 12), command=delete_all_students)
delete_btn.place(x=800, y=680, width=90, height=30)

root.mainloop()