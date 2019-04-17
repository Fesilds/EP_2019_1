# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 16:19:54 2019

@author: enzos
"""

def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

cenarios, nome_cenario_atual = carregar_cenarios()

game_over = False
while not game_over:
    cenario_atual = cenarios[nome_cenario_atual]

    print("Porta do Insper")
    print("---------------")
    print()
    print("O medo de ir pedir ao professor que adie o EP é muito grande"
          "Mas você sente a determinação no seu coração e toma o primeiro passo"
          "É só entrar na porta e começar sua aventura!"
          "Ou não, sei lá...")
    print()      
       
    opcoes = cenario_atual['opcoes']
    if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
    else:

            escolha = "Qual a sua escolha?"

    if escolha in opcoes:
                nome_cenario_atual = escolha
    else:
        print("Sua indecisão foi sua ruína!")
        game_over = True

    print("Você Perdeu!")


# Programa principal.
if __name__ == "__main__":
    main()
