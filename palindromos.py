import unicodedata

def filtrar_caracteres(texto):
    # Filtrar caracteres alfanuméricos y convertir a minúsculas
    texto_filtrado = ''.join(c.lower() for c in texto if c.isalnum())
    return texto_filtrado

def quitar_acentos(texto):
    # Sustituir caracteres acentuados por sus equivalentes sin acento
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')

def es_palindromo(texto):
    # Filtrar y quitar acentos
    texto_filtrado = filtrar_caracteres(texto)
    texto_sin_acentos = quitar_acentos(texto_filtrado)
    
    # Verificar si el texto filtrado es igual a su imagen reflejada
    return texto_sin_acentos == texto_sin_acentos[::-1]

# Ejemplos
frases = [
    "Dábale arroz a la zorra el abad",
    "Logré ver gol",
    "Salas",
    "1754571",
    "10000000000000000001",
    "Oso"
]

for frase in frases:
    if es_palindromo(frase):
        print(f'La frase "{frase}" es un palíndromo.')
    else:
        print(f'La frase "{frase}" no es un palíndromo.')

# Solicitar una frase al usuario
frase_usuario = input("Ingrese una frase para comprobar si es un palíndromo: ")
if es_palindromo(frase_usuario):
    print(f'La frase "{frase_usuario}" es un palíndromo.')
else:
    print(f'La frase "{frase_usuario}" no es un palíndromo.')