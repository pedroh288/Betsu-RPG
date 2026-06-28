import json
import os
    
def limpar():
    os.system("clear")  # Linux
    # os.system("cls")  # Windows

def executar():
    limpar()
    print("""\33[35m
*****************************************************
*                                                   *
*     ██╗      ██████╗      ██╗ █████╗ ███████╗     *
*     ██║     ██╔═══██╗     ██║██╔══██╗██╔════╝     *
*     ██║     ██║   ██║     ██║███████║███████╗     *
*     ██║     ██║   ██║██   ██║██╔══██║╚════██║     *
*     ███████╗╚██████╔╝╚█████╔╝██║  ██║███████║     *
*     ╚══════╝ ╚═════╝  ╚════╝ ╚═╝  ╚═╝╚══════╝     *
*                                                   *
*****************************************************
          \33[0m""")

    caminho = os.path.join(
        os.path.dirname(__file__),
        "..",
        "dados",
        "lojas.json"
    )

    # Carrega o arquivo
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            lojas = json.load(arquivo)
    except FileExistsError:
        print("Arquivo lojas.json não encontrado")
        return
    except json.JSONDecodeError:
        print("Erro no formato do betsuario.json")
        return
    
    def escolher_opcao(opcoes, titulo):
        print(f"=== \33[36m{titulo}\33[0m ===")

        lista = list(opcoes)

        for i, item in enumerate(lista, start=1):
            print(f"[{i}] {item}")
            
        print("[0] Voltar")

        while True:
            try:
                escolha = int(
                    input("\nEscolha: ")
                )

                if escolha == 0:
                    return None

                if 1 <= escolha <= len(lista):
                    return lista[escolha - 1]


                print("Opção inválida.")

            except ValueError:
                print("Digite apenas números.")

    while True:
        #Reino
        reino = escolher_opcao(
            lojas.keys(),
            "Reinos"
        )

        if reino is None:
            return

        # Local
        local = escolher_opcao(
            lojas[reino].keys(),
            "LOCAIS"
        )

        if local is None:
            return

        dados_local = lojas[reino][local]

        #limpar()

        # Verifica se existe ação (Comprar, Venda, Fabricar)
        if any(
            opcao in dados_local
            for opcao in ["Comprar", "Venda", "Fabricar"]
        ):

            acao = escolher_opcao(
                dados_local.keys(),
                local.upper()
            )

            if acao is None:
                continue

            itens = dados_local[acao]

        else:
            itens = dados_local

        # Item
        item = escolher_opcao(
            itens.keys(),
            "ITENS"
        )

        if item is None:
            continue

        dados = itens[item]

        #limpar()

        print("\n" + "=" * 40)
        print(f"\33[33m{item.upper()}\33[0m")
        print("=" * 40)

        for chave, valor in dados.items():

            if isinstance(valor, list):
                print(f"\n{chave}:")

                for item_lista in valor:
                    print(f" - {item_lista}")

            else:
                if chave == "Preço":
                    print (f"\n{chave}: B${valor}")
                
                else:
                    print(f"\n{chave}: {valor}")

        print("\n" + "=" * 40)
    
        voltar = input(
            "\nDeseja consultar outro mob? (s/n): "
            ).lower()

        if voltar == "s":
            limpar()
            continue
        
        else:
            break

if __name__ == "__main__":
    executar() 