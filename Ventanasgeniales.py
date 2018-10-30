# Interfaz Principial
from tkinter import *
from Base_de_Datos import datos1
from tkinter import messagebox 
from Funciones import Verificar



# Ventana Principal

ventana = Tk()
ventana.geometry('400x300')
ventana.title("FreeClassRoom")
ventana.config(bg = 'white')

# Frame
miframe = Frame(ventana,width=400,height=300,bg="white")
miframe.pack()

                # Labels
codigotxt = Label(miframe,text="Código:",bg="white") #Creamos el texto codigo
passwordtxt = Label(miframe,text="Contraseña:",bg="white")
codigotxt.grid(row=0,column=1,padx=20,pady=20)
passwordtxt.grid(row=1,column=1,padx=20,pady=10)

                # Entradas
Codigoinsert = Entry(miframe) #Creamos la entrada codigo
Passwordinsert =Entry(miframe)
Codigoinsert.grid(row=0,column=2)
Passwordinsert.grid(row=1,column=2)
Passwordinsert.config(show="*") #Oculta la escritura del password



                # Botones 

ingresar = Button(ventana,text="Ingresar",command= Verificar(datos1,Codigoinsert,Passwordinsert))
ingresar.pack()

ventana.mainloop()

# Obtenemos Usuario


