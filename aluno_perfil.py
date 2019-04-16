# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:19:57 2019

@author: felip
"""
nome = input("Como você se chama?")
nome = {}
nome["Vida"]= 10
nome["Ataque"] = 1
inventario_nome= []
print (nome)
for e in inventario_nome:
    if e == ("livro de cálculo"):
        nome["Ataque"]+=2
    elif e == ("kit Bixo"):
        nome["Ataque"]+= 5
        nome["Vida"]+= 5

    