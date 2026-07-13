import random
import threading
from concurrent.futures import ThreadPoolExecutor
import time

def tabuada(nome, x):
    
    for i in range(1, 11):
        z = x * i
        print(f"{nome}, {x}*{i}={z}") 
    z="\nA thread "+ nome + "terminou\n";
    print(z)
    
# tabuada("T1H", 2)
executor = ThreadPoolExecutor(max_workers=4)
executor.submit(tabuada("T1H", 2))
executor.submit(tabuada("T2H", 3))
executor.submit(tabuada("T3H", 4))
executor.submit(tabuada("T4H", 5))


print("FIM")



"""x1 = threading.Thread(target=tabuada, args=("T1H", 2))
x2 = threading.Thread(target=tabuada, args=("T2H", 3))
x3 = threading.Thread(target=tabuada, args=("T3H", 4))
x4 = threading.Thread(target=tabuada, args=("T4H", 5))

x1.start()
x2.start()
x3.start()
x4.start()

x1.join()
x2.join()
x3.join()
x4.join()"""