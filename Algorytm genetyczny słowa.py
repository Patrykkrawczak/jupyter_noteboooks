#!/usr/bin/env python
# coding: utf-8

# In[21]:


import numpy as np
import random
import string
from IPython.display import clear_output
class osobnik:
    def get_przys(self):
        return self.przystosowanie
    def __init__(self,napis):
        self.napis = []
        for i in range(len(napis)):
            self.napis.append(random.choice(string.printable))
        self.przystosowanie = self.przystosowaniev2(napis)
    def przystosowaniev2(self,napis):
        wynik = 0
        for i,j in zip(self.napis,napis):
            if i == j:
                wynik = wynik + 1 
        return wynik
    def krzyzuj(self,drugi,napis):
        o1 = osobnik(napis)
        o2 = osobnik(napis)
        dlugosc = len(napis)
        xd = str(napis) + str(self.napis)
        dzielnik =  random.randint(1,10)
        if random.random() < 0.0001 :
            o1.napis = [random.choice(xd) for i in range(dlugosc)]
            o2.napis = [random.choice(xd) for i in range(dlugosc)]
        else:
            o1.napis = self.napis[0:int(len(napis)/dzielnik)]+drugi.napis[int(len(napis)/dzielnik):int(len(napis))]
            o2.napis = drugi.napis[0:int(len(napis)/dzielnik)]+self.napis[int(len(napis)/dzielnik):int(len(napis))]
        o1.przystosowanie = o1.przystosowaniev2(napis)
        o2.przystosowanie = o2.przystosowaniev2(napis)
        
        return o1,o2
    def mutuj(self):
        for i in range(len(napis)):
            if random.random() < 0.001:
                self.napis[i] = random.choice(string.printable)
    def __str__(self):
        return str(self.napis)
        
napis = input()
lista = [osobnik(napis) for x in range( 1000)]

for num in range(50000): 
    ile = [i.przystosowanie for i in lista]
    ile = sum(ile)
    pula_losujaca = [i.przystosowanie/ile for i in lista]


    lista2 = []
    # licznik = 0
    # for s in pula_losujaca:
    #     licznik += int(100*s)
    for i,s in zip(lista,pula_losujaca):
        lista2 += [i]*int((500 )*s )
        i.mutuj()
        i.przystosowanie = i.przystosowaniev2(napis)
        lista2 += [i]*int((500 )*s )

    listauzup = [osobnik(napis) for x in range(1000-len(lista2))]
    lista3 = []
    for i in range(50):
        index1 = random.randint(0,len(lista2)-1)
        index2 = random.randint(0,len(lista2)-1)

        osobnik1, osobnik2 = lista2[index1].krzyzuj(lista2[index2],napis)
        lista3.append(osobnik1)
        lista3.append(osobnik1)
    lista = lista3
    lista.sort(reverse=True,key=lambda x: x.przystosowanie)

    if num % 100 :
        clear_output()
        print(("\r"+''.join(lista[0].napis)),end = "")
        
    if list(napis) == lista[0].napis:
        print("nauczyłem się po " + str(num) + " iteracjach")
        break

    
print("PO NAUCE")
for o in lista:
    print(''.join(o.napis))


# In[ ]:





# In[ ]:




