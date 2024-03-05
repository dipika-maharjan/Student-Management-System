from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
import subprocess

# Define functions

def add_student():
    subprocess.run(["python", "add_student.py"])

def update_student():
    # Get the selected item from the Treeview
    selected_item = student_table.focus()
    if not selected_item:
        messagebox.showerror("Error", "Please select a student to update.")
        return

    # Get the values of the selected item
    values = student_table.item(selected_item, "values")

    # Open a new popup window for updating data
    update_window = Toplevel(root)
    update_window.title("Update Student")

    # Create entry fields for updating data
    label_class = Label(update_window, text="Class:")
    label_class.grid(row=0, column=0, padx=10, pady=10)
    entry_class = Entry(update_window)
    entry_class.grid(row=0, column=1, padx=10, pady=10)
    entry_class.insert(0, values[2])  # Populate with current value

    label_roll = Label(update_window, text="Roll No.:")
    label_roll.grid(row=1, column=0, padx=10, pady=10)
    entry_roll = Entry(update_window)
    entry_roll.grid(row=1, column=1, padx=10, pady=10)
    entry_roll.insert(0, values[3])  # Populate with current value

    label_section = Label(update_window, text="Section:")
    label_section.grid(row=2, column=0, padx=10, pady=10)
    entry_section = Entry(update_window)
    entry_section.grid(row=2, column=1, padx=10, pady=10)
    entry_section.insert(0, values[4])  # Populate with current value

    label_course = Label(update_window, text="Course:")
    label_course.grid(row=3, column=0, padx=10, pady=10)
    entry_course = Entry(update_window)
    entry_course.grid(row=3, column=1, padx=10, pady=10)
    entry_course.insert(0, values[10])  # Populate with current value

    # Define function to update data in the database
    def update_data():
        new_class = entry_class.get()
        new_roll = entry_roll.get()
        new_section = entry_section.get()
        new_course = entry_course.get()

        # Update data in the database
        conn = sqlite3.connect('students.db')
        c = conn.cursor()

        # Construct the update query
        c.execute("UPDATE students SET Class=?, Roll=?, Section=?, Course=? WHERE id=?",
                  (new_class, new_roll, new_section, new_course, values[0]))
        conn.commit()

        # Update data in the Treeview
        updated_values = list(values)
        updated_values[2] = new_class
        updated_values[3] = new_roll
        updated_values[4] = new_section
        updated_values[10] = new_course

        student_table.item(selected_item, values=updated_values)

        conn.close()
        update_window.destroy()

    # Add update button
    btn_update = Button(update_window, text="Update", command=update_data)
    btn_update.grid(row=4, columnspan=2, padx=10, pady=10)

def search_student():
    # Get the phone number from the search entry
    phone_number = entry_search.get().strip()

    # If the search entry is empty, show an error message
    if not phone_number:
        messagebox.showerror("Error", "Please enter a phone number to search.")
        return

    # Clear existing records from the Treeview
    student_table.delete(*student_table.get_children())

    # Fetch data from the database matching the entered phone number
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute("SELECT * FROM students WHERE number = ?", (phone_number,))
    records = c.fetchall()
    conn.close()

    # Populate the Treeview with matching records
    for record in records:
        student_table.insert('', 'end', values=record)

def fetch_data_from_db():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    records = c.fetchall()
    conn.close()
    return records

def populate_student_table():
    data = fetch_data_from_db()
    for record in data:
        student_table.insert('', 'end', values=record)

def delete_student():
    # Get the selected item from the Treeview
    selected_item = student_table.selection()
    if not selected_item:
        messagebox.showerror("Error", "Please select a student to delete.")
        return

    # Extract the ID of the selected record
    selected_id = student_table.item(selected_item)['values'][0]

    # Delete the record from the database
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute("DELETE FROM students WHERE id=?", (selected_id,))
    conn.commit()
    conn.close()

    # Remove the selected item from the Treeview
    student_table.delete(selected_item)

def reload_data():
    # Clear existing records from the Treeview
    student_table.delete(*student_table.get_children())
    # Populate the Treeview with updated records
    populate_student_table()

# Create root window
root = Tk()
root.title("Student Management System")
root.maxsize(width=1520, height=900)
root.minsize(width=1520, height=900)

# Define colors
bg_color = '#f0f0f0'
frame_color = '#d3d3d3'
btn_color = '#5c85d6'
nav_color = '#333'

# Create navigation bar
nav_frame = Frame(root, bg=nav_color)
nav_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

# Create labels for navigation bar
login_label = Label(nav_frame, text='Student Management System', bg=nav_color, fg='white', font=("Arial", 24, "bold"))
login_label.pack(pady=10)

label_std1 = Label(nav_frame, text='Options', bg=nav_color, fg='white',font=("Arial", 18, 'bold'))
label_std1.pack(side=LEFT, padx=(20, 40), pady=(20,10))

label_std1 = Label(nav_frame, text='Student Details', bg=nav_color, fg='white',font=("Arial", 18, 'bold'))
label_std1.pack(side=RIGHT, padx=(20, 40), pady=(20,10))

# Create frames
frame1 = Frame(root, bg=frame_color, padx=20, pady=20)
frame1.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

frame2 = Frame(root, bg=frame_color, padx=20, pady=20)
frame2.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

frame3 = Frame(root, bg=frame_color, padx=20, pady=10)
frame3.grid(row=2, column=1, padx=20, pady=10, sticky="ew")

frame4 = Frame(root, bg=frame_color, padx=20, pady=10)
frame4.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

# Create widgets
btn_add = Button(frame1, text='Add', command=add_student, font=("Arial", 14), relief="flat", bg=btn_color, padx=10, pady=5)
btn_add.grid(row=0, column=0, padx=10, pady=10)

btn_delete = Button(frame1, text='Delete', command=delete_student, font=("Arial", 14), relief="flat", bg=btn_color, padx=10, pady=5)
btn_delete.grid(row=0, column=2, padx=10, pady=10)

btn_update = Button(frame1, text='Update', command=update_student, font=("Arial", 14), relief="flat", bg=btn_color, padx=10, pady=5)
btn_update.grid(row=0, column=3, padx=10, pady=10)

# Create reload button
btn_reload = Button(frame1, text='Reload', command=reload_data, font=("Arial", 14), relief="flat", bg=btn_color, padx=10, pady=5)
btn_reload.grid(row=0, column=4, padx=10, pady=10)

# Create frame3
frame3 = Frame(root, bg=frame_color, padx=20, pady=10)
frame3.grid(row=2, column=1, padx=20, pady=10, sticky="ew")

# Create search bar
label_search = Label(frame3, text="Search by Phone Number:", font=("Arial", 14), bg=frame_color)
label_search.grid(row=0, column=0, padx=10, pady=10)
entry_search = Entry(frame3, font=("Arial", 14), width=20)
entry_search.grid(row=0, column=1, padx=10, pady=10)
btn_search = Button(frame3, text='Search', command=search_student, font=("Arial", 14), relief="flat", bg=btn_color, padx=10, pady=5)
btn_search.grid(row=0, column=2, padx=10, pady=10)

# Bind the search function to the Enter key
root.bind('<Return>', lambda event: search_student())

student_table = ttk.Treeview(frame2, columns=('id', 'Name', 'Class', 'Roll No.', 'Section', 'Contact No.', 'Email', 'Gender', 'Date Of Birth', 'Address', 'Course'))
student_table.heading('id', text='ID')
student_table.heading('Roll No.', text='Roll No.')
student_table.heading('Name', text='Name')
student_table.heading('Class', text='Class')
student_table.heading('Section', text='Section')
student_table.heading('Contact No.', text='Contact No.')
student_table.heading('Email', text='Email')
student_table.heading('Gender', text='Gender')
student_table.heading('Date Of Birth', text='Date Of Birth')
student_table.heading('Address', text='Address')
student_table.heading('Course', text='Course')
student_table['show'] = 'headings'
student_table.column('id', width=20)
student_table.column('Roll No.', width=50)
student_table.column('Name', width=95)
student_table.column('Class', width=95)
student_table.column('Section', width=95)
student_table.column('Contact No.', width=95)
student_table.column('Email', width=95)
student_table.column('Gender', width=95)
student_table.column('Date Of Birth', width=95)
student_table.column('Address', width=95)
student_table.column('Course', width=95)
student_table.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
populate_student_table()

# Add horizontal scrollbar
scrollbar_x = ttk.Scrollbar(frame2, orient=HORIZONTAL, command=student_table.xview)
scrollbar_x.grid(row=1, column=0, sticky="ew")
student_table.configure(xscrollcommand=scrollbar_x.set)

# Configure grid weights
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)
frame1.grid_rowconfigure(0, weight=1)
frame1.grid_columnconfigure(0, weight=1)
frame2.grid_rowconfigure(0, weight=1)
frame2.grid_columnconfigure(0, weight=1)
frame3.grid_columnconfigure(0, weight=1)
frame4.grid_columnconfigure(0, weight=1)

# Run the main loop
root.mainloop()
