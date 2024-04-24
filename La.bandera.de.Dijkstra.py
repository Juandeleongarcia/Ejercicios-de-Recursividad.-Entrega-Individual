def ordenar_fichas_de_colores(fichas):
    # Inicializar los índices para las fichas rojas, verdes y azules
    indice_rojo = 0
    indice_verde = 0
    indice_azul = len(fichas) - 1
    
    while indice_verde <= indice_azul:
        if fichas[indice_verde] == 'R':
            # Intercambiar la ficha verde con la roja
            fichas[indice_rojo], fichas[indice_verde] = fichas[indice_verde], fichas[indice_rojo]
            indice_rojo += 1
            indice_verde += 1
        elif fichas[indice_verde] == 'V':
            # La ficha verde ya está en su lugar correcto, solo incrementamos el índice
            indice_verde += 1
        else:
            # Intercambiar la ficha verde con la azul
            fichas[indice_verde], fichas[indice_azul] = fichas[indice_azul], fichas[indice_verde]
            indice_azul -= 1
    
    return fichas

# Ejemplo de uso
fichas = ['B', 'R', 'V', 'R', 'B', 'V', 'B', 'R', 'V', 'R', 'V', 'R', 'B']
fichas_ordenadas = ordenar_fichas_de_colores(fichas)
print("Fichas ordenadas:", fichas_ordenadas)
