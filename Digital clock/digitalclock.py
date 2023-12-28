from tkinter import *
import time

# function to update time
def update_time():
    current_time = time.strftime('%H:%M:%S %p')
    clock_label.config(text=current_time)
    clock_label.after(200, update_time)

# creating tkinter window
window = Tk()
window.title('Digital Clock')

# creating a label widget
clock_label = Label(window, font=('calibri', 40), bg='white')
clock_label.pack(anchor='center')

# start updating time
update_time()

# starting tkinter main loop
window.mainloop()