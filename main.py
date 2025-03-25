from modulos import downloader
from menus import menus
import os


def exibir_menu(titulo, opcoes):
    """Função para exibir o menu com opções."""
    os.system("cls" if os.name == "nt" else "clear")
    
    
    print("=" * 50)
    print(f"{titulo} (Windows)")
    print("=" * 50)

    for chave, opcao in opcoes.items():
        print(f"{chave}️⃣  {opcao[0]}")
    
    print("\n" + "=" * 50)

def menu_principal():
    opcoes_principais = {
        "1": ("Navegadores", menus.menu_navegadores),
        "2": ("SDK's", menus.menu_sdk),
        "3": ("Ambientes de desenvolvimento", menus.menu_ides),
        "4": ("Banco de dados", menus.menu_banco_de_dados),
        "5": ("Sair", None)
    }
    
    while True:
        exibir_menu("Escolha a Categoria de Aplicativos", opcoes_principais)

        escolha = input("👉 Digite o número correspondente: ")

        if escolha in opcoes_principais:
            if escolha == "5":
                print("\n👋 Saindo... Até logo!\n")
                break
            else:
                opcoes_principais[escolha][1]()  # Chama a função do menu escolhido
        else:
            print("\n❌ Opção inválida! Tente novamente.\n")
            input("Pressione ENTER para continuar...")

menu_principal()
