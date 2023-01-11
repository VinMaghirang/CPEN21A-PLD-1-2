#Add widgets to create a UI application progress

from tkinter import *
window = Tk()
window.geometry("300x200+10+20")

window.title("Vin's first python GUI")

#add label widget
lbl = Label(window,text="My first UI Python program",fg="red",font=("Merriweather,10"))
lbl.place(x=30,y=70)

#add text field
txtfld=Entry(window,text = "This is Barbie",bd =5)
txtfld.place(x=70,y=100)

#add button widget
btn = Button(window,text = "Submit", bg="Purple")
btn.place(x=110,y=130)

def sel():
    selection ="You selected the option"+str(var.get())
    label.config(text=selection)
var = IntVar()
r1 = Radiobutton(window,text="Male",variable=var,value=1,command=sel)
r1.pack(anchor=W)

r2 = Radiobutton(window,text="Female",variable=var,value=2,command=sel)
r2.pack(anchor=W)

label = Label(window)
label.pack()
window.mainloop()