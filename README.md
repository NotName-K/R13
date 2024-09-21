# R13
Reto 13 Programación
## Algoritmo de impresion organizada de valores
```python
dictx = {22:"x", 23:23, 80:24**(1/2)} # Diccionario con error
try: 
   k = list(dictx.values()) # hacer una lista de todos los valores
   k.sort() # ordena la lista de valores de forma ascendente
   for i in k: # imprime los valores ordenados
    print(i) 
except TypeError: # muestra el error cuando los datos son de distinto tipo
    print("Error: No todos los valores son del mismo tipo")
```
## Diccionario de Diccionarios
```python
def x(a, b): # funcion de diccionario nuevo
    b.update(a) # se añade el diccionario a al diccionario b
    return b # regresa un nuevo diccionario

def listx(): # funcion de primer diccionario
    k = [] # lista vacia
    m = 1  # contador
    while True: # bucle
        # Crear una lista  de 2 elementos
        clave = input(f"Clave {m} del diccionario 1: ")
        if clave == "":  # Si la clave es vacía, romper el bucle
            break
        valor = input(f"Valor {m} del diccionario 1: ")
        m += 1 # se señala el siguiente valor
        
        # Añadir la clave y el valor como una tupla
        k.append((clave, valor))  # Usamos una tupla para cada par clave-valor
    
    # Convertir la lista de tuplas en un diccionario
    a = dict(k)
    return a

def listy(): # funcion de segundo diccionario
    k = [] # nueva lista
    m = 1 # contador
    while True:
        # Crear una lista temporal de 2 elementos
        clave = input(f"Clave {m} del diccionario 2: ")
        if clave == "":  # Si la clave es vacía, romper el ciclo
            break
        valor = input(f"Valor {m} del diccionario 2: ")
        m += 1
        
        # Añadir la clave y el valor como una tupla
        k.append((clave, valor))  # Usamos una tupla para cada par clave-valor
    
    # Convertir la lista de tuplas en un diccionario
    a = dict(k)
    return a

if __name__ == "__main__":
    # Crear dos diccionarios usando las funciones listx y listy
    a = listx()
    b = listy()
    
    # Unir los diccionarios usando la función x y mostrar el resultado
    print(x(a, b))
```

## JSON definido por el usuario
### Deporte dado practicado por estudiante
```python
import json # se importa el modulo

def deporte(a): # funcion buscadora de deportes practicados
 readFile = open('json.json', "r") # abre el json
 d = json.load(readFile) 
 k = d.values() # se separan los valores del json
 e = False # se agrega una bandera

 for i in k: # para todos los valores separados...
  if a in i["deportes"]: # si el deporte esta en la lista de deportes de cada estudiante
   print(f"{i['nombres']} {i['apellidos']}") #se imprime su nombre y apellido
   e = True # la bandera es positiva
 
 if not e: # si no se consigue un estudiante que practique el deporte ingresado....
  print(f"No se encontro quien practique {a}") # se imprime el mensaj

if __name__ == "__main__":
   z = str(input("Ingrese Deporte: "))
   deporte(z)
```
### Estudiante en rango dado de edad
```python
import json # se importa el modulo

def edad(a,b): # funcion buscadora de estudiantes por rango de edad
  readfile = open('json.json', "r")
  d = json.load(readfile)
  l = d.values()
  e = False # se agrega una bandera

  for i in l: # para todos los valores separados...
   if i['edad'] in range(a,b): # si la edad esta en el rango...
     print(f"{i['nombres']} {i['apellidos']}") # se imprimen los nombres
     e = True # la bandera es positiva
 
  if not e: # si no se consigue un estudiante con la edad buscada....
     print(f"No se encontro un estudiante en el rango de edad {a} - {b}") # se imprime el mensaje

if __name__ == "__main__": # datos a ingresar
  a = int(input("Edad Minima: ")) 
  b = int(input("Edad Maxima: "))
  edad(a,b) # se llama a la funcion
```
