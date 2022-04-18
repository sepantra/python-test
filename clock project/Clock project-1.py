from time import strftime
from tkinter import Label, Tk

window = Tk()
window.title('Display')
window.geometry('200x100')
window.configure(bg='purple')
window.resizable(False, False)

clock_label = Label(window, bg= "purple", fg="white", font=("Time", 30, 'bold'), relief= "raised")
clock_label.place(x=20, y=20)

def update_label():
    current_time = strftime('%H:%M:%S')
    clock_label.configure(text = current_time)
    clock_label.after(1000, update_label)
    
update_label()
window.mainloop()