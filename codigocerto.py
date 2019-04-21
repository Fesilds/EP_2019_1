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
    opcoes = input("Deseja entrar?")

    if opcoes == "Saguao" or opcoes == "Sim":
            print("Saguao")
            print( "-------")
            print("Voce entrou no Insper e esta no saguao,"
                  "e ve a biblioteca e o elevador." )
            opcoes = input("Para aonde deseja ir?")
    if opcoes == "Biblioteca":
        print("Biblioteca")
        print("----------")
        print("Voce chegou a Biblioteca do Insper"
              "lá você pode procurar por um livro"
              "para saber mais sobre o EP, ir para"
              "um aquario tentar fazer o EP ou voltar"
              "para o Saguao,")
        opcoes = input("Para aonde deseja ir: Procurar um livro,"
                       "Aquario, ou Saguao?")
        if opcoes != "Procurar um livro" or opcoes != "Aquario" or opcoes != "Saguao":
            print("Opcao invalida, digite novamente")
            opcoes = input("Para aonde deseja ir: Procurar um livro,"
                       "Aquario, ou Saguao?")

    if opcoes == "Aquario":
        print("Aquario"
              "-------"
              "Voce encontrou sua chave do armario")
        inventario_nome.append("chave do armario")
        opcoes = input("Para aonde deseja ir: Procurar um livro,"
                       "ou Saguao?")
    if opcoes == "Procurar um livro":
        print("Procurar um livro")
        print("-----------------")
        print("Ao procurar por um livro, você encontra um de cálculo")
        print("e guarda no seu inventario para te ajudar futuramente")
        opcoes = input("Para aonde deseja ir:,"
                       "Aquario, ou Saguao?")
    if opcoes == "Elevador":
        opcoes = input("Você entrou no elevador, para qual andar deseja ir:"
              "1 andar/ 2andar/ 3 andar/ 4 andar/ sair do elevador ?")
    if opcoes == "2 andar":
        print("2 andar")
        print("-------")
        print("Você esta no 2 andar, saindo do elevador você encontra o Help-")
        print("Desk, e os Armarios.")
        opcoes = input("Para aonde deseja ir: Help-Desk, Armarios ou voltar"
                       "ao Elevador?")
    if opcoes == "Help-Desk":
        print("Help-Desk")
        print("---------")
        print("Você chegou no Help-Desk e pediu ajuda a um dos profissionais lá")
        print("ele te diz que vai te ajudar e mostra o Portal-HD, ele pode te levar")
        print("para qualquer lugar desde que você saiba o nome do lugar que deseja ir")
        opcoes = input("Aonde quer que o Portal-HD te leve?")
    if opcoes == "Armario":
        print("Armario")
        print("-------")
        print("Você lembra que havia deixado algo importante no armario,")
        print("Por acaso esta com a chave?")
        for e in inventario_nome:
            if e == "chave do armario":
                inventario_nome.append("kit bicho")
                print("Abrindo o armario você pega seu kit bicho, que te da um UP")
                print("contra os terriveis veteranos")
            else:
                print("Não importa a força que faça, não consegue abrir o armario")
                print("sem a chave, ela esta perdida pelo Insper, vá encontra-la!")
        opcoes = input("Para aonde deseja ir: Help-Desk ou Elevador")
    if opcoes == "3 andar":
        print("3 andar")
        print("-------")
        print("Você chgou no 3 andar, não há muito a se fazer aqui, se não fosse")
        print("pela sala da Barbara na 301, será que ela vai te ajudar ?")
        opcoes = input("Para aonde deseja ir: Sala 301 ou Elevador")
    if opcoes == "Sala 301":
        print("Sala 301")
        print("--------")
        print("Você entra na sala da Barbara, e humildemente pede a ajuda dela")
        print("para finalizar o EP. Com toda bondade ela te explica os erros no")
        print("seu codigo e te ajuda a arrumar seu EP.")
        print("Tudo pronto, agora é só entregar o EP para o porfessor")
        print("onde ele pode estar?")
        inventario_nome.append("EP")
        opcoes = input("Para aonde deseja ir: 3 andar ou Elevador"
    if opcoes == "4 andar":
        print("4 andar")
        print("------")
        print("Você chegou no 4 andar, avistando a sua frente um espaço")
        print("com um Wii e a sala do porfessro 405")
        opcoes = input("Para aonde deseja ir: Wii, Sala 405 ou Elevador")
    if opcoes == "Wii":
        print("Jogar um Wii")
        print("------------")
        print("Você estava cansado decidiu jogar um pouco para descansar, quando")
        print("foi pegar o controle um Veterano apareceu e decidiu brigar com você")
        while veterano['vida'] > 0 and nome['vida'] > 0:
                veterano['vida'] = veterano['vida'] - nome['ataque']
                nome['vida'] = nome['vida'] - veterano['ataque']
                if veterano['vida'] == 0:
                    print("Você ganhou do veterano!")
                    opcoes = input("Para onde deseja ir: Sala 405 ou Elevador?")
                elif nome['vida'] == 0:
                    print("Você morreu!")
                    print("------------")
                    print(" GAME OVER  ")
                    game_on == False
    if opcoes == "Sala 405":
        for e in inventario_nome:
            if e == "EP":
                print("Voce chegou na sala do seu professor, confiante você")
                print("olha no fundo dos olhos do porfessor e entrega seu belo")
                print("EP finalizado, agora é so esperar o A+ no seu trabalho")
                print("------------------------------------------------------")
                print("                    YOU WIN!                          ")
            else:
                print("Você chega no seu professor com uma certa inseguraça,")
                print("ao pedir para ele adiar a entrega do EP, seu professor")
                print("se transforma em um monstro e te devora")
                print("              Você morreu!             ")
                print("---------------------------------------")
                print("               GAME OVER               ")
        break
    if opcoes == "1 andar":
        print("1 andar")
        print("-------")
        print("Voce chegou ao 1 andar")
        print("Você encontrou um veterano, ele não foi com sua cara por ter"
              "subido um andar de elevador, e te atacou.")
        while veterano['vida'] > 0 and nome['vida'] > 0:
            veterano['vida'] = veterano['vida'] - nome['ataque']
            nome['vida'] = nome['vida'] - veterano['ataque']
            if veterano['vida'] == 0:
            elif nome['vida'] == 0:
                print("Você morreu!")
                print("------------")
                print(" GAME OVER  ")
        break

