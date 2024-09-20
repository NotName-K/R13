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
