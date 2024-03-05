from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3

root =Tk()

root.maxsize(width=1520, height=900)
root.minsize(width=1520, height=900)
root.title("Student Management System")
root.iconbitmap("building.ico")
root.config(bg='lightblue')


# Function to create a database table if it doesn't exist
def create_table():
    conn = sqlite3.connect('login_info.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS admins
             (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    conn.commit()
    conn.close()

# Function to add user credentials to the database
def add_user(username, password):
    conn = sqlite3.connect('login_info.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

# Function to check if the entered username and password are valid
def authenticate(username, password):
    # Check if the provided credentials match the administrator credentials
    if username == "admin" and password == "admin":
        return True
    else:
        return False



 #photo
image_background=ImageTk.PhotoImage(Image.open('login.jpg'))
label=Label(root,image=image_background)
label.place(x=0,y=0,width=1520,height=800)




#frame
frame = LabelFrame(root,relief='raised',bg='lightblue')
frame.place(x=900, y=110,width=450, height=580) 


#heading
login=Label(frame,text='Login',bg='lightblue', font=("times new roman",24,"bold"))
login.place(x=190,y=20)



#label, place for the details
user_name=Label(frame,text='Username:',bg='lightblue', font=("times new roman",16,"bold"))
user_name.place(x=70,y=170)
Password=Label(frame,text='Password:',bg='lightblue', font=("times new roman",16,"bold"))
Password.place(x=70, y=260)



#entry of other details
entry_name=Entry(frame,width=50)
entry_name.place(x=70,y=210)         #for name
entry_password=Entry(frame, width=50,show='')       #show='' is used first when user type anything it shows  asterick(*) after clicking on the button only it shows password
entry_password.place(x=70, y=300)       #for password







#to show and not to show password
def add():
    if CheckVar1.get()==1:
        entry_password.config(show="")
    else:
        entry_password.config(show="*")
    
CheckVar1=IntVar()
c1 = Checkbutton(frame, text="Show password", bg='lightblue',variable=CheckVar1, onvalue=1, offvalue=0, command=add)
c1.place(x=70, y=330)


def back_to_registration():
    root.destroy()
    import register


back_button = Button(frame, text="Back", fg='lightblue', bg='Royal Blue', relief='raised',
                     font=("times new roman", 15, "bold"), command=back_to_registration)
back_button.place(x=180, y=500)

    
def home():
    username = entry_name.get()
    password = entry_password.get()

    if entry_name.get() == '' or entry_password.get() == '':
        messagebox.showerror('Error!', 'Please fill up all the required details.')
    else:
        if authenticate(username, password):  # Using authenticate function here
            messagebox.showinfo('Success', 'Successfully logged in!')
            root.destroy()
            import homepage
        else:
            messagebox.showerror('Error', 'Invalid username or password')

    

login=Button(frame,text="LOGIN",fg='lightblue', bg='Royal Blue',relief='raised', font=("times new roman",15,"bold"),command=home)
login.place(x=180, y=450)




# forget password?
# #to destroy the login and go to forget password
# def forget():
#     root.destroy()
#     import forget_password


# for_pass=Button(frame,text="Forget Passoword?",relief='raised',command=forget)
# for_pass.place(x=280, y=360)





# #sign up
# #to destroy the login and go to sign up
# def sign():
#     root.destroy()
#     import sign_up


# label_sign=Label(frame,text="Don't have an account?",bg='lightblue')
# label_sign.place(x=120,y=520)


# sign_up=Button(frame,text="Sign up",relief='raised',command=sign)
# sign_up.place(x=260, y=520)


root.mainloop()