# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 11:52:58 2019

@author: felip
"""
import random 
nome = {}
nome['vida']= 10
nome['ataque'] = 1
inventario_nome= []
for e in inventario_nome:
    if e == ("livro de cálculo"):
        nome['ataque']+=2
    elif e == ('kit Bixo'):
        nome['ataque']+= 5
        nome['vida']+= 5
veterano = {}
veterano['vida'] = 20
veterano['ataque'] = 5
inventario_do_veterano = []
    
a = random.randint(1,20)
if ((a/3) == 0):
    inventario_do_veterano.append("livro de cálculo")
elif a== 10:
    inventario_do_veterano.append("Kit Bixo")
game_on = True 
print("Porta do Insper"
      "---------------"
      "Voce esta na porta "
      "de entrada do Insper")
while game_on == True:
    opcoes = input("Para aonde deseja ir?")

    if opcoes == "Saguao":
            print("Saguao")
            print( "-------")
            print("Voce entrou no Insper e esta no saguao")
            opcoes = input("Para aonde deseja ir?")
    if opcoes == "Biblioteca":
        print("Biblioteca"
              "----------"
              "Voce chegou a Biblioteca do Insper"
              "lá você pode procurar por um livro"
              "para saber mais sobre o EP, ir para"
              "um aquario tentar fazer o EP ou voltar"
              "para o Saguao,")
        opcoes = input("Para aonde deseja ir: Procurar um livro,"
                       "Aquario, ou Saguao?")
        if opcoes != "Procurar um livro" or "Aquario" or "Saguao":
            print("Opcao invalida, digite novamente")
            opcoes = input("Para aonde deseja ir: Procurar um livro,"
                       "Aquario, ou Saguao?")

    if opcoes == "Aquario":
        print("Aquario"
              "-------"
              "Voce encontrou sua chave do armario")
        inventario_nome.append("chave do armario")
    if opcoes == "1 andar":
        print("1 andar"
              "--------"
              "Voce chegou ao 1 andar")
        print("Você encontrou um veterano, ele não foi com sua cara por ter"
              "subido um andar de elevador, e te atacou.")
        while veterano['vida'] > 0 and nome['vida'] > 0:
            veterano['vida'] = veterano['vida'] - nome['ataque']
            nome['vida'] = nome['vida'] - veterano['ataque']
            if veterano['vida'] == 0:
                print("Você ganhou do veterano, confira seu inventario" 
                      "para ver se você ganhou algum item especial")
            elif nome['vida'] == 0:
                print("Você perdeu")