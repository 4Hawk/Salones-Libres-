# Interfaz Principial

from tkinter import *
from tkinter import ttk

ventana = Tk()
ventana.geometry('650x450')
ventana.title("FreeClassRoom")
ventana.configure(bg = 'white')

ttk.Button(ventana,text='Salir',command=quit).pack(side=BOTTOM)
ventana.mainloop()