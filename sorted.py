dictx = {22:"x", 23:23, 80:24**(1/2)} 
try: 
   k = list(dictx.values()) 
   k.sort() 
   for i in k: 
    print(i) 
except TypeError: 
    print("Error: No todos los valores son del mismo tipo")