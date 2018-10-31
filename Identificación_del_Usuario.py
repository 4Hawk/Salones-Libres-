                            # Preguntar al Usuario - Codigo y Contraseña
from Base_de_Datos import datos1
from Base_de_Datos import salones
from Base_de_Datos import cursos_disp1
from Base_de_Datos import cursos_disp2
from Base_de_Datos import cursos_disp7

from Funciones import Buscador


                # Verificación del Usuario
           
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
        print(" Bienvenido(a) a FreeClassRoom")

        # Creando la Lista de Opciones
        opcion = int(input(" ¿ Qué desea hacer ? \n"+
        "1-Buscar salones Disponibles \n" +
        "2.-Buscar Asesorías Disponibles \n"+
        "3.-Reportar o Revisar objetos perdidos \n"+
        " Ingrese la opción requerida -----> "))

        if(opcion==1):
            campus = int(input(" En qué campus desea buscar salones \n" +
            "1.-Campus 1 \n"+
            "2.-Campus 2 \n"+
            "3.-Campus 7\n"+
            " Ingrese la opción -----> "))

            # Observación: Aquí podemos quitar las opciones multiples y usar solamente la función(No si se desean hacerlo)
            if(campus==1):
                pabellon=int(input("Ingrese el pabellon \n"+
                "1-A \n" +
                "2.-B \n"+
                "3.-C \n"+
                " Ingrese la opción -----> "))
                print("Los salones disponibles son:")
                Buscador(salones,campus,pabellon)

            if(campus == 2):
                pabellon = int(input("Ingrese el pabellon \n"+
                "1-A \n" +
                "2.-B \n"+
                "3.-C \n"+
                " Ingrese la opción -----> "))
                print("Los salones disponibles son:")
                Buscador(salones,campus,pabellon)

            if(campus == 3):
                pabellon = int(input("Ingrese el pabellon \n"+
                "1-A \n" +
                "2.-B \n"+
                "3.-C \n"+
                " Ingrese la opción -----> "))
                print("Los salones disponibles son:")
                Buscador(salones,campus,pabellon)


        elif(opcion==2):
            curso=input("Que curso desea reforzar ?   ")
            validbusque = curso in cursos_disp1
            if(validbusque == True):
                print("Curso disponible solo en: Campus 1 ")
            validbusque = curso in cursos_disp2
            if(validbusque == True):
                print("Curso disponible solo en: Campus 2 ")     
            validbusque = curso in cursos_disp7
            if(validbusque == True ):
                print("Curso disponible solo en: Campus 7 ")
            else:
                print("Curso no disponible por el momento")

            

      