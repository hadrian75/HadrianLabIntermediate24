sayur = "selada"
buah = "apel"

def swapVar(a, b):
    global sayur
    global buah
    
    buah = a 
    sayur = b
    

swapVar(sayur, buah)

print(buah, sayur)