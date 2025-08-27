import time
import threading

def Dorme_e_Printa(a:float):
    time.sleep(a)
    print(a)

def sleep_sort(a: float, b:float, c:float):

    MyT1 = threading.Thread(target=Dorme_e_Printa, args=(a,))
    MyT2 = threading.Thread(target=Dorme_e_Printa, args=(b,))
    MyT3 = threading.Thread(target=Dorme_e_Printa, args=(c,))

    MyT1.start()
    MyT2.start()
    MyT3.start()

    MyT1.join()
    MyT2.join()
    MyT3.join()

a = float(input())
b = float(input())
c = float(input())

sleep_sort(a, b, c)
