import tkinter

FONT = ('Courier',20,'normal')
COLOR = '#e3f0f5'
TEXT_COLOR = 'white'
ENTRY_FONT = ('Helvetica',18)
km = 0

window = tkinter.Tk()
window.title('Transform Miles to Kilometers.')
window.minsize(width = 450, height= 150)
window.configure(bg=COLOR)
# Add padding to the entire window
main_frame = tkinter.Frame(window)
main_frame.grid(row=0, column=0)



# input
entry = tkinter.Entry(width=10,font = ENTRY_FONT)
entry.grid(column=1, row = 0)

#Label
label = tkinter.Label(text = 'miles', font = FONT)
label.grid(column= 2, row = 0)
label.configure(bg=COLOR)

def clicked_button():
    input = float(entry.get())
    km = input * 1.60934
    label_km.config(text=f'{km:.2f}')


label = tkinter.Label(text = 'is equal to ', font = FONT)
label.grid(column= 0, row = 1)
label.configure(bg=COLOR)

label_km = tkinter.Label(text = f'{km}', font = FONT)
label_km.grid(column= 1, row = 1)
label_km.configure(bg=COLOR)

label = tkinter.Label(text = 'Km.', font = FONT)
label.grid(column= 2, row = 1)
label.configure(bg=COLOR)


# Button
button = tkinter.Button(text='Calculate',font= ('Time New Romans',17), command=clicked_button,fg=TEXT_COLOR)
button.grid(column = 1, row = 2)
button.configure(bg='#044d69')

window.mainloop()