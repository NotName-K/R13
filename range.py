import json 

def edad(a,b): 
  readfile = open('json.json', "r")
  d = json.load(readfile)
  l = d.values()
  e = False 

  for i in l:
   if i['edad'] in range(a,b): 
     print(f"{i['nombres']} {i['apellidos']}") 
     e = True 
 
  if not e: 
     print(f"No se encontro un estudiante en el rango de edad {a} - {b}")

if __name__ == "__main__": 
  a = int(input("Edad Minima: ")) 
  b = int(input("Edad Maxima: "))
  edad(a,b) 