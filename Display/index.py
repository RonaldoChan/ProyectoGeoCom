from tkinter import ttk
from tkinter import *
import sqlite3
from plotDelaunay import Plot


class Product:

    # connection dir property
    db_name = '/Users/ronaldochan23/DocumentosR/Universidad/geocom/proyecto final/Display/database.db'

    def __init__(self, window):
        # Initializations
        self.wind = window
        self.wind.title('Transformacion de Imagenes 2D a 3D')

        # Creating a Frame Container
        frame = LabelFrame(self.wind, text='Ingresar Puntos')
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        # Name Input
        Label(frame, text='Punto X: ').grid(row=1, column=0)
        self.x = Entry(frame)
        self.x.focus()
        self.x.grid(row=1, column=1)

        # Price Input
        Label(frame, text='Punto Y: ').grid(row=2, column=0)
        self.y = Entry(frame)
        self.y.grid(row=2, column=1)

        # Button Add Product
        ttk.Button(frame, text='Agregar punto', command=self.add_product).grid(
            row=3, columnspan=2, sticky=W + E)

        # Output Messages
        self.message = Label(text='', fg='red')
        self.message.grid(row=3, column=0, columnspan=2, sticky=W + E)

        # Table
        self.tree = ttk.Treeview(height=10, columns=2)
        self.tree.grid(row=4, column=0, columnspan=2)
        self.tree.heading('#0', text='X', anchor=CENTER)
        self.tree.heading('#1', text='Y', anchor=CENTER)

        ttk.Button(text='Borar', command=self.getPlot).grid(
            row=5, column=0, sticky=W + E)
        ttk.Button(text='Editar', command=self.edit_product).grid(
            row=5, column=1, sticky=W + E)

        # Filling the Rows
        self.get_products()

    def getPlot(self):
        Plot()

    # Function to Execute Database Querys
    def run_query(self, query, parameters=()):

        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        result = cursor.execute(query, parameters)
        conn.commit()
        return result

    # Get Products from Database
    def get_products(self):

        # cleaning Table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # getting data
        query = 'SELECT * FROM points'
        db_rows = self.run_query(query)

        # filling data
        for row in db_rows:
            self.tree.insert('', 0, text=row[1], values=row[2])
            print(self.tree)
        print(db_rows)

        # Validation
    def validation(self):
        return len(self.x.get()) != 0 and len(self.y.get()) != 0

    def add_product(self):
        if self.validation():
            query = 'INSERT INTO points VALUES(NULL, ?, ?)'
            parameters = (self.x.get(), self.y.get())
            self.run_query(query, parameters)
            self.message['text'] = 'El punto ({},{}) fue agregado correctamente'.format(
                self.x.get(), self.y.get())
            self.x.delete(0, END)
            self.y.delete(0, END)
        else:
            self.message['text'] = 'El valor X es requerido'
        self.get_products()

    def delete_product(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Seleccione un campo'
            return
        self.message['text'] = ''
        x = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM points WHERE x = ?'
        self.run_query(query, (x, ))
        self.message['text'] = 'Borrado correctamente'
        self.get_products()

    def edit_product(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['text'] = 'Seleccione el punto para editar'
            return
        x = self.tree.item(self.tree.selection())['text']
        actualY = self.tree.item(self.tree.selection())['values'][0]
        self.edit_wind = Toplevel()
        self.edit_wind.title = 'Editar punto'
        # Old Name
        Label(self.edit_wind, text='X:').grid(row=0, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind,
                                                     value=x), state='readonly').grid(row=0, column=2)
        # New Name
        Label(self.edit_wind, text='Nuevo X:').grid(row=1, column=1)
        nuevoX = Entry(self.edit_wind)
        nuevoX.grid(row=1, column=2)

        # Old Price
        Label(self.edit_wind, text='Y:').grid(row=2, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind,
                                                     value=actualY), state='readonly').grid(row=2, column=2)
        # New Price
        Label(self.edit_wind, text='Nuevo Y:').grid(row=3, column=1)
        nuevoY = Entry(self.edit_wind)
        nuevoY.grid(row=3, column=2)

        Button(self.edit_wind, text='Actualizar', command=lambda: self.edit_records(
            nuevoX.get(), x, nuevoY.get(), actualY)).grid(row=4, column=2, sticky=W)
        self.edit_wind.mainloop()

    def edit_records(self, nuevoX, x, nuevoY, actualY):
        query = 'UPDATE points SET x = ?, y = ? WHERE x = ? AND y = ?'
        parameters = (nuevoX, nuevoY, x, actualY)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.message['text'] = 'El punto {} fue actualizado correctamente'.format(
            x)
        self.get_products()

    def getX(self):
        print('guardar los elementos de X en un arreglos')

    def getY(self):
        print('guardar los elementos de Y en un arreglos')


if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()
