import json
import os
    
def limpar():
    os.system("clear")  # Linux
    # os.system("cls")  # Windows

def executar():
    limpar()
    print("\n=== BETSUARIO ===")

    # Carrega o arquivo
    with open("dados/betsuario.json", "r", encoding="utf-8") as arquivo:
        betsuario = json.load(arquivo)

    def escolher_opcao(opcoes, titulo):
        print(f"\n=== {titulo} ===")

        lista = list(opcoes)

        for i, item in enumerate(lista, start=1):
            print(f"[{i}] {item}")

        while True:
            try:
                escolha = int(input("\nEscolha: "))

                if 1 <= escolha <= len(lista):
                    return lista[escolha - 1]

                print("Opção inválida.")

            except ValueError:
                print("Digite apenas números.")


    while True:

        # Reino
        reino = escolher_opcao(
            betsuario.keys(),
            "REINOS"
        )

        # Região
        regiao = escolher_opcao(
            betsuario[reino].keys(),
            "REGIÕES"
        )

        # Mob
        mob = escolher_opcao(
            betsuario[reino][regiao].keys(),
            "MOBS"
        )

        dados = betsuario[reino][regiao][mob]

        print("\n" + "=" * 40)
        print(mob.upper())
        print("=" * 40)

        for chave, valor in dados.items():

            if isinstance(valor, list):
                print(f"\n{chave}:")
                for item in valor:
                    print(f" - {item}")

            else:
                print(f"\n{chave}: {valor}")

        print("\n" + "=" * 40)

        voltar = input(
            "\nDeseja consultar outro mob? (s/n): "
        ).lower()

        if voltar != "s":
            break

if __name__ == "__main__":
    executar() 