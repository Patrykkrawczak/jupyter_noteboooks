#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np
import random
class osobnik:
    def __init__(self):
        self.napis = []
        
        for i in range(8):
            if random.random() >= 1/2:
                self.napis.append(1)
            else:
                self.napis.append(0)
                
        self.przystosowanie = self.przystosowanie()
    def przystosowanie(self):
        self.przystosowanie = sum(self.napis)
        return self.przystosowanie
    def krzyzuj(self,drugi):
        o1 = osobnik()
        o2 = osobnik()
        o1.napis = self.napis[0:4]+drugi.napis[4:8]
        o2.napis = drugi.napis[0:4]+self.napis[4:8]
        return o1,o2
    def __str__(self):
        return str(napis)
        

lista = [osobnik() for x in range( 100)]

print("PRZED NAUKĄ:")
    
for o in lista:
    print(o.napis) 

for num in range(900): 
    lista.sort(reverse=True,key = osobnik.przystosowanie)
    ile = [i.przystosowanie for i in lista]
    ile = sum(ile)
    pula_losujaca = [i.przystosowanie/ile for i in lista]


    lista2 = []
    # licznik = 0
    # for s in pula_losujaca:
    #     licznik += int(100*s)
    for i,s in zip(lista,pula_losujaca): 
        lista2 += [i]*int((1000 )*s )


    lista3 = []
    for i in range(50):
        index1 = random.randint(0,len(lista2)-1)
        index2 = random.randint(0,len(lista2)-1)

        osobnik1, osobnik2 = lista2[index1].krzyzuj(lista2[index2])
        lista3.append(osobnik1)
        lista3.append(osobnik1)
    lista = lista3
    if sum([sum(o.napis) for o in lista]) == 800:
        print("nauczyłem się po " + str(num) + " iteracjach")
        break

    
print("PO NAUCE")
for o in lista:
    print(o.napis)


# In[ ]:





# In[ ]:




