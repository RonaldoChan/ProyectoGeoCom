from Tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.pyplot import text


def donothing():

    filewin = Toplevel(root)
    filewin.title('Triangulacion de Voronoi')
    # frame input
    frameInput = Frame(filewin)
    frameInput.config(borderwidth=2, relief='solid')
    frameInput.pack(ipadx=30, ipady=30, padx=30, pady=30)

    # label intupt
    text2 = Label(frameInput, text='x')
    text2.grid(column=1, row=1)
    text2 = Label(frameInput, text='y')
    text2.grid(column=2, row=1)
    text2 = Label(frameInput, text='Agregar punto')
    text2.grid(column=0, row=2)
    x = Entry(frameInput, width=2)
    x.grid(column=1, row=2)
    y = Entry(frameInput, width=2)
    y.grid(column=2, row=2)
    boton1 = Button(frameInput, text='Agregar',)
    boton1.grid(column=0, row=3)

    # frame viewData
    frameData = Frame(filewin)
    frameData.config(borderwidth=2, relief='solid', height=200, width=200)
    frameData.pack()
    label1 = Label(frameData, text="Puntos", font=("Arial Bold", 20))
    label1.pack()

    def callback():
        label1.insert(END, 'hh')


def donothing1():
    rootGrafico = Toplevel(root)
    rootGrafico.title('Grafico de Voronoi')

    frameInput = Frame(rootGrafico)
    frameInput.config(borderwidth=2, relief='solid')
    frameInput.pack(ipadx=30, ipady=30, padx=30, pady=30)
    text1 = Label(rootGrafico, text='Grafico')
    text1.pack()

    frameOutput = Frame(rootGrafico)
    frameOutput.config(borderwidth=2, relief='solid')
    frameInput.pack(ipadx=30, ipady=30, padx=30, pady=30)


root = Tk()
root.title('Geometria computacional')
root.geometry('500x500')
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Voronoi", menu=filemenu)
filemenu.add_command(label="Agregar Puntos", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Graficar", command=donothing1)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Delaunay", menu=editmenu)
editmenu.add_command(label="Agregar Puntos", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Graficar", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Exit", command=root.quit)


root.config(menu=menubar)
root.mainloop()
