import json
import os
from . import utils

def escolher_opcao(opcoes, titulo):
    print(f"\n=== \33[36m{titulo}\33[0m ===")

    lista = list(opcoes)

    for i, item in enumerate(lista, start=1):
        print(f"[{i}] {item}")

    print("[0] Voltar")

    while True:
        try:
            escolha = int(input("\nEscolha: "))

            if escolha == 0:
                print("\nFinalizando o programa!")
                return None

            if 1 <= escolha <= len(lista):
                return lista[escolha - 1]

            print("Opção inválida.")

        except ValueError:
            print("Digite apenas números.")

def executar():
    while True:
        utils.menu_betsuario()

        caminho = os.path.join(
        os.path.dirname(__file__),
        "..",
        "dados",
        "betsuario.json"
        )

        try:
            with open(caminho, "r", encoding="utf-8") as arquivo:
                betsuario = json.load(arquivo)
        except FileNotFoundError:
            print("Arquivo betsuario.json não encontrado")
            return
        except json.JSONDecodeError:
            print("Erro no formato do betsuario.json")
            return

        # Reino
        reino = escolher_opcao(
            betsuario.keys(),
            "REINOS"
        )
                
        # 0
        if reino is None:
            return
        

        # Região
        regiao = escolher_opcao(
            betsuario[reino].keys(),
            "REGIÕES"
        )

        # 0
        if regiao is None:
            return

        # Mob
        mob = escolher_opcao(
            betsuario[reino][regiao].keys(),
            "MOBS"
        )

        if mob is None:
            return   # volta para o betsu.py

        dados = betsuario[reino][regiao][mob]

        print("\n" + "=" * 40)
        print(f"\33[33m{mob.upper()}\33[0m")
        print("=" * 40)

        for chave, valor in dados.items():

            if isinstance(valor, list):
                print(f"\n{chave}:")
                for item in valor:
                    print(f" - {item}")

            else:
                print(f"\n{chave}: {valor}")

        print("\n" + "=" * 40)

        if not utils.sn ("Deseja gerar outro inimigo?"):
            return

if __name__ == "__main__":
    executar() 