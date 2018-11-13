from Base_de_Datos import *

                                                # Función Principal


def Todo():
        hora_actual= datetime.now()
        hora_actual = time(hora_actual.hour, hora_actual.minute, hora_actual.second)
        print("Hora de Ingreso:"+str(hora_actual))
        print("                         INICIAR SESIÓN" )           
        codigo = input(" Ingrese su código de Estudiante-----> ").strip()
        validar = codigo in datos1
        while(validar==False):
                codigo = input(" Ingrese su código de Estudiante------> ").strip()
                validar = codigo in datos1
        else:
                obtain = datos1.get(codigo)
                contraseña = input(" Ingrese su contraseña------> ").strip()
                while(obtain!=contraseña):
                        contraseña = input(" Ingrese su contraseña-------> ").strip()
                else:
                        ListadeOpciones(cursos,cursos_disp1,cursos_disp2,cursos_disp3)


                                                # Función Media


def ListadeOpciones(cursos,cursos_disp1,cursos_disp2,cursos_disp3):
        try:
                print("\n -------------------- Bienvenido(a) a FreeClassRoom ----------------------- \n")
                opcion = input(" \n ¿ Qué desea hacer ? \n\n"+
                "1.-Buscar salones Disponibles \n" +
                "2.-Buscar Asesorías Disponibles \n"+
                "3.-Reportar objetos encontrados y/o Revisar objetos perdidos \n"+
                "4.-Salir \n"+
                " Ingrese la opción----->")
                if(opcion=="1"):
                        Buscarsalones()
                        # Asesorías Disponibles
                elif(opcion=="2"):
                        Asesorias()
                elif(opcion=="3"):
                        Objetos()
                elif(opcion=="4"):
                        Salir()
                else:
                        print("\n <<<<<<  La opción es Incorrecta  >>>>> \n")  
                        ListadeOpciones(cursos,cursos_disp1,cursos_disp2,cursos_disp3)  
        except(ValueError):
                print("\n <<<<<<  La opción es Incorrecta  >>>>> \n")  
                ListadeOpciones(cursos,cursos_disp1,cursos_disp2,cursos_disp3) 


                                                # Funciones Cola


# Función para Buscar Salones
def Buscarsalones():
        try:
                campus = int(input("  \n En qué campus desea buscar salones \n" +
                        "1.-Campus 1 \n"+
                        "2.-Campus 2 \n"+
                        "3.-Campus 7\n"+
                        "4.-Volver al Menú \n"+
                        "5.-Salir \n"+
                        " Ingrese la opción  ----->"))

                if(campus==1):
                        tiempo()
                        sincronizar(h1,hora_inicio1,hora_finalizacion1)
                        sincronizar(h2,hora_inicio2,hora_finalizacion2)
                        sincronizar(h3,hora_inicio3,hora_finalizacion3)
                        sincronizar(h4,hora_inicio4,hora_finalizacion4)
                        sincronizar(h5,hora_inicio5,hora_finalizacion5)
                        sincronizar(h6,hora_inicio6,hora_finalizacion6)
                        sincronizar(h7,hora_inicio7,hora_finalizacion7)
                        sincronizar(h8,hora_inicio8,hora_finalizacion8)
                        Regresar()
                                        
                elif(campus == 2):
                        tiempo()
                        sincronizar(h11,hora_inicio1,hora_finalizacion1)
                        sincronizar(h22,hora_inicio2,hora_finalizacion2)
                        sincronizar(h33,hora_inicio3,hora_finalizacion3)
                        sincronizar(h44,hora_inicio4,hora_finalizacion4)
                        sincronizar(h55,hora_inicio5,hora_finalizacion5)
                        sincronizar(h66,hora_inicio6,hora_finalizacion6)
                        sincronizar(h77,hora_inicio7,hora_finalizacion7)
                        sincronizar(h88,hora_inicio8,hora_finalizacion8)
                        Regresar()

                elif(campus == 3):
                        tiempo()
                        sincronizar(h111,hora_inicio1,hora_finalizacion1)
                        sincronizar(h222,hora_inicio2,hora_finalizacion2)
                        sincronizar(h333,hora_inicio3,hora_finalizacion3)
                        sincronizar(h444,hora_inicio4,hora_finalizacion4)
                        sincronizar(h555,hora_inicio5,hora_finalizacion5)
                        sincronizar(h666,hora_inicio6,hora_finalizacion6)
                        sincronizar(h777,hora_inicio7,hora_finalizacion7)
                        sincronizar(h888,hora_inicio8,hora_finalizacion8)
                        Regresar()

                elif(campus==4):
                        ListadeOpciones(cursos,cursos_disp1,cursos_disp2,cursos_disp3)
                elif(campus==5):
                        Salir()
                else:
                        print(" \n <<<<<<  La opción es Incorrecta  >>>>> \n ")
                        Buscarsalones()
        except(ValueError):
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
        try:
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
        except(IndexError,ValueError):
                print("\n  <<<<<<< Opción Incorrecta  >>>>>>>")
                Asesorias()

# Funcion Buscar Objetos Perdidos


def Objetos():
        try:
                print(" \n ------- Objetos Perdidos: -------\n")
                p=int(input("1.-Reportar objeto encontrado \n"+
                "2.-Ver objetos reportados \n"+
                "3.-Regresar \n "
                + "Ingrese la opción ----->"))
                if(p==1):
                        f = open('objetos.txt','a')
                        p=str(input(" \n Tipo de objeto encontrado: ")).strip()
                        print("<<<< Especifique: >>>>>")
                        q=str(input("- Color: \n ")).strip()
                        r=str(input("- Marca: \n ")).strip()
                        f.writelines('\n' + " **** "+p+" ****" +'\n'+ "- Color: " + q + '\n'+ "- Marca: "+r)
                        f.close()
                        Regresar()

                elif(p==2):
                        f = open('objetos.txt','r')
                        mensaje = f.read()
                        print(mensaje)
                        f.close
                        Regresar()
                elif(p==3):
                        ListadeOpciones(cursos,cursos_disp1,cursos_disp2,cursos_disp3)
        except(ValueError):
                print(" \n <<<<<<<<< Opción Incorrecta >>>>>>>> ")
                Objetos()
                
        
        

                                        # Funciones de Soporte


# Función para regresar al Menú Principal

def Regresar():
        try:
                volver = int(input(" \n Desea regresar al Menú principal \n 1.-Si \n 2.-No \n Ingrese la opción----->"))
                if(volver == 1):
                        return ListadeOpciones(cursos,cursos_disp1,cursos_disp2,cursos_disp3)
                elif(volver==2):
                        print("\n ***********************Agradecemos su visita********************** ")
                elif(volver!=1 or volver!=2):
                        print("\n  <<<<<<< Opción Incorrecta  >>>>>>>")
                        Regresar()
        except(ValueError):
                print("\n  <<<<<<< Opción Incorrecta  >>>>>>>")
                Regresar()
# Función para salir de la Aplicación
def Salir():
        print("\n ***************** Gracias por su Visita ***************** ")

# Funcion que Busca salones disponibles indexada a (Funcion Buscarsalones)

def Buscador(lista,campus,pabellon):
    for elem in lista[campus-1][pabellon-1]:
        print(" - " + str(elem))

# Función para obtener pabellon  indexada a (Funcion Buscarsalones)           
def Pabellon():
        try:
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
        except(ValueError):
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


# Código Reducido de Luis

def sincronizar(lista,hora_inicio,hora_fin):
    actual = datetime.now()
    actual = time(actual.hour, actual.minute,actual.second)  # este objeto se puede comparar sin tener en cuenta la fecha
    for i in lista:
        if actual > hora_inicio and actual < hora_fin:
            print(" - "+str(i))
        else:
            break

def tiempo():
    hora_actual= datetime.now()
    hora_actual = time(hora_actual.hour, hora_actual.minute, hora_actual.second)
    print(" \n -------------------- La Hora Actual es: ------------------ ")
    print("                          "+"|"+str(hora_actual)+"|")
    print("  \n * * * * * *  Lista de salones libres a ésta hora(por pabellones):  * * * * * * * \n")