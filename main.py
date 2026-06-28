import os
import sistemas as sistemas

VERSAO = "0.1"

def limpar():
    os.system("clear")  # Linux
    # os.system("cls")  # Windows

def mostrar_menu():
    print(f"""
>>======================================================<<
||                                                      ||
||  $$$$$$$\  $$$$$$$$\ $$$$$$$$\  $$$$$$\  $$\   $$\   ||
||  $$  __$$\ $$  _____|\__$$  __|$$  __$$\ $$ |  $$ |  ||
||  $$ |  $$ |$$ |         $$ |   $$ /  \__|$$ |  $$ |  ||
||  $$$$$$$\ |$$$$$\       $$ |   \$$$$$$\  $$ |  $$ |  ||
||  $$  __$$\ $$  __|      $$ |    \____$$\ $$ |  $$ |  ||
||  $$ |  $$ |$$ |         $$ |   $$\   $$ |$$ |  $$ |  ||
||  $$$$$$$  |$$$$$$$$\    $$ |   \$$$$$$  |\$$$$$$  |  ||
||  \_______/ \________|   \__|    \______/  \______/   ||
||                                                      ||
>>======================================================<<
                    BETSU {VERSAO}
    """)

    print("[1] Betsuário")
    print("[2] Status")
    print("[3] Spawn")
    print("[4] Lojas")
    print("[0] Sair")

def executar_opcao(opcao):

    if opcao == "1":
        limpar()
        sistemas.betsuario.executar()

    elif opcao == "2":
        limpar()
        sistemas.status.executar()

    elif opcao == "3":
        limpar()
        sistemas.spawn.executar()

    elif opcao == "4":
        limpar()
        sistemas.lojas.executar()

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