# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:54:08 2019

@author: enzos
"""
def carregar_cenarios():
    cenarios = {
        "Porta do Insper": {
            "titulo": "Porta do Insper",
            "descricao": "Voce esta na porta de entrada do Insper",
            "opcoes": {
                "Entrar no Insper": "Entrar no Insper e ir para o Saguao",
                "Voltar para Casa": "Miar do Ep e voltar para sua casa"
            }
        },
        "Saguao": {
            "titulo": "Saguao",
            "descricao": "Voce entrou no Insper e esta no saguao",
            "opcoes": {
                "Sair do Insper": "Voltar para o Porta do Insper",
                "Elevador": "Entrar no Elevador",
                "Biblioteca": "Ir a Biblioteca"
            }
        },
        "Biblioteca": {
            "titulo": "Biblioteca",
            "descricao": "Voce chegou a Biblioteca do Insper",
            "opcoes": {
                "Procurar um livro": "Talvez um livro possa de ajudar",
                "Aquario": "Ir para um aquario rushar o Ep",
                "Saguao": "Voltar para o Saguao"
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
        },   
          "3 andar": {
            "titulo": "3 andar",
            "descricao": "Voce chegou ao 3 andar",
            "opcoes": {
                "Elevador": "Voltar para o Elevador"
            }
        }
    }
    }
    nome_cenario_atual = "Porta do Insper"
    return cenarios, nome_cenario_atual
