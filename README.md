# Reto_12
***
Solución de los problemas asignados - Realizado por Lucas García Álvarez

![logo](https://i.ibb.co/440n654/A-adir-un-t-tulo.png)

*Nota*: Para esta actividad se utilizó Python 3.12.5
## Consulta inicial
***
Para la realización de el presente reto, se tuvo que indagar respecto a ciertos métodos de strings en python, los cuales a continuación se definen y ejemplifican para explicitar su funcionalidad.

### Endswith y Startswith
Estos métodos tienen la función de analizar si una cadena de strings termina o inicia, respectivamente, con una subcadena determinada.
- Ejemplo:
```python
string: str = "Jason Vorhees"
print(string.endswith("Vorhees")) # Devuelve un True
print(string.startswith("Vorhees")) # Devuelve un False
# Y viceversa
print(string.endswith("Jason")) # False
print(string.startswith("Jason")) # True
```
Además, este método tiene la siguiente estructura interna:
```python
.ends/startswith(x,a,z)
```
Donde:
- x: Es la subcadena o tupla por comprobar, es obligatorio.
- a: Es el índice desde donde se desea comprobar, es opcional.
- z: Es el índice hasta donde se desea comprobar, es opcional.

### Isalpha, Isalnum, Isdigit e Isspace
***
Estos métodos cumplen con la función de verificar si la cadena de strings deseada solo tiene:
- isalpha(): Letras
- isalnum(): Caracteres alfanuméricos
- isdigit(): Digitos
- isspace(): Espacios en blanco, es decir, una cadena vacía

Ejemplos:
```python
letras: str = "aeipou"
numeros: str = "12345"
maquinaExpendedora: str = "A1"
elAmorDeElla: str = ""

print(letras.isspace()) # Falso
print(numeros.isalnum()) # Verdadero
print(maquinaExpendedora.isdigit()) # Falso
print(elAmorDeElla.isalpha()) # Falso
```
### Istitle, Islower e Isupper
***
Estos métodos verifican, de manera respectiva, si la cadena de strings es un título, es decir, tiene la primera letra de cada palabra en mayúscula; si todas las palabras que lo componen estan en minúscula, o si estan en mayúscula.

Ejemplo:
```python
Obra : str = "La Guerra De Las Galaxias"
Dialogo1: str = "Te amo"
Dialogo2: str = "ya lo sé"
Dialogo3: str = "Luke, yo soy tu padre"
Dialogo4: str = "NOOOOOO"

print(Obra.istitle()) # True
print(Dialogo1.islower()) # False
print(Dialogo2.islower()) # True
print(Dialogo3.isupper()) # False
print(Dialogo4.isupper()) # True
```
## Ejercicio
***
Se pidió procesar un archivo dentro de un programa y que este entregase la cantidad de vocales y consonantes en el texto, además, entregase las 50 palabras más frecuentes en él.

Para esto se crea la función en donde se ingresa el archivo y se convierte a una cadena de string, para así poder sacar las cuentas requeridas, además convierte a mayúsculas todos los elementos para no diferenciar entre mayúsculas y minúsculas, y se elimina todo lo que sea letras y espacios, para luego separar en una lista, a través de los espacios, las palabras y contabilizar las que se repiten más veces, organizandolas de mayor a menor y entregando las primeras 50.
```python
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
```
Esta función llama a las otras dos, las cuales son encargadas de contabilizar la cantidad individual y total de vocales y consonantes, respectivamente.
```python
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
```
Por último se usa la función main y se ejecutan las demás.
```python
if __name__ == "__main__": # Función main para iniciar el código
    # Ruta del archivo de texto plano, ejemplo: C:/Users/Lucas/Documents/Python_Unal_2024-1/Reto_12/mbox.txt
    rutaArchivo = str(input("Ingresa la ruta del archivo a procesar:"))
    # Se llaman a las funciones
    analizarArchivo(rutaArchivo)
```
