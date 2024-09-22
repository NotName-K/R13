import json  
import requests 
from pprint import pprint  

def urls(a):
    p = requests.get(a)  
    return json.loads(p.content) 

if __name__ == "__main__":  
    a = 'https://official-joke-api.appspot.com/random_joke'  
    b = 'https://api.agify.io?name=meelad'  
    c = 'https://api.zippopotam.us/us/33162'  
    d = urls(a) 
    e = urls(b)  
    f = urls(c)  
    pprint((a, d))
    pprint((b, e))
    pprint((c, f))  