                            # Preguntar al Usuario - Codigo y Contraseña
from Base_de_Datos import datos1

                # Verificación del Usuario
codigo = int(input(" Ingrese su código de Estudiante-----> "))
validar = codigo in datos1
while(validar==False):
    codigo = int(input(" Ingrese su código de Estudiante------> "))
    validar = codigo in datos1
else:
    obtain = datos1.get(codigo)
    contraseña = input(" Ingrese su contraseña------> ") 
    while(obtain!=contraseña):
        contraseña = input(" Ingrese su contraseña-------> ") 
    else:
        print(" Bienvenido(a) a FreeClassRoom")
        # Creando la Lista de Opciones
        opcion = int(input(" Ingrese una Opción \n"+
        "1.-Buscar salones Disponibles \n" +
        "2.-Buscar Asesorías Disponibles \n"+
        "3.-Reportar o Revisar objetos perdidos \n"))
        if(opcion==1):
            campus = input(" En qué campus desea buscar salones")
      