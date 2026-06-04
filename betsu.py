import os

from sistemas import status
from sistemas import betsuario
from sistemas import spawn

VERSAO = "0.1"

def limpar():
    os.system("clear")  # Linux
    # os.system("cls")  # Windows

def mostrar_menu():
    print("=" * 40)
    print(f"       BETSU v{VERSAO}")
    print("=" * 40)

    print("[1] Betsuário")
    print("[2] Status")
    print("[3] Spawn")
    print("[4] xxx")
    print("[0] Sair")

def executar_opcao(opcao):

    if opcao == "1":
        limpar()
        betsuario.executar()

    elif opcao == "2":
        limpar()
        status.executar()

    elif opcao == "3":
        limpar()
        spawn.executar()

    elif opcao == "4":
        print("\nSistema ainda não implementado.")

    elif opcao == "0":
        print("\nEncerrando BETSU...")
        return False

    else:
        print("\nOpção inválida.")

    input("\nPressione ENTER para continuar...")
    return True

def main():

    while True:

        limpar()
        mostrar_menu()

        opcao = input("\nEscolha: ")

        if not executar_opcao(opcao):
            break

if __name__ == "__main__":
    main()