                            # Preguntar al Usuario - Codigo y Contraseña
from Base_de_Datos import datos1

# Verificando Usuario
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
        print(" Bienvenido(a)")