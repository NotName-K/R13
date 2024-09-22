import json 

def deporte(a): 
 readFile = open('json.json', "r") 
 d = json.load(readFile) 
 k = d.values() 
 e = False 

 for i in k: 
  if a in i["deportes"]: 
   print(f"{i['nombres']} {i['apellidos']}") 
   e = True 
 
 if not e:
  print(f"No se encontro quien practique {a}") 

if __name__ == "__main__":
   z = str(input("Ingrese Deporte: "))
   deporte(z)