from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import sqlite3
import datetime  # Add this import

# Function to create the students table if it doesn't exist
def create_students_table():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            class TEXT,
            roll INTEGER,
            section TEXT,
            number TEXT,
            email TEXT,
            gender TEXT,
            dob TEXT,
            address TEXT,
            course TEXT
        )
    """)
    conn.commit()
    conn.close()

# Function to handle submission and storing of student details
def homepage():
    name = entry_name.get()
    class_ = entry_class.get()
    roll = entry_roll.get()
    section = section_var.get()
    number = entry_number.get()
    email = entry_email.get()
    gender = gender_var.get()
    dob = entry_dob.get()
    address = entry_address.get()
    course = course_var.get()

    if '@gmail.com' not in email:
        messagebox.showerror("Invalid Email", "Please enter a valid Gmail address.")
        return

    if not number.isdigit():
        messagebox.showerror("Invalid Number", "Please enter a valid numeric phone number.")
        return

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO students (name, class, roll, section, number, email, gender, dob, address, course)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (name, class_, roll, section, number, email, gender, dob, address, course))

    conn.commit()
    conn.close()

    clear_entries()

    messagebox.showinfo('Success', 'Student details added successfully!')
    root.destroy()

def clear_entries():
    entry_name.delete(0, END)
    entry_class.delete(0, END)
    entry_roll.delete(0, END)
    entry_number.delete(0, END)
    entry_email.delete(0, END)
    entry_dob.set_date(datetime.date(2000, 1, 1))  # Set default date
    entry_address.delete(0, END)

create_students_table()

root = Tk()
root.title("Student Management System")
root.geometry("800x600")
root.config(bg='lightblue')

navbar_frame = Frame(root, bg='lightgrey')
navbar_frame.pack(side=TOP, fill=X)

Label(navbar_frame, text='Add Student Details', bg='lightgrey', font=("times new roman", 18, "bold")).pack(pady=10)

card_frame = Frame(root, bg='white', bd=2, relief='raised')
card_frame.pack(padx=50, pady=30, fill=BOTH, expand=True)

canvas = Canvas(card_frame, bg='white')
canvas.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar = Scrollbar(card_frame, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

inner_frame = Frame(canvas, bg='white')
canvas.create_window((0, 0), window=inner_frame, anchor="nw")

Label(inner_frame, text="Name: ", bg='white', font=("times new roman", 16)).grid(row=0, column=0, pady=10, padx=10, sticky="e")
entry_name = Entry(inner_frame)
entry_name.grid(row=0, column=1, pady=10, padx=10, sticky="w")

Label(inner_frame, text="Class: ", bg='white', font=("times new roman", 16)).grid(row=1, column=0, pady=10, padx=10, sticky="e")
entry_class = Entry(inner_frame)
entry_class.grid(row=1, column=1, pady=10, padx=10, sticky="w")

Label(inner_frame, text="Roll No: ", bg='white', font=("times new roman", 16)).grid(row=2, column=0, pady=10, padx=10, sticky="e")
entry_roll = Entry(inner_frame)
entry_roll.grid(row=2, column=1, pady=10, padx=10, sticky="w")

Label(inner_frame, text="Section: ", bg='white', font=("times new roman", 16)).grid(row=3, column=0, pady=10, padx=10, sticky="e")
section_var = StringVar()
section_var.set("A")  # Default value
section_options = ["A", "B", "C", "D"]
section_dropdown = OptionMenu(inner_frame, section_var, *section_options)
section_dropdown.config(bg='white', font=("times new roman", 12))
section_dropdown.grid(row=3, column=1, pady=10, padx=10, sticky="w")

Label(inner_frame, text='Contact number: ', bg='white', font=("times new roman", 16)).grid(row=4, column=0, pady=10, padx=10, sticky="e")
entry_number = Entry(inner_frame)
entry_number.grid(row=4, column=1, pady=10, padx=10, sticky="w")

Label(inner_frame, text='Email:', bg='white', font=("times new roman", 16)).grid(row=5, column=0, pady=10, padx=10, sticky="e")
entry_email = Entry(inner_frame)
entry_email.grid(row=5, column=1, pady=10, padx=10, sticky="w")

Label(inner_frame, text='Gender: ', bg='white', font=("times new roman", 16)).grid(row=6, column=0, pady=10, padx=10, sticky="e")
gender_var = StringVar()
gender_var.set("Male")  # Default value
gender_options = ["Male", "Female", "Others"]
gender_dropdown = OptionMenu(inner_frame, gender_var, *gender_options)
gender_dropdown.config(bg='white', font=("times new roman", 12))
gender_dropdown.grid(row=6, column=1, pady=10, padx=10, sticky="w")

Label(inner_frame, text='Date Of Birth: ', bg='white', font=("times new roman", 16)).grid(row=7, column=0, pady=10, padx=10, sticky="e")
entry_dob = DateEntry(inner_frame, bg='white', font=("times new roman", 12))
entry_dob.grid(row=7, column=1, pady=10, padx=10, sticky="w")
entry_dob.set_date(datetime.date(2000, 1, 1))  # Default date

Label(inner_frame, text='Address: ', bg='white', font=("times new roman", 16)).grid(row=8, column=0, pady=10, padx=10, sticky="e")
entry_address = Entry(inner_frame)
entry_address.grid(row=8, column=1, pady=10, padx=10, sticky="w")

Label(inner_frame, text='Course: ', bg='white', font=("times new roman", 16)).grid(row=9, column=0, pady=10, padx=10, sticky="e")
course_var = StringVar()
course_var.set("BSc (Hons) CS Ai")  # Default value
course_options = ["BSc (Hons) CS Ai", "BSc (Hons) C", "BSc (Hons) EHC", "MSc DSA CI"]
course_dropdown = OptionMenu(inner_frame, course_var, *course_options)
course_dropdown.config(bg='white', font=("times new roman", 12))
course_dropdown.grid(row=9, column=1, pady=10, padx=10, sticky="w")

submit = ttk.Button(inner_frame, text='Submit', command=homepage, style='Submit.TButton')
submit.grid(row=10, columnspan=2, pady=20)

# Style configuration
style = ttk.Style()
style.configure('Submit.TButton', background='lightblue', foreground='black', font=('Helvetica', 12), borderwidth=0)

root.mainloop()
