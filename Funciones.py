from tkinter import messagebox 

# Funcion que Busca salones disponibles

def Buscador(lista,campus,pabellon):
    for elem in lista[campus-1][pabellon-1]:
        print(" - " + str(elem))

# Funcion para lOGEAR
def Verificar(Datos,codigo,password):
    obtcodigo = codigo.get()
    validarcod= obtcodigo in Datos
    obtpassword=password.get()
    obtainPassword = Datos.get(obtcodigo)
    if(validarcod==True and obtainPassword==obtpassword):
        messagebox.showwarning(title="Bienvenido",message="Genial")                
    