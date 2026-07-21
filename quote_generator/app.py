"""Personal Quote Generator - Terminal Interface.

A terminal-based application for browsing, searching, and managing
quotes with persistent favorites storage.
"""

import os
import sys
from typing import Optional
from utils import (
    get_random_quote,
    get_quote_by_category,
    search_quote,
    get_all_categories,
    favorite_quote,
    remove_favorite,
    list_favorites,
    save_favorites,
    load_favorites,
)


def clear_screen() -> None:
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def print_header() -> None:
    """Print the application header."""
    print("\n" + "=" * 50)
    print("         PERSONAL QUOTE GENERATOR")
    print("=" * 50 + "\n")


def display_quote(quote: dict) -> None:
    """Display a single quote in a formatted manner.
    
    Args:
        quote: The quote dictionary to display.
    """
    print("\n" + "-" * 50)
    print(f"📌 {quote['category']}\n")
    print(f'"{quote["quote"]}"\n')
    print(f"— {quote['author']} (ID: {quote['id']})")
    print("-" * 50 + "\n")


def display_quotes_list(quotes: list[dict]) -> None:
    """Display a list of quotes in a compact format.
    
    Args:
        quotes: List of quote dictionaries to display.
    """
    if not quotes:
        print("\n❌ Nenhuma citação encontrada.\n")
        return
    
    print(f"\n📚 Total de citações: {len(quotes)}\n")
    for quote in quotes:
        print(f"[ID: {quote['id']:3}] {quote['category']:20} | {quote['quote'][:50]}...")
    print()


def get_menu_choice() -> str:
    """Get user's menu choice.
    
    Returns:
        str: The user's choice (1-6).
    """
    try:
        choice = input("\nEscolha uma opção (1-6): ").strip()
        return choice
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrompido pelo usuário.")
        sys.exit(0)


def display_menu() -> None:
    """Display the main menu."""
    print("-" * 50)
    print("1 - Citação aleatória")
    print("2 - Procurar categoria")
    print("3 - Pesquisar palavra")
    print("4 - Meus Favoritos")
    print("5 - Listar categorias")
    print("6 - Sair")
    print("-" * 50)


def handle_random_quote() -> None:
    """Handle random quote display."""
    quote = get_random_quote()
    display_quote(quote)
    
    while True:
        choice = input("Deseja favoritar? (s/n): ").strip().lower()
        if choice in ["s", "sim"]:
            if favorite_quote(quote["id"]):
                print("✅ Citação adicionada aos favoritos!\n")
            else:
                print("⚠️  Citação já está nos favoritos.\n")
            break
        elif choice in ["n", "não", "nao"]:
            break
        else:
            print("⚠️  Digite 's' ou 'n'.")


def handle_category_search() -> None:
    """Handle category-based quote search."""
    categories = get_all_categories()
    
    print("\n📂 Categorias disponíveis:")
    for i, category in enumerate(categories, 1):
        print(f"{i:2} - {category}")
    
    try:
        choice = input("\nEscolha uma categoria (número ou nome): ").strip()
        
        # Try numeric choice first
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(categories):
                category = categories[idx]
            else:
                print("❌ Número inválido.")
                return
        except ValueError:
            # Try direct name
            category = choice
        
        quotes = get_quote_by_category(category)
        
        if not quotes:
            print(f"\n❌ Nenhuma citação encontrada na categoria '{category}'.\n")
            return
        
        display_quotes_list(quotes)
        
        while True:
            try:
                quote_id = input("Digite o ID da citação para mais detalhes (ou 'voltar'): ").strip()
                if quote_id.lower() == "voltar":
                    break
                
                quote_id = int(quote_id)
                quote_obj = next((q for q in quotes if q["id"] == quote_id), None)
                
                if quote_obj:
                    display_quote(quote_obj)
                    choice = input("Favoritar? (s/n): ").strip().lower()
                    if choice in ["s", "sim"]:
                        if favorite_quote(quote_obj["id"]):
                            print("✅ Citação adicionada aos favoritos!\n")
                        else:
                            print("⚠️  Citação já está nos favoritos.\n")
                else:
                    print("❌ ID não encontrado.\n")
            except ValueError:
                print("❌ Digite um número válido.")
    
    except KeyboardInterrupt:
        print("\n🔙 Voltando ao menu...")


def handle_keyword_search() -> None:
    """Handle keyword-based quote search."""
    keyword = input("\n🔍 Digite a palavra para pesquisar: ").strip()
    
    if not keyword:
        print("❌ Digite uma palavra válida.\n")
        return
    
    quotes = search_quote(keyword)
    display_quotes_list(quotes)
    
    while True:
        try:
            quote_id = input("Digite o ID da citação para mais detalhes (ou 'voltar'): ").strip()
            if quote_id.lower() == "voltar":
                break
            
            quote_id = int(quote_id)
            quote_obj = next((q for q in quotes if q["id"] == quote_id), None)
            
            if quote_obj:
                display_quote(quote_obj)
                choice = input("Favoritar? (s/n): ").strip().lower()
                if choice in ["s", "sim"]:
                    if favorite_quote(quote_obj["id"]):
                        print("✅ Citação adicionada aos favoritos!\n")
                    else:
                        print("⚠️  Citação já está nos favoritos.\n")
            else:
                print("❌ ID não encontrado.\n")
        except ValueError:
            print("❌ Digite um número válido.")


def handle_favorites() -> None:
    """Handle favorites menu."""
    favorites = list_favorites()
    
    if not favorites:
        print("\n📭 Você ainda não tem favoritos.\n")
        return
    
    print("\n⭐ SEUS FAVORITOS")
    display_quotes_list(favorites)
    
    while True:
        choice = input("Opções: (v)er citação, (r)emover, (v)oltar: ").strip().lower()
        
        if choice in ["v", "ver"]:
            try:
                quote_id = input("Digite o ID da citação: ").strip()
                quote_id = int(quote_id)
                quote_obj = next((q for q in favorites if q["id"] == quote_id), None)
                
                if quote_obj:
                    display_quote(quote_obj)
                else:
                    print("❌ ID não encontrado nos favoritos.\n")
            except ValueError:
                print("❌ Digite um número válido.")
        
        elif choice in ["r", "remover"]:
            try:
                quote_id = input("Digite o ID da citação para remover: ").strip()
                quote_id = int(quote_id)
                
                if remove_favorite(quote_id):
                    print("✅ Citação removida dos favoritos!\n")
                    favorites = list_favorites()  # Atualizar lista
                    if not favorites:
                        print("📭 Nenhum favorito restante.\n")
                        break
                    display_quotes_list(favorites)
                else:
                    print("❌ Citação não encontrada nos favoritos.\n")
            except ValueError:
                print("❌ Digite um número válido.")
        
        elif choice in ["voltar", "sair", "v"]:
            break


def handle_categories() -> None:
    """Display all available categories."""
    categories = get_all_categories()
    
    print("\n📂 CATEGORIAS DISPONÍVEIS\n")
    for i, category in enumerate(categories, 1):
        count = len(get_quote_by_category(category))
        print(f"{i:2} - {category:20} ({count:2} citações)")
    print()


def main() -> None:
    """Main application loop."""
    while True:
        try:
            clear_screen()
            print_header()
            display_menu()
            
            choice = get_menu_choice()
            
            if choice == "1":
                handle_random_quote()
            elif choice == "2":
                handle_category_search()
            elif choice == "3":
                handle_keyword_search()
            elif choice == "4":
                handle_favorites()
            elif choice == "5":
                handle_categories()
            elif choice == "6":
                print("\n👋 Obrigado por usar o Quote Generator!\n")
                sys.exit(0)
            else:
                print("\n❌ Opção inválida. Digite de 1 a 6.")
            
            input("Pressione Enter para continuar...")
        
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrompido.")
            sys.exit(0)
        except Exception as e:
            print(f"\n❌ Erro inesperado: {e}")
            print("Tente novamente.\n")
            input("Pressione Enter para continuar...")


if __name__ == "__main__":
    main()
