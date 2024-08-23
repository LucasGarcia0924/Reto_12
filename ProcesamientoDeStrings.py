def contarVocales(texto: str):
    # Se incializan y declaran variables para comparar las vocales en mayúscula dentro del texto
    vocales : str = "AEIOU"
    acumulado: int = 0
    i : int = 0
    print("Las vocales aparecen en esta cantidad:\n")
    # Para cada vocal se obtiene su frecuencia y se acumula para imprimir el total
    for i in range(len(vocales)):
        vocal = texto.count(vocales[i])
        print(f"{vocales[i]}: {vocal} veces")
        acumulado += vocal
    print(f"\nEn total, dentro del texto aparecen: {acumulado} vocales")

def contarConsonantes(texto: str):
    # Se incializan y declaran variables para comparar las consonantes en mayúscula dentro del texto
    consonantes : str = "BCDFGHJKLMNPQRSTVWXYZ"
    acumulado: int = 0
    j : int = 0
    print("Las consonantes aparecen en esta cantidad:\n")
    # Para cada consonante se obtiene su frecuencia y se acumula para imprimir el total
    for j in range(len(consonantes)):
        consonante: int = texto.count(consonantes[j])
        print(f"{consonantes[j]}: {consonante} veces")
        acumulado += consonante
    print(f"\nEn total, dentro del texto aparecen: {acumulado} consonantes")

def analizarArchivo(rutaArchivo: str):
    # Se declaran e inicializan las variables
    palabras: list = []
    top50Palabras: list = []
    frecuenciaPalabra : dict = {}
    # Se lee el contenido del archivo y se guarda en un string
    with open(rutaArchivo, 'r', encoding='utf-8') as file:
        texto : str = file.read()
    # Se convierte todo el texto a mayúsculas para que no haya diferencia entre las mismas letras en minúsculas
    texto = texto.upper()
    
    # Se llaman a las funciones para contar vocales y consonantes
    contarVocales(texto)
    print("\n")
    contarConsonantes(texto)

    # Se reemplazan caracteres no alfabéticos por espacios
    texto = "".join(carácter if carácter.isalpha() or carácter.isspace() else " " for carácter in texto)
    # Se separa el texto en palabras
    palabras = texto.split()

    # Se Cuenta la frecuencia de cada palabra
    for palabra in palabras:
        if palabra in frecuenciaPalabra:
            frecuenciaPalabra[palabra] += 1
        else:
            frecuenciaPalabra[palabra] = 1

    # Se ordenan las palabras por frecuencia y se obtienen las 50 más comunes
    palabras = sorted(frecuenciaPalabra.items(), key=lambda item: item[1], reverse=True)
    top50Palabras = palabras[:50]

    print("\nListado de las 50 palabras que más se repiten:")
    for palabras, cantidad in top50Palabras:
        print(f"{palabras}: {cantidad} veces")

if __name__ == "__main__": # Función main para iniciar el código
    # Ruta del archivo de texto plano, ejemplo: C:/Users/Lucas/Documents/Python_Unal_2024-1/Reto_12/mbox.txt
    rutaArchivo = str(input("Ingresa la ruta del archivo a procesar:"))
    # Se llaman a las funciones
    analizarArchivo(rutaArchivo)