# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 16:59:09 2019

@author: enzos
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

def carregar_cenarios():
    cenarios = {
        "Porta do Insper": {
            "titulo": "Porta do Insper",
            "descricao": "Voce esta na porta de entrada do Insper",
            "opcoes": {
                "Saguao": "Entrar no Insper e ir para o Saguao",
                
            }
        },
        "Saguao": {
            "titulo": "Saguao",
            "descricao": "Voce entrou no Insper e esta no saguao",
            "opcoes": {
                "Porta do Insper": "Voltar para o Porta do Insper",
                "Elevador": "Entrar no Elevador",
                "Biblioteca": "Ir a Biblioteca",
                "Inventario": "Abrir Inventario",
            }
        },
        "Biblioteca": {
            "titulo": "Biblioteca",
            "descricao": "Voce chegou a Biblioteca do Insper",
            "opcoes": {
                "Procurar um livro": "Talvez um livro possa te ajudar",
                "Aquario": "Ir para um aquario rushar o Ep",
                "Saguao": "Voltar para o Saguao",
                "Inventario": "Abrir Inventario"
            }
        },
        "Aquario":{
            "titulo":"Voce e merecedor",
            "descricao":"Voce ganhou um kit Bicho",
            "opcoes":{
                "Biblioteca": "Voltar para Biblioteca",
                "Inventario": "Abrir Inventario"
             } 
            
        },
        "Procurar um livro": {
            "titulo":"Voce e merecedor",
            "descricao":"Voce ganhou um Livro de Calculo",
            "opcoes":{
                "Biblioteca": "Voltar para Biblioteca",
                "Inventario": "Abrir Inventario"
             }  
        }, 
        "Teleporte": {
            "titulo":"Teleporte",
            "descricao":"Onde voce deseja ir?",
            "opcoes":{
                "Saguao": "ir para o Saguao",
                "Biblioteca": "Ir para Biblioteca",
                "Elevador": "Ir para o Elevador",
                "Sala 301": "O que terá nessa Sala?",
                "Sala 405": "Sala do Professor",
             }  
        }, 
        "Help-Desk": {
            "titulo":"Help-Desk",
            "descricao":"Precisa de alguma ajuda?",
            "opcoes":{
                "2 andar": "Voltar Para o Corredor do 2 andar",
                "Teleporte": "Vai uma ajudinha?",
                "Inventario": "Abrir Inventario"
             }  
        },  
        "Armario": {
            "titulo":"Armario",
            "descricao":"Voce chegou no seu Armario, Voce lembrou de trazer a chave?",
            "opcoes":{
                "2 andar": "Voltar Para o Corredor do 2 andar",
                "Inventario": "Abrir Inventario"
             }  
        },  
        "1 andar": {
            "titulo": "1 andar",
            "descricao": "Voce chegou ao 1 andar",
            "opcoes": {
                "Elevador": "Voltar para o Elevador",
                "Inventario": "Abrir Inventario"
            }
        },
        "2 andar": {
            "titulo": "2 andar",
            "descricao": "Voce chegou ao 2 andar",
            "opcoes": {
                "Help-Desk": "Talvez eles possam ajudar",
                "Armario": "Sera que voce esqueceu algo no armario?",
                "Elevador": "Voltar para o Elevador",
                "Inventario": "Abrir Inventario"
            }
        }, 
          "3 andar": {
            "titulo": "3 andar",
            "descricao": "Voce chegou ao 3 andar",
            "opcoes": {
                "Sala 301": "Sala da Barbara",                
                "Elevador": "Voltar para o Elevador",
                "Inventario": "Abrir Inventario"
            }
        },
          "Sala 301": {
            "titulo": "Sala 301",
            "descricao": "Sala da Barbara",
            "opcoes": {
                "Elevador": "Voltar para o Elevador",
                "Inventario": "Abrir Inventario"
            }
        },
          "4 andar": {
            "titulo": "4 andar",
            "descricao": "Voce chegou ao 4 andar",
            "opcoes": {
                "Wii": "Um jogo pode ajudar a relaxar",
                "Sala 405": "Sala do Professor",
                "Elevador": "Voltar para o Elevador",
                "Inventario": "Abrir Inventario"
            }
        }, 
        "Wii": {
            "titulo":"Wii",
            "descricao":"Relaxar e sempre bom",
            "opcoes":{
                "4 andar": "Voltar Para o Corredor do 4 andar",
                "Inventario": "Abrir Inventario"
             }  
        },  
        "Sala 405": {
            "titulo":"Sala 405",
            "descricao":"Ja criou a coragem necessaria?",
            "opcoes":{
                "4 andar": "Voltar Para o Corredor do 4 andar",
                "Inventario": "Abrir Inventario"
             }  
        }, 
        "Elevador": {
               "titulo": "Elevador",
            "descricao": "Voce entrou no Elevador",
            "opcoes": {
                "Saguao": "Voltar para o Saguao",
                "1 andar": "Ir para o 1 andar",
                "2 andar": "Ir para o 2 andar",
                "3 andar": "Ir para o 3 andar",
                "4 andar": "Ir para o andar",
                "Inventario": "Abrir Inventario"
            }
         }
    }
    nome_cenario_atual = "Porta do Insper"
    if opcoes == "Saguao":
        a = random.randint(1,20)
        if a == 1:
            while veterano['vida'] > 0 and nome['vida'] > 0:
                veterano['vida'] = veterano['vida'] - nome['ataque']
                nome['vida'] = nome['vida'] - veterano['ataque']
                if veterano['vida'] == 0:
                    print("Você ganhou do veterano, confira seu inventario" 
                          "para ver se você ganhou algum item especial")
                elif nome['vida'] == 0:
                    game_over = True
    if opcoes == "Inventario":
        print(inventario_nome)
    if opcoes == "Armario":
        for e in inventario_nome:
            if e == "Chave do Armario":
                inventario_nome.append("Kit Bicho")
            else:
                print("Você não tem como abrir o armário, parece que"
                      "esqueceu de trazer a chave. Aonde ela pode estar?")
    if opcoes == "1 andar":
        print("Você encontrou um veterano, ele não foi com sua cara por ter"
              "subido um andar de elevador, e te atacou.")
        while veterano['vida'] > 0 and nome['vida'] > 0:
                veterano['vida'] = veterano['vida'] - nome['ataque']
                nome['vida'] = nome['vida'] - veterano['ataque']
                if veterano['vida'] == 0:
                    print("Você ganhou do veterano, confira seu inventario" 
                          "para ver se você ganhou algum item especial")
                elif nome['vida'] == 0:
                    game_over = True
    if opcoes == "Sala 301":
        inventario_nome.append("EP")
        print("Na sala 301 você encontrou a Barbara. Cheio de dúvidas"
              "você pediu a ajuda dela para terminar seu EP."
              "Deu tudo certo, seu EP está pronto! Agora é entregar"
              "para o professor e esperar aquele A+")
    if opcoes == "Procurar um livro":
                inventario_nome.append["livro de cálculo"]
    if opcoes == "Aquario":
                inventario_nome.append["Chave do Armário"]
    if opcoes == "Wii":
        while veterano['vida'] > 0 and nome['vida'] > 0:
            veterano['vida'] = veterano['vida'] - nome['ataque']
            nome['vida'] = nome['vida'] - veterano['ataque']
            if veterano['vida'] == 0:
                print("Você ganhou do veterano, confira seu inventario" 
                      "para ver se você ganhou algum item especial")
            elif nome['vida'] == 0:
                game_over = True
    if opcoes == "Sala 405":
        for e in inventario_nome:
            if e == "EP":
                print("Parabens! Voce conseguiu entregar o Ep a tempo" 
                      "sua nota foi maxima!")
            elif e!= "EP":
                game_over == True
    
    return cenarios, nome_cenario_atual

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
    
if __name__ == "__main__":
    main()
    
cenarios, nome_cenario_atual = carregar_cenarios()

game_over = False

while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        print(cenario_atual["titulo"])
        print(len(cenario_atual["titulo"])*"-")
        print(cenario_atual["descricao"])
        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            print("Suas opções são:")
            for x,y in opcoes.items():
                print("{0}:{1}".format(x,y))
            escolha = (input("Qual sua opção?")).strip()
            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True
                print("Você morreu!"
                      "------------"
                      " GAME OVER  ")


