import sistemas

def mestre_player():
    while True:
        sistemas.utils.menu()
        print("""=== ESCOLHA ===""")
        print(""" 
[1] Mestre
[2] Jogador
[0] Sair
""")
        escolha_menu = input("Escolha: ").strip()
        try:
            if escolha_menu == "1":
                menu_mestre()

            elif escolha_menu == "2":
                menu_jogador()

            elif escolha_menu == "0":
                print("\nEncerrando BETSU...")
                input("\nPressione ENTER para continuar...")
                break

            else:
                print("\nOpção inválida.")
                input("\nPressione ENTER para continuar...")

        except EOFError:
            sistemas.utils.encerrar()
            break


def menu_mestre():
    while True:
        sistemas.utils.menu()
        print("""=== betsu rpg - mestre ===""".upper())
        print("""
[1] Status
[2] Betsuário
[3] Spawn
[4] Lojas
[5] Dado
[0] Sair
""")
        escolha_mestre = input("Escolha: ").strip()
        try:
            if escolha_mestre == "1":
                sistemas.status.executar()
            
            elif escolha_mestre == "2":
                sistemas.betsuario.executar()

            elif escolha_mestre == "3":
                sistemas.spawn.executar()

            elif escolha_mestre == "4":
                sistemas.lojas.executar()

            elif escolha_mestre == "5":
                sistemas.dado.executar()

            elif escolha_mestre == "0":
                break

            else:
                print("\nOpção inválida.")
                input("\nPressione ENTER para continuar...")
        
        except EOFError:
            sistemas.utils.encerrar()
            break

def menu_jogador():
    while True:
        sistemas.utils.menu()
        print ("""=== betsu rpg - jogador ===""".upper())
        print("""
[1] Status
[2] Betsuário
[3] Lojas
[4] Dado
[0] Sair
""")
        
        escolha_jogador = input("Escolha: ").strip()
        try:
            if escolha_jogador == "1":
                sistemas.status.executar()

            elif escolha_jogador == "2":
                sistemas.betsuario.executar()

            elif escolha_jogador == "3":
                sistemas.lojas.executar()
            
            elif escolha_jogador == "4":
                sistemas.dado.executar()

            elif escolha_jogador == "0":
                break

            else:
                sistemas.utils.encerrar()

        except EOFError:
            sistemas.utils.encerrar()
            break        


def main():
    try:
        sistemas.utils.limpar()
        mestre_player()
    
    except (KeyboardInterrupt, EOFError, ValueError):
        sistemas.utils.encerrar()

if __name__ == "__main__":
    main()