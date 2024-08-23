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
