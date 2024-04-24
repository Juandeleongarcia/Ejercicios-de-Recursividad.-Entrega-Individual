def busqueda_dicotomica_recursiva(tabla, elemento, inicio, fin):
    # Caso base: si el inicio es mayor que el fin, significa que el elemento no está en la tabla
    if inicio > fin:
        return -1
    
    # Calculamos el índice medio
    medio = (inicio + fin) // 2
    
    # Caso base: si el elemento está en la posición media, devolvemos el índice medio
    if tabla[medio] == elemento:
        return medio
    
    # Si el elemento está en la mitad izquierda, hacemos una llamada recursiva en esa mitad
    elif elemento < tabla[medio]:
        return busqueda_dicotomica_recursiva(tabla, elemento, inicio, medio - 1)
    
    # Si el elemento está en la mitad derecha, hacemos una llamada recursiva en esa mitad
    else:
        return busqueda_dicotomica_recursiva(tabla, elemento, medio + 1, fin)

# Solicitar al usuario ingresar una tabla ordenada
tabla_ordenada = []
while True:
    entrada = input("Ingrese un número para la tabla ordenada (o 'fin' para terminar): ")
    if entrada.lower() == 'fin':
        break
    try:
        numero = int(entrada)
        tabla_ordenada.append(numero)
    except ValueError:
        print("Por favor, ingrese solo números.")

# Solicitar al usuario ingresar el elemento a buscar
elemento_buscado = int(input("Ingrese el elemento que desea buscar en la tabla ordenada: "))

# Realizar la búsqueda dicotómica recursiva
indice = busqueda_dicotomica_recursiva(tabla_ordenada, elemento_buscado, 0, len(tabla_ordenada) - 1)

# Mostrar el resultado de la búsqueda
if indice != -1:
    print(f"El elemento {elemento_buscado} está en la posición {indice}.")
else:
    print(f"El elemento {elemento_buscado} no está en la tabla.")
