def x(a, b): 
    b.update(a)
    return b 

def listx(): 
    k = [] 
    m = 1  
    while True: 
        clave = input(f"Clave {m} del diccionario 1: ")
        if clave == "":  
            break
        valor = input(f"Valor {m} del diccionario 1: ")
        m += 1 
        k.append((clave, valor))
    a = dict(k)
    return a

def listy(): 
    k = [] 
    m = 1 
    while True:
        clave = input(f"Clave {m} del diccionario 2: ")
        if clave == "":
            break
        valor = input(f"Valor {m} del diccionario 2: ")
        m += 1
        k.append((clave, valor))
    a = dict(k)
    return a

if __name__ == "__main__":
    a = listx()
    b = listy()
    print(x(a, b))