

# Funcion que Busca salones disponibles

def Buscador(lista,campus,pabellon):
    for elem in lista[campus-1][pabellon-1]:
        print(" - " + str(elem))

# Función para mostrar los pabellones             
def Pabellon():
        global pabellon
        pabellon = int(input("Ingrese el pabellon \n"+
                "1-A \n" +
                "2.-B \n"+
                "3.-C \n"+
                " Ingrese la opción -----> "))
        if(pabellon==1 or pabellon==2 or pabellon==3):
                return pabellon
        else:
                print(" La Opción es Incorrecta")
                return Pabellon()
                
                
