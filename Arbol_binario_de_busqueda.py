lista_main = ['D', 'F', 'E', 'B', 'A', 'C', 'G']
lista_in_orden = ['D']
i = 0

# Función que ordena (in-orden) los valores del array
def in_orden():
    while True:
        i += 1
        if lista_main[i] > lista_in_orden[0]:
            lista_in_orden.append(lista_main[i])



# El usuario decide ingresar valores o ver el arbol ordenado
while True:
    opcion = input("¿Desea ingresar valores o ver el arbol? (INGRESAR / VER)  ").lower()
    if opcion == 'ver':
        # Impresión del árbol
        print("El Árbol ordenado queda asi: ")
        in_orden()
    elif opcion == 'ingresar':
        #ingresa valores al arbol
        print("\nIngrese los valores a agregar (si desea dejar de agregar valores, escriba CHAU): ")
        valores = input().upper
        while valores != 'CHAU':
            lista_main.append(valores)
            print("Perfecto, ingrese un nuevo valor")
    else:
        print("Palabra incorrecta, escriba bien")