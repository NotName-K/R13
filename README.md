# R13
[Reto 13](https://github.com/fegonzalez7/pdc_unal_clase18?tab=readme-ov-file#reto-13/) Programación
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
## Pronostico del clima
```python
import json # se importa el modulo compatible con json
from datetime import datetime # se importa el modulo para pasar de Fecha en UTC a Fecha Calendario
from pprint import pprint

# json de pronosticos
jsonString = '''
{\"dt\": {\"0\": 1685116800, \"1\": 1685203200, \"2\": 1685289600, \"3\": 1685376000, \"4\": 1685462400, \"5\": 1685548800, \"6\": 1685635200, \"7\": 1685721600}, \"sunrise\": {\"0\": 1685097348, \"1\": 1685183745, \"2\": 1685270143, \"3\": 1685356542, \"4\": 1685442942, \"5\": 1685529342, \"6\": 1685615743, \"7\": 1685702145}, \"sunset\": {\"0\": 1685143042, \"1\": 1685229458, \"2\": 1685315875, \"3\": 1685402291, \"4\": 1685488708, \"5\": 1685575124, \"6\": 1685661541, \"7\": 1685747958}, \"moonrise\": {\"0\": 1685118300, \"1\": 1685207460, \"2\": 1685296620, \"3\": 1685385720, \"4\": 1685474880, \"5\": 1685564220, \"6\": 1685653740, \"7\": 1685743500}, \"moonset\": {\"0\": 0, \"1\": 1685164320, \"2\": 1685253000, \"3\": 1685341560, \"4\": 1685430120, \"5\": 1685518740, \"6\": 1685607600, \"7\": 1685696640}, \"moon_phase\": {\"0\": 0.22, \"1\": 0.25, \"2\": 0.28, \"3\": 0.31, \"4\": 0.35, \"5\": 0.38, \"6\": 0.41, \"7\": 0.45}, \"pressure\": {\"0\": 1011, \"1\": 1012, \"2\": 1012, \"3\": 1012, \"4\": 1012, \"5\": 1012, \"6\": 1012, \"7\": 1011}, \"humidity\": {\"0\": 85, \"1\": 61, \"2\": 68, \"3\": 74, \"4\": 84, \"5\": 66, \"6\": 81, \"7\": 82}, \"dew_point\": {\"0\": 23.93, \"1\": 22.5, \"2\": 23.67, \"3\": 23.35, \"4\": 24.22, \"5\": 22.73, \"6\": 23.18, \"7\": 22.93}, \"velViento\": {\"0\": 3.56, \"1\": 5.07, \"2\": 5.38, \"3\": 3.95, \"4\": 4.74, \"5\": 3.75, \"6\": 4.08, \"7\": 5.94}, \"dirViento\": {\"0\": 188, \"1\": 14, \"2\": 21, \"3\": 23, \"4\": 40, \"5\": 330, \"6\": 176, \"7\": 168}, \"wind_gust\": {\"0\": 6.47, \"1\": 8.86, \"2\": 8.95, \"3\": 6.12, \"4\": 7.17, \"5\": 5.4, \"6\": 5.13, \"7\": 9.67}, \"weather\": {\"0\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"1\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"2\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"3\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"4\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"5\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"6\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"7\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}]}, \"clouds\": {\"0\": 100, \"1\": 82, \"2\": 99, \"3\": 100, \"4\": 100, \"5\": 59, \"6\": 100, \"7\": 100}, \"pop\": {\"0\": 1.0, \"1\": 0.65, \"2\": 0.98, \"3\": 0.86, \"4\": 1.0, \"5\": 0.62, \"6\": 0.93, \"7\": 0.95}, \"prcp\": {\"0\": 40.0, \"1\": 1.65, \"2\": 14.01, \"3\": 5.07, \"4\": 16.55, \"5\": 2.17, \"6\": 2.77, \"7\": 1.73}, \"uvi\": {\"0\": 10.14, \"1\": 12.78, \"2\": 12.73, \"3\": 8.44, \"4\": 0.59, \"5\": 1.0, \"6\": 1.0, \"7\": 1.0}, \"temp.day\": {\"0\": 26.62, \"1\": 30.95, \"2\": 30.17, \"3\": 28.37, \"4\": 27.22, \"5\": 29.78, \"6\": 26.83, \"7\": 26.36}, \"tmpMin\": {\"0\": 25.64, \"1\": 24.64, \"2\": 25.84, \"3\": 25.56, \"4\": 25.72, \"5\": 24.86, \"6\": 25.96, \"7\": 25.47}, \"tmpMax\": {\"0\": 27.16, \"1\": 31.1, \"2\": 30.2, \"3\": 29.5, \"4\": 28.87, \"5\": 29.78, \"6\": 28.96, \"7\": 28.25}, \"temp.night\": {\"0\": 25.67, \"1\": 27.39, \"2\": 26.24, \"3\": 27.2, \"4\": 25.92, \"5\": 27.14, \"6\": 26.56, \"7\": 25.66}, \"temp.eve\": {\"0\": 25.91, \"1\": 28.73, \"2\": 27.42, \"3\": 28.27, \"4\": 27.94, \"5\": 29.29, \"6\": 28.96, \"7\": 28.12}, \"temp.morn\": {\"0\": 26.5, \"1\": 24.64, \"2\": 26.13, \"3\": 25.72, \"4\": 26.04, \"5\": 24.86, \"6\": 25.98, \"7\": 25.57}, \"feels_like.day\": {\"0\": 26.62, \"1\": 34.99, \"2\": 34.96, \"3\": 32.03, \"4\": 30.67, \"5\": 33.62, \"6\": 29.45, \"7\": 26.36}, \"feels_like.night\": {\"0\": 26.56, \"1\": 30.98, \"2\": 26.24, \"3\": 30.62, \"4\": 26.84, \"5\": 30.16, \"6\": 26.56, \"7\": 26.45}, \"feels_like.eve\": {\"0\": 26.85, \"1\": 32.49, \"2\": 30.94, \"3\": 31.8, \"4\": 31.51, \"5\": 33.17, \"6\": 32.64, \"7\": 31.18}, \"feels_like.morn\": {\"0\": 26.5, \"1\": 25.48, \"2\": 26.13, \"3\": 26.62, \"4\": 26.04, \"5\": 25.73, \"6\": 25.98, \"7\": 26.4}, \"date\": {\"0\": 1685098800000, \"1\": 1685185200000, \"2\": 1685271600000, \"3\": 1685358000000, \"4\": 1685444400000, \"5\": 1685530800000, \"6\": 1685617200000, \"7\": 1685703600000}, \"main\": {\"0\": \"Rain\", \"1\": \"Rain\", \"2\": \"Rain\", \"3\": \"Rain\", \"4\": \"Rain\", \"5\": \"Rain\", \"6\": \"Rain\", \"7\": \"Rain\"}, \"description\": {\"0\": \"lluvia moderada\", \"1\": \"lluvia ligera\", \"2\": \"lluvia moderada\", \"3\": \"lluvia ligera\", \"4\": \"lluvia moderada\", \"5\": \"lluvia ligera\", \"6\": \"lluvia ligera\", \"7\": \"lluvia ligera\"}, \"icono\": {\"0\": \"10d\", \"1\": \"10d\", \"2\": \"10d\", \"3\": \"10d\", \"4\": \"10d\", \"5\": \"10d\", \"6\": \"10d\", \"7\": \"10d\"}, \"alertPrecip\": {\"0\": \"X\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertAlertas\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertVelViento\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"X\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMax\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"X\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMin\": {\"0\": \"-\", \"1\": \"X\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"recomendaciones\": {\"lluvias\": \"Realice una revisi\\u00f3n y limpieza a la red de desague y canales existentes ENTER8 Cuente con una estaci\\u00f3n de bombeo, que debe estar ubicada en el punto m\\u00e1s bajo del predio. Aseg\\u00farese de encender y probar el sistema de bombeo al menos una vez al mes y hacer un mantenimiento mensual al equipo de bombeoENTER8 Los productos alojados en zonas de almacenamiento deben mantenersen sobre estibas - estanterias, con el fin de que no entren en contacto directo con el agua.\", \"vientos\": \"-\", \"temperatura\": \"-\"}}
'''
data = json.loads(jsonString) # se carga el json
l = ['alertAlertas', 'alertPrecip', 'alertTmpMax', 'alertTmpMin', 'alertVelViento'] # Lista de Alertas
m = ['tmpMin', 'temp.night', 'temp.morn', 'feels_like.night', 'feels_like.morn'] # Lista de Variables asociadas de cada alerta
n = ['tmpMax', 'temp.day', 'temp.eve', 'feels_like.day', 'feels_like.eve']
o = ['pop', 'prcp', 'clouds', 'weather', 'description']
p = ['velViento', 'wind_gust', 'dirViento']
k = [] # lista vacia para almacenar los datos solicitados

for i in l: # para cada campo de alerta ...
        for _ in data[i]: # para cada dia ...
            if data[i].get(_) == "X":  # si ese dia tiene una alerta ...
                k.append([_,i])  # se agrega el dia y el campo de alerta a la lista vacia

# Bucle para la lista de parametros relevantes de lluvia
for i in o: # para cada varibale 
    k[0].append((i, data[i].get("0")))

# Bucle para la lista de parametros relevantes de temperatura maxima
for i in n:
    k[1].append((i, data[i].get("5")))

# Bucle para la lista de parametros relevantes de temperatura minima
for i in m:
    k[2].append((i, data[i].get("1")))

# Bucle para la lista de parametros relevantes de Viento
for i in p:
    k[3].append((i, data[i].get("2")))

for i in k: # para cada elemento en lista de datos ...
  k[k.index(i)][0] = data['dt'].get(k[k.index(i)][0]) # transformacion de dato de dia a fecha en UTC 
  k[k.index(i)][0] = datetime.fromtimestamp(k[k.index(i)][0]).strftime('%Y-%m-%d') # Tansformacion de fecha UTC a Fecha de Calendario

def mn(a): # funcion de orden de fechas
    return a[0]

k.sort(key=mn) # se ordena la lista por fecha 

for i in k: # se imprime la lista de fecha, alerta y sus variables respectivas
     pprint(tuple(i))
    
```
## Extraccion de API´s
```python
import json  # Importa el módulo para trabajar con datos JSON
import requests  # Importa el módulo para hacer solicitudes HTTP
from pprint import pprint  # Importa pprint para imprimir de forma legible

def urls(a):
    # Esta función toma una URL como argumento
    p = requests.get(a)  # Realiza una solicitud GET a la URL
    return json.loads(p.content)  # Convierte el contenido de la respuesta JSON a un diccionario de Python y lo retorna

if __name__ == "__main__":  # Este bloque se ejecuta solo si el script es ejecutado directamente
    a = 'https://official-joke-api.appspot.com/random_joke'  # URL para obtener un chiste aleatorio
    b = 'https://api.agify.io?name=meelad'  # URL para predecir la edad de la persona con el nombre "meelad"
    c = 'https://api.zippopotam.us/us/33162'  # URL para obtener información sobre el código postal 33162
    d = urls(a)  # Llama a la función urls con la primera URL y almacena el resultado en 'd'
    e = urls(b)  # Llama a la función urls con la segunda URL y almacena el resultado en 'e'
    f = urls(c)  # Llama a la función urls con la tercera URL y almacena el resultado en 'f'
    # Imprime la URL 'a' junto con el resultado de 'd' de forma legible
    pprint((a, d))
    # Imprime la URL 'b' junto con el resultado de 'e' de forma legible
    pprint((b, e))
    # Imprime la URL 'c' junto con el resultado de 'e' de forma legible (esto es probablemente un error, debería ser 'f')
    pprint((c, f))  # Esto debería ser 'f' para imprimir la respuesta de la URL 'c'
```
