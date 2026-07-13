import threading
import time
from concurrent.futures import ThreadPoolExecutor

m=int(input("Escreva um inteiro: "))

z = 0
def calcular(x):
    global z
    for i in range(100):
        z +=(i+m)*x 
    print(f"o maior múltiplo de {x} calculado a partir de {m} é: {z}")
        
executor = ThreadPoolExecutor(max_workers=2)
executor.submit(calcular(2, ))
executor.submit(calcular(5, ))



