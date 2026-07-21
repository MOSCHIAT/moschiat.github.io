#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de Citações
Um projeto simples que gera citações aleatórias inspiradoras.
"""

import random

# Lista de citações inspiradoras
QUOTES = [
    ("A criatividade é a inteligência se divertindo.", "Albert Einstein"),
    ("O único modo de fazer um ótimo trabalho é amar o que você faz.", "Steve Jobs"),
    ("Inovação distingue um líder de um seguidor.", "Steve Jobs"),
    ("A vida é 10% o que acontece com você e 90% como você reage a isso.", "Charles R. Swindoll"),
    ("O futuro pertence àqueles que acreditam na beleza de seus sonhos.", "Eleanor Roosevelt"),
    ("Não é sobre como começar, é sobre como terminar.", "Amy Poehler"),
    ("Você não pode mudar o vento, mas pode ajustar suas velas.", "Dolly Parton"),
    ("A única coisa que está entre você e seus objetivos é a história que você continua contando a si mesmo.", "Jordan Belfort"),
    ("Sucesso não é final, fracasso não é fatal.", "Winston Churchill"),
    ("Faça algo hoje que seu 'eu' futuro agradecerá.", "Sean Patrick Flanery"),
]


def get_random_quote():
    """
    Retorna uma citação aleatória da lista.
    
    Returns:
        tuple: (citação, autor)
    """
    return random.choice(QUOTES)


def display_quote(quote, author):
    """
    Exibe uma citação formatada.
    
    Args:
        quote (str): O texto da citação
        author (str): O autor da citação
    """
    print("\n" + "=" * 60)
    print(f'  "{quote}"')
    print(f"  — {author}")
    print("=" * 60 + "\n")


def main():
    """
    Função principal.
    """
    print("\n🌟 Bem-vindo ao Gerador de Citações! 🌟")
    print("\nDigite 'q' para sair ou pressione Enter para nova citação\n")
    
    while True:
        user_input = input("Pressione Enter para nova citação (ou 'q' para sair): ").strip().lower()
        
        if user_input == 'q':
            print("\nAté logo! 👋\n")
            break
        
        quote, author = get_random_quote()
        display_quote(quote, author)


if __name__ == "__main__":
    main()
