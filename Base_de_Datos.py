from datetime import datetime
from datetime import time

                                    # Base de Datos para Identificación del Usuario
 
datos1 = {"1811854":"JavierIn34","17035465":"MariaRojas123","16042341":"Peru123",
"13094354":"Usiperu","15051243":"easy","17114354":"password","11112222":"estudiante","12":"12"}



                                    
                                     #  Base de Datos de los Salones Disponibles
                                     


         # Horario 1
hora_inicio1 = time(7,0,0)         # siete de la mañana
hora_finalizacion1 = time(9,0,0)   # nueve de la mañana
h1 =["A307","B406","D302"]         # Campus 1
h11 =["A307","B406","D302"]        # Campus 2
h111 =["A307","B406","D302"]       # Campus 7

         # Horario 2
hora_inicio2 = time(9,0,0)        # nueve de la mañana
hora_finalizacion2 = time(11,0,0) # once de la mañana
h2 =["A107","B406","D102"]        # Campus 1
h22 =["A707","B506","A302"]       # Campus 2
h222 =["A307","B406","D302"]      # Campus 7

       # Horario 3
hora_inicio3 = time(11,0,0)        # once de la mañana
hora_finalizacion3 = time(13,0,0)  # una de la tarde
h3 =["A306","B206","D301"]        # Campus 1
h33 =["B307","C406","D303"]       # Campus 2
h333 =["A307","A406","D102"]      # Campus 7

       # Horario 4
hora_inicio4 = time(13,0,0)        # una de la tarde
hora_finalizacion4 = time(15,0,0)  # tres de la tarde
h4 =["B107","C806","D702"]        # Campus 1
h44 =["A107","B506","D502"]       # Campus 2
h444=["B307","B106","D102"]      # Campus 7

       # Horario 5
hora_inicio5 = time(15,0,0)         # tres de la tarde
hora_finalizacion5 = time(17,0,0)   # cinco de la tarde
h5 =["B303","B506B","D102"]        # Campus 1
h55 =["A407","C306","D202"]        # Campus 2
h555 =["B507","B206","D102"]       # Campus 7

      # Horario 6
hora_inicio6 = time(17,0,0)        # cinco de la tarde
hora_finalizacion6 = time(19,0,0)  # siete de la noche
h6 =["A304","C405","C302"]        # Campus 1
h66 =["B307","B406","A302"]       # Campus 2
h666 =["C303","B406","D302"]      # Campus 7

     # Horario 7
hora_inicio7 = time(19,0,0)        # siete de la noche
hora_finalizacion7 = time(21,0,0)  # nueve de la noche
h7 =["C207","B106","D302"]        # Campus 1
h77 =["B308","B203","C102"]       # Campus 2
h777 =["A107","B506","C301"]      # Campus 7

     # Horario 8
hora_inicio8 = time(21,0,0)        # nueve de la noche
hora_finalizacion8 = time(23,0,0)  # once de la noche
h8 =["A103","C404","D102"]        # Campus 1
h88 =["A205","B106","C305"]       # Campus 2
h888 =["B507","B403","C102"]      # Campus 7

def sincronizar1():
    actual = datetime.now()
    actual = time(actual.hour, actual.minute,actual.second)  # este objeto se puede comparar sin tener en cuenta la fecha
    for i in h1:
        if actual > hora_inicio1 and actual < hora_finalizacion1:
            print(i)
        else:
            break

def sincronizar11():
    actual = datetime.now()
    actual = time(actual.hour, actual.minute,actual.second)  # este objeto se puede comparar sin tener en cuenta la fecha
    for i in h11:
        if actual > hora_inicio1 and actual < hora_finalizacion1:
            print(i)
        else:
            break

def sincronizar111():
    actual = datetime.now()
    actual = time(actual.hour, actual.minute,actual.second)  # este objeto se puede comparar sin tener en cuenta la fecha
    for i in h111:
        if actual > hora_inicio1 and actual < hora_finalizacion1:
            print(i)
        else:
            break

def sincronizar2():
    actual = datetime.now()
    actual = time(actual.hour, actual.minute,actual.second)  # este objeto se puede comparar sin tener en cuenta la fecha
    for i in h2:
        if actual > hora_inicio2 and actual < hora_finalizacion2:
            print(i)
        else:
            break

def sincronizar22():
    actual = datetime.now()
    actual = time(actual.hour, actual.minute,actual.second)  # este objeto se puede comparar sin tener en cuenta la fecha
    for i in h22:
        if actual > hora_inicio2 and actual < hora_finalizacion2:
            print(i)
        else:
            break

def sincronizar222():
    actual = datetime.now()
    actual = time(actual.hour, actual.minute,actual.second)  # este objeto se puede comparar sin tener en cuenta la fecha
    for i in h222:
        if actual > hora_inicio2 and actual < hora_finalizacion2:
            print(i)
        else:
            break

def sincronizar3():
    actual = datetime.now()
    actual = time(actual.hour, actual.minute,actual.second)  # este objeto se puede comparar sin tener en cuenta la fecha
    for i in h3:
        if actual > hora_inicio3 and actual < hora_finalizacion3:
            print(i)
        else:
            break

def sincronizar33():
    actual = datetime.now()
    actual = time(actual.hour, actual.minute,actual.second)  # este objeto se puede comparar sin tener en cuenta la fecha
    for i in h33:
        if actual > hora_inicio3 and actual < hora_finalizacion3:
            print(i)
        else:
            break

def sincronizar333():
    actual = datetime.now()
    actual = time(actual.hour, actual.minute,actual.second)  # este objeto se puede comparar sin tener en cuenta la fecha
    for i in h333:
        if actual > hora_inicio3 and actual < hora_finalizacion3:
            print(i)
        else:
            break

def sincronizar4():
    actual = datetime.now()
    actual = time(actual.hour, actual.minute,actual.second)  # este objeto se puede comparar sin tener en cuenta la fecha
    for i in h4:
        if actual > hora_inicio4 and actual < hora_finalizacion4:
            print(i)
        else:
            break

def sincronizar44():
    actual = datetime.now()
    actual = time(actual.hour, actual.minute,actual.second)  # este objeto se puede comparar sin tener en cuenta la fecha
    for i in h44:
        if actual > hora_inicio4 and actual < hora_finalizacion4:
            print(i)
        else:
            break
def sincronizar444():
    actual = datetime.now()
    actual = time(actual.hour, actual.minute,actual.second)  # este objeto se puede comparar sin tener en cuenta la fecha
    for i in h444:
        if actual > hora_inicio4 and actual < hora_finalizacion4:
            print(i)
        else:
            break

def sincronizar5():
    actual = datetime.now()
    actual = time(actual.hour, actual.minute,actual.second)  # este objeto se puede comparar sin tener en cuenta la fecha
    for i in h5:
        if actual > hora_inicio5 and actual < hora_finalizacion5:
            print(i)
        else:
            break

def sincronizar55():
    actual = datetime.now()
    actual = time(actual.hour, actual.minute,actual.second)  # este objeto se puede comparar sin tener en cuenta la fecha
    for i in h55:
        if actual > hora_inicio5 and actual < hora_finalizacion5:
            print(i)
        else:
            break

def sincronizar555():
    actual = datetime.now()
    actual = time(actual.hour, actual.minute,actual.second)  # este objeto se puede comparar sin tener en cuenta la fecha
    for i in h555:
        if actual > hora_inicio5 and actual < hora_finalizacion5:
            print(i)
        else:
            break

def sincronizar6():
    actual = datetime.now()
    actual = time(actual.hour, actual.minute,actual.second)  # este objeto se puede comparar sin tener en cuenta la fecha
    for i in h6:
        if actual > hora_inicio6 and actual < hora_finalizacion6:
            print(i)
        else:
            break

def sincronizar66():
    actual = datetime.now()
    actual = time(actual.hour, actual.minute,actual.second)  # este objeto se puede comparar sin tener en cuenta la fecha
    for i in h66:
        if actual > hora_inicio6 and actual < hora_finalizacion6:
            print(i)
        else:
            break

def sincronizar666():
    actual = datetime.now()
    actual = time(actual.hour, actual.minute,actual.second)  # este objeto se puede comparar sin tener en cuenta la fecha
    for i in h666:
        if actual > hora_inicio6 and actual < hora_finalizacion6:
            print(i)
        else:
            break


def sincronizar7():
    actual = datetime.now()
    actual = time(actual.hour, actual.minute,actual.second)  # este objeto se puede comparar sin tener en cuenta la fecha
    for i in h7:
        if actual > hora_inicio7 and actual < hora_finalizacion7:
            print(i)
        else:
            break

def sincronizar77():
    actual = datetime.now()
    actual = time(actual.hour, actual.minute,actual.second)  # este objeto se puede comparar sin tener en cuenta la fecha
    for i in h77:
        if actual > hora_inicio7 and actual < hora_finalizacion7:
            print(i)
        else:
            break

def sincronizar777():
    actual = datetime.now()
    actual = time(actual.hour, actual.minute,actual.second)  # este objeto se puede comparar sin tener en cuenta la fecha
    for i in h777:
        if actual > hora_inicio7 and actual < hora_finalizacion7:
            print(i)
        else:
            break

def sincronizar8():
    actual = datetime.now()
    actual = time(actual.hour, actual.minute,actual.second)  # este objeto se puede comparar sin tener en cuenta la fecha
    for i in h8:
        if actual > hora_inicio8 and actual < hora_finalizacion8:
            print(i)
        else:
            break

def sincronizar88():
    actual = datetime.now()
    actual = time(actual.hour, actual.minute,actual.second)  # este objeto se puede comparar sin tener en cuenta la fecha
    for i in h88:
        if actual > hora_inicio8 and actual < hora_finalizacion8:
            print(i)
        else:
            break

def sincronizar888():
    actual = datetime.now()
    actual = time(actual.hour, actual.minute,actual.second)  # este objeto se puede comparar sin tener en cuenta la fecha
    for i in h888:
        if actual > hora_inicio8 and actual < hora_finalizacion8:
            print(i)
        else:
            break

def tiempo():
    hora_actual= datetime.now()
    hora_actual = time(hora_actual.hour, hora_actual.minute, hora_actual.second)
    print("son las: ")
    print(hora_actual)
    print("Lista de salones libres a ésta hora por pabellones: ")




                                                             
                                    # Base de Datos de Asesorías Disponibles

#Campus1
cursos_disp1={}
cursos_disp1["Lenguaje"]=["  Juan Carlos Perez  ",["  -C1A205 (2.00 pm)  ","  -C1B304 (9.00 am)  "]]
cursos_disp1["Fisica"]=["  Jean Pedro Vasquez  ",["-C1A505 (3.15 pm)","-C1E304 (10.00 am)"]]
cursos_disp1["Matematica 1"]=["  Mario Pardo  ",["  -C1B305 (4.00 pm)  ","  -C1C504 (6.00pm)  "]]
cursos_disp1["Cálculo 1"]=["  Sir Isaac Carhuancho  ",["  -C1C315 (2.30 pm)  ","  -C1A204 (4.15 pm)  "]]

#Campus2
cursos_disp2={}
cursos_disp2["Estadistica"]=["  John Carmona Perez  ",["  -C2I205 (2.00 pm)  ","  -C2T304 (9.00 am)  "]]
cursos_disp2["Inglés"]=["  Joaquin Piero Vasquez  ",["  -C2W505 (3.15 pm)  ","  -C2U304 (10.00 am)  "]]
cursos_disp2["Calculo de Varias Variables"]=["  Jacob Bernoulli Pardo  ",["  -C2T305 (4.00 pm)  ","  -C2H504 (6.00pm)  "]]
cursos_disp2["Fisica II"]=["  Leyla Crisanto Merino ",["  -C2T315 (2.30 pm)  ","  -C2Y204 (4.15 pm)  "]]

#Campus3
cursos_disp3={}
cursos_disp3["Estadistica"]=["  Juan Carlos Perez Avogadro  ",["  -C3Y205 (2.00 pm)  ","  -C3H304 (9.00 am)  "]]
cursos_disp3["Autocad"]=["  Jean Pedro Vasquez Tongo",["  -C3B505 (3.15 pm)","  -C3R304 (10.00 am)"]]
cursos_disp3["Calculo de Varias Variables"]=["  Paolo Riemman Guevara ",["  -C3F305 (4.00 pm)","  -C3G504 (6.00pm)"]]
cursos_disp3["Leyes"]=["  Sir Isaac Carhuancho",["  -C3A315 (2.30 pm)","  -C3B204 (4.15 pm)"]]

cursos=[cursos_disp1,cursos_disp2,cursos_disp3]



    

