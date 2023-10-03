import numpy as np
import math as m
lista_x = []
lista_S1 = []
lista_S2 = []
lista_Sc = []
lista_k0 = []
lista_Sa = []
lista_Sb = []
lista_k = []
for x in range(0, 110, 10):
    e = 10**(-10)
    Sa = 1.0
    Sb = 1.0
    Sc = 1.0
    Sk = 1.0
    k = 0

    while abs(Sk) >= e:
        k = k+1
        Sk = ((-1)**k)*(x**k)/(m.factorial(k))
        Sa = Sa + Sk
        lista_S1.append(Sa)
        
        lista_k0.append(k)
        
    lista_Sa.append(lista_S1[-1])
    lista_k.append(lista_k0[-1])
    while abs(Sk) >= e:
        k = k+1
        Sk = -Sk*(x/k)
        Sb = Sb+Sk
        lista_S2.append(Sb)
    print(lista_S2)
    
    lista_Sb.append(lista_S2[-1])
        

    e_x = m.exp(x)
    rec_e_x = 1/e_x

    lista_Sc.append(rec_e_x)
    
    lista_x.append(x)

print(lista_x)
print(lista_Sa)
print(lista_Sb)
print(lista_Sc)
print(lista_k)

    


        