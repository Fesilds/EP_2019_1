# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:30:46 2019

@author: felip
"""
import random 
#Monstro 
Veterano = {}
Veterano["Vida"] = 20
Veterano["Ataque"] = 5
inventario_do_veterano = []
    
a = random.randint(1,20)
if ((a/3) == 0):
    inventario_do_veterano.append("livro de cálculo")
elif a== 10:
    inventario_do_veterano.aapend("Kit Bixo")