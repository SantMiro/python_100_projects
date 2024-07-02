from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from day5_password_generator import password_generator
import pyperclip

# -------------------------------------------RESIZE IMAGE ------------------------------------#
original_image = Image.open('day29_password_manager/lock.png')
resized_image = original_image.resize((250, 250), Image.LANCZOS)

# -------------------------------------------SAVE DATA ------------------------------------#
def save_data():
    web = entry_web.get()
    email = entry_email.get()
    password = entry_pass.get()
    proceed = False
    
    if not web or not password or not email:
        messagebox.showerror(title='Oops!',message='Please do not leave any information empty.')
    else:
        proceed = messagebox.askokcancel(title=web, message=f'This is the provided information:\nEmail: {email}\nPassword: {password}\n Is it okay to save?')
    
    if proceed:
        with open('day29_password_manager/data.txt','a') as data:
            data.write(f'{web} | {email} | {password}\n')
        entry_web.delete(0,END)
        entry_pass.delete(0,END)

# -------------------------------------------RANDOMLY GENERATE PASSWORD ------------------------------------#

def generate_password():
    entry_pass.delete(0,END)
    password = password_generator()
    pyperclip.copy(password)
    entry_pass.insert(0,f'{password}')



# -------------------------------------------UI DESIGN ------------------------------------#
WHITE = '#EBF4F6'
LIGHT_BLUE = '#37B7C3'
BLUE = '#088395'
DARK_BLUE = '#071952'

LABEL_FONT = ('Helvetica',16,'normal')
WIDTH_ENTRIES = 20

# WINDOW
window = Tk()
window.title('Password Manager')
window.config(padx=20,pady=20,bg=WHITE)


# CANVAS
canvas = Canvas(width=250,height=250, bg=WHITE)
lock_img = ImageTk.PhotoImage(resized_image)
window.lock_img = lock_img
canvas.create_image(125,125,image= lock_img)
canvas.grid(column=1,row=0)

# LABELS
label_web = Label(text='Website: ', font=LABEL_FONT, bg=WHITE)
label_web.grid(column=0, row=1)

label_email = Label(text='Email/Username: ', font=LABEL_FONT, bg=WHITE)
label_email.grid(column=0,row=2)

label_password = Label(text='Password: ', font=LABEL_FONT, bg=WHITE)
label_password.grid(column=0,row=3)

# ENTRIES
entry_web = Entry(width=WIDTH_ENTRIES * 2,font=LABEL_FONT)
entry_web.grid(column=1,row=1,columnspan=2,padx=0,pady=10)
entry_web.focus()

entry_email = Entry(width=WIDTH_ENTRIES * 2,font=LABEL_FONT)
entry_email.grid(column=1,row=2,columnspan=2,pady=10)
entry_email.insert(END,'mirot.santiago@gmail.com')

entry_pass = Entry(width=WIDTH_ENTRIES,font=LABEL_FONT)
entry_pass.grid(column=1,row=3,pady=10)

# BUTTONS
button_password = Button(text='Generate Password',font=LABEL_FONT, bg=BLUE, fg=WHITE,command=generate_password)
button_password.grid(column=2,row=3,pady=10)

button_add = Button(text='Add', width=36, font=LABEL_FONT, bg=BLUE, fg=WHITE, command=save_data)
button_add.grid(column=1, row=4, columnspan=2,pady=10)



window.mainloop()