from tkinter import *
root = Tk()
root.title("backgroundcolor")
root.geometry("150x222")
e1 = Entry(width=15,justify = CENTER)
lal = Label(width=10, height=1, fg='black',justify = CENTER)
def insert1():
    e1.delete(0, END)
    e1.insert(0,"#ff0000")
    lal.config(text='красный')
def insert2():
    e1.delete(0, END)
    e1.insert(0,"#ff7d00")
    lal.config(text='оранжевый')
def insert3():
    e1.delete(0, END)
    e1.insert(0,"#ffff00")
    lal.config(text='желтый')
def insert4():
    e1.delete(0, END)
    e1.insert(0,"#00ff00")
    lal.config(text='зеленый')
def insert5():
    e1.delete(0, END)
    e1.insert(0,"#007dff")
    lal.config(text='голубой')
def insert6():
    e1.delete(0, END)
    e1.insert(0,"#0000ff")
    lal.config(text='синий')
def insert7():
    e1.delete(0, END)
    e1.insert(0,"#7d00ff")
    lal.config(text='фиолетовый')

b1 = Button(bg='#ff0000', width=12, command = insert1)
b2 = Button(bg='#ff7d00', width=12, command = insert2)
b3 = Button(bg='#ffff00', width=12, command = insert3)
b4 = Button(bg='#00ff00', width=12, command = insert4)
b5 = Button(bg='#007dff', width=12, command = insert5)
b6 = Button(bg='#0000ff', width=12, command = insert6)
b7 = Button(bg='#7d00ff', width=12, command = insert7)
lal.pack()
e1.pack()
b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
b6.pack()
b7.pack()

root.mainloop()
