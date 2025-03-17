from tkinter import*
from tkinter . ttk import*
from time import strftime

top=Tk()
top. title ("Digital Clock")
def none():
     text=strftime(' %H:%M: %S: %P')
                ibl.config(text=text)
                   ibl.after(1000,none)
ibl=lable(top,font=(" digital-7 , 50,bold)
                     background='black', forefrond'red')
ibl.pack(anchor='center')
none()
mainloop()
