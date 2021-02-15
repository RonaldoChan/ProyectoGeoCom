from Tkinter import *


def add():
    lista.insert(END, x.get() + "," + y.get())
    x.focus()
    x.set("ww ")
    y.set('')


root = Tk()
root.title('Geometria computacional')
root.geometry('500x500')

# frame input
frameInput = Frame(root)
frameInput.config(borderwidth=2, relief='solid')
frameInput.pack(ipadx=30, ipady=30, padx=30, pady=30)

# label intupt
text2 = Label(frameInput, text='x')
text2.grid(column=1, row=1)

text2 = Label(frameInput, text='y')
text2.grid(column=2, row=1)
text2 = Label(frameInput, text='Agregar punto')
text2.grid(column=0, row=2)
x = StringVar()
y = StringVar()
xa = Entry(frameInput, width=2, textvariable=x)
xa.grid(column=1, row=2)
ya = Entry(frameInput, width=2, textvariable=y)
ya.grid(column=2, row=2)
boton1 = Button(frameInput, text='Agregar', command=add)
boton1.grid(column=0, row=3)

framePoints = Frame(root)
framePoints.pack()

lista = Listbox(framePoints)
lista.pack()

root.mainloop()
