# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 16:11:30 2019

@author: felip
"""
while veterano['vida'] > 0 and nome['vida'] > 0:
    veterano['vida'] = veterano['vida'] - nome['ataque']
    nome['vida'] = nome['vida'] - veterano['ataque']
    if veterano['vida'] == 0:
        print("Você ganhou do veterano, confira seu inventario" 
     "para ver se você ganhou algum item especial")
    elif nome['vida'] == 0:
        print("GAME OVER")
        
       

