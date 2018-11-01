from Base_de_Datos import *



                                                # Función Principal


def Todo():
        print("                     INICIAR SESIÓN" )           
        codigo = input(" Ingrese su código de Estudiante-----> ")
        validar = codigo in datos1
        while(validar==False):
                codigo = input(" Ingrese su código de Estudiante------> ")
                validar = codigo in datos1
        else:
                obtain = datos1.get(codigo)
                contraseña = input(" Ingrese su contraseña------> ") 
                while(obtain!=contraseña):
                        contraseña = input(" Ingrese su contraseña-------> ") 
                else:
                        ListadeOpciones(salones,cursos,cursos_disp1,cursos_disp2,cursos_disp3)


                                                # Función Media


def ListadeOpciones(salones,cursos,cursos_disp1,cursos_disp2,cursos_disp3):
        print("\n -------------------- Bienvenido(a) a FreeClassRoom ----------------------- \n")
        opcion = int(input(" \n ¿ Qué desea hacer ? \n\n"+
        "1-Buscar salones Disponibles \n" +
        "2.-Buscar Asesorías Disponibles \n"+
        "3.-Reportar o Revisar objetos perdidos \n"+
        "4.-Salir \n"+
        " Ingrese la opción----->"))
        if(opcion==1):
                Buscarsalones()
                # Asesorías Disponibles
        elif(opcion==2):
                Asesorias()
        elif(opcion==3):
                Objetos()
        elif(opcion==4):
                Salir()
        else:
                print("\n <<<<<<  La opción es Incorrecta  >>>>> \n")  
                ListadeOpciones(salones,cursos,cursos_disp1,cursos_disp2,cursos_disp3)  


                                                # Funciones Cola


# Función para Buscar Salones
def Buscarsalones():
        campus = int(input("  \n En qué campus desea buscar salones \n" +
                "1.-Campus 1 \n"+
                "2.-Campus 2 \n"+
                "3.-Campus 7\n"+
                "4.-Volver al Menú \n"+
                "5.-Salir \n"+
                " Ingrese la opción  ----->"))

        if(campus==1):
                pabellon = Pabellon()
                print("\n Los salones disponibles son:")
                Buscador(salones,campus,pabellon)
                Regresar()
                                
        elif(campus == 2):
                pabellon = Pabellon()
                print("\n Los salones disponibles son:")
                Buscador(salones,campus,pabellon)
                Regresar()

        elif(campus == 3):
                pabellon = Pabellon()
                print("\n Los salones disponibles son:")
                Buscador(salones,campus,pabellon)
                Regresar()
        elif(campus==4):
                ListadeOpciones(salones,cursos,cursos_disp1,cursos_disp2,cursos_disp3)
        elif(campus==5):
                Salir()
        else:
                print(" \n <<<<<<  La opción es Incorrecta  >>>>> \n ")
                Buscarsalones()

# Función para Buscar Asesorías
def Asesorias():
        cursosid = []
        print("\n  ------ Cursos Disponibles ----- \n")
        contador=1
        for elem in cursos:
                lista = elem.keys()
                for i in lista:
                        cursosid.append(i)
                        print(str(contador)+".- " + i)
                        contador+=1
                # Validación de la Búsqueda
        reforzar = int(input(" \n ¿ Qué curso desea reforzar ? ------->"))
        valor=cursosid[reforzar-1]
        validarcursoreforzar = valor in cursosid
        while(validarcursoreforzar==False):
                reforzar = input(" \n <<< La opción que puso no existe >>>  \n ¿Qué curso desea a reforzar? ------->")
                valor=cursosid[reforzar-1]
                validarcursoreforzar = valor in cursosid
        else:
                validbusque = valor in cursos_disp1
                if(validbusque==True):
                        BuscadorCampus(valor,cursos_disp1)
                        Regresar()
                else:
                        validbusque = valor in cursos_disp2
                        if(validbusque==True):
                                BuscadorCampus(valor,cursos_disp2)
                                Regresar()
                        else:
                                BuscadorCampus(valor,cursos_disp3)
                                Regresar()

# Funcion Buscar Objetos Perdidos

def Objetos():
        
        # Aqui copia y pega tu parte Luis Fernando

                                        # Funciones de Soporte


# Función para regresar al Menú Principal

def Regresar():
        volver = int(input(" \n Desea regresar al Menú principal \n 1.-Si \n 2.-No \n Ingrese la opción----->"))
        if(volver == 1):
                return ListadeOpciones(salones,cursos,cursos_disp1,cursos_disp2,cursos_disp3)
        else:
                print("\n ***********************Agradecemos su visita********************** ")

# Función para salir de la Aplicación
def Salir():
        print("\n ***************** Gracias por su Visita ***************** ")

# Funcion que Busca salones disponibles indexada a (Funcion Buscarsalones)

def Buscador(lista,campus,pabellon):
    for elem in lista[campus-1][pabellon-1]:
        print(" - " + str(elem))

# Función para obtener pabellon  indexada a (Funcion Buscarsalones)           
def Pabellon():
        global pabellon
        pabellon = int(input(" \n Ingrese el pabellon \n\n"+
                "1-A \n" +
                "2.-B \n"+
                "3.-C \n"+
                " Ingrese la opción -----> "))
        if(pabellon==1 or pabellon==2 or pabellon==3):
                return pabellon
        else:
                print("\n <<<<<<  La opción es Incorrecta  >>>>> \n")
                return Pabellon()
                
# Funcion Buscar Cursos Campus indexada a (Funcion Buscarsalones)

def BuscadorCampus(curso,lista):
    a = lista.get(curso)
    profesor = a[0]
    print("\n  **** Profesor: ****")
    print(profesor)
    Horarios =a[1]
    print("\n  **** Horarios: ****")
    for e in Horarios:
        print(e)                


