# Interfaz Principial
from tkinter import *
from Base_de_Datos import datos1
from tkinter import messagebox 
import tkinter.messagebox as tm
global codigodatos
global contraseñadatos

codigodatos = datos1.keys()
contraseñadatos = datos1.values()
 # Crear función ventana 2
 #  def ventana2():

class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_username = Label(self, text="Código",pady=10,padx=20)
        self.label_password = Label(self, text="Contraseña",padx=20)

        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.label_username.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        self.logbtn = Button(self, text=" Iniciar Sesión ", command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2,pady=30)

        self.pack()

    def _login_btn_clicked(self):
        # print("Clicked")
        username = self.entry_username.get()
        password = self.entry_password.get()
        validarcod = username in codigodatos
        # Obteniendo contraseña
        obtaincontra = datos1.get(username)
        
        if validarcod == True and password==obtaincontra:
            # Ventana de Opciones Num1.
            ventana2=Tk()
            ventana2.geometry("550x450+500+250")
            root.destroy()
            botonSalones = Button(ventana2,text="Buscar Salones")
            botonAsesorias = Button(ventana2,text="Buscar Asesorías")
            botonObjPerdidos = Button(ventana2,text="Objetos Perdidos")
            
        else:
            tm.showerror(" Error de Sesión ", " Datos Incorrectos \n Vuelva a ingresar sus datos")
     


root = Tk()
root.title("FreeClassRoom")
root.geometry("350x150+500+250")
root.update_idletasks() 
# Centrar Ventanas

w = root.winfo_screenwidth() 
h = root.winfo_screenheight() 
size = tuple(int(_) for _ in root.geometry().split('+')[0].split('x')) 
x = w/2 - size[0]/2 
y = h/2 - size[1]/2 
root.geometry("%dx%d+%d+%d" % (size + (x, y))) 

# Llamar a las clases
lf = LoginFrame(root)
root.mainloop()

# Obtenemos Usuario




