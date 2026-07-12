from threading import Thread
import time

m=int(input("Escreva um inteiro: "))

multi_2 = 0
multi_5 = 0

def calcular(x):
    global multi_2, multi_5
    
    if x == 2:
        for i in range(100):
            valor = (m+i)*2
            if valor > multi_2:
                multi_2 = valor
        print("Multiplos de 5: ", multi_5)
    
    else:
        for i in range(100):
            valor = (m+i)*5
            if valor > multi_5:
                multi_5 = valor
        print("Multiplos de 2: ", multi_2)
        
th1 = Thread(target=calcular, args=(5,))
th2 = Thread(target=calcular, args=(2,))

th1.start()
th2.start()

th1.join()
th2.join()

print("FIM")