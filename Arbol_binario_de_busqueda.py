lista_main = ['D', 'F', 'E', 'B', 'A', 'C', 'G']
lista_in_orden = ['D']
i = 0

def in_orden():
    while True:
        i += 1
        if lista_main[i] > lista_in_orden[0]:
            lista_in_orden.append(lista_main[i])