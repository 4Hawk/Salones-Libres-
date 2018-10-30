
# Funcion que Busca salones disponibles

def Buscador(lista,campus,pabellon):
    for elem in lista[campus-1][pabellon-1]:
        print(" - " + str(elem))


