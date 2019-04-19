# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 16:59:09 2019

@author: enzos
"""
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
                "Biblioteca": "Ir a Biblioteca"
            }
        },
        "Biblioteca": {
            "titulo": "Biblioteca",
            "descricao": "Voce chegou a Biblioteca do Insper",
            "opcoes": {
                "Procurar um livro": "Talvez um livro possa te ajudar",
                "Aquario": "Ir para um aquario rushar o Ep",
                "Saguao": "Voltar para o Saguao"
            }
        },
        "Aquario":{
            "titulo":"Voce e merecedor",
            "descricao":"Voce ganhou um kit Bicho",
            "opcoes":{
                "Biblioteca": "Voltar para Biblioteca"
             }  
        },
        "Procurar um livro": {
            "titulo":"Voce e merecedor",
            "descricao":"Voce ganhou um Livro de Calculo",
            #Colocar codigo do livro
            "opcoes":{
                "Biblioteca": "Voltar para Biblioteca"
             }  
        },  
        "Help-Desk": {
            "titulo":"Help-Desk",
            "descricao":"Precisa de alguma ajuda?",
            #Colocar codigo do livro
            "opcoes":{
                "2 andar": "Voltar Para o Corredor do 2 andar"
             }  
        },  
        "Armario": {
            "titulo":"Armario",
            "descricao":"Voce chegou no seu Armario, Voce lembrou de trazer a chave?",
            #Colocar codigo do livro
            "opcoes":{
                "2 andar": "Voltar Para o Corredor do 2 andar"
             }  
        },  
        "2 andar": {
            "titulo": "2 andar",
            "descricao": "Voce chegou ao 2 andar",
            "opcoes": {
                "Help-Desk": "Talvez eles possam ajudar",
                "Armario": "Sera que voce esqueceu algo no armario?",
                "Elevador": "Voltar para o Elevador"
            }
        },       
          "4 andar": {
            "titulo": "4 andar",
            "descricao": "Voce chegou ao 4 andar",
            "opcoes": {
                "Wii": "Um jogo pode ajudar a relaxar",
                "Sala 405": "Sala do Professor",
                "Elevador": "Voltar para o Elevador"
            }
        }, 
        "Wii": {
            "titulo":"Wii",
            "descricao":"Relaxar e sempre bom",
            #Colocar codigo do livro
            "opcoes":{
                "4 andar": "Voltar Para o Corredor do 4 andar"
             }  
        },  
        "Sala 405": {
            "titulo":"Sala 405",
            "descricao":"Ja criou a coragem necessaria?",
            #Colocar codigo do livro
            "opcoes":{
                "4 andar": "Voltar Para o Corredor do 4 andar"
             }  
        },  
           "3 andar": {
            "titulo": "3 andar",
            "descricao": "Voce chegou ao 3 andar",
            "opcoes": {
                "Elevador": "Voltar para o Elevador"
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
            }
         }
    }
    nome_cenario_atual = "Porta do Insper"
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


