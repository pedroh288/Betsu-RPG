## CÓDIGO PARA SISTEMA DE SPAWN DE MONSTROS ##

import random
import time
import os
import json

def limpar():
    os.system("clear")  # Linux
    # os.system("cls")  # Windows

def executar():
    limpar()
    print("""\33[35m
********************************************************
*                                                      *
*     ███████╗██████╗  █████╗ ██╗    ██╗███╗   ██╗     *
*     ██╔════╝██╔══██╗██╔══██╗██║    ██║████╗  ██║     *
*     ███████╗██████╔╝███████║██║ █╗ ██║██╔██╗ ██║     *
*     ╚════██║██╔═══╝ ██╔══██║██║███╗██║██║╚██╗██║     *
*     ███████║██║     ██║  ██║╚███╔███╔╝██║ ╚████║     *
*     ╚══════╝╚═╝     ╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═══╝     *
*                                                      *
********************************************************
          \33[0m""")

    caminho = os.path.join(
        os.path.dirname(__file__),
        "..",
        "dados",
        "spawn.json"
    )

    # Definir as cores para cada raridade (ANSI escape codes)
    cores_raridade = {
        "Comum": "\033[32m",    # Verde
        "Incomum": "\033[33m",  # Amarela
        "Raro": "\033[31m",      # Vermelho
        "Épico": "\033[35m",    # Roxo/Magenta
        "Mítico": "\033[36m",   # Ciano
        "Calamidade": "\033[35m" # Magenta
    }
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            regioes = json.load(arquivo)
    except FileNotFoundError:
        print("Arquivo spawn.json não encontrado.")
        return
    except json.JSONDecodeError:
        print("Erro no formato do spawn.json")
        return

    lista_regioes = list(regioes.keys())

    CHANCE_SPAWN = 80
    CHANCE_NADA = 20


    def escolher_monstro(reino, regiao, horario):
        """Escolhe um monstro baseado no reino, região e horário usando roleta de chances."""

        # 1. Verifica se a combinação é válida
        if reino not in regioes or regiao not in regioes[reino] or horario not in ["Dia", "Noite", "Madrugada"]:
            return None, None

        chances_monstros = regioes[reino][regiao]

        # Extrai os nomes dos monstros e suas chances para o horário escolhido
        monstros = list(chances_monstros.keys())
        # O valor de chance é obtido usando dados[horario], que é a chave 'Dia', 'Noite' ou 'Madrugada'
        pesos = [dados.get(horario, 0) for dados in chances_monstros.values()]

        # Filtra monstros com chance > 0 para evitar erros no random.choices
        monstros_validos = [monstros[i] for i in range(len(monstros)) if pesos[i] > 0]
        pesos_validos = [pesos[i] for i in range(len(pesos)) if pesos[i] > 0]

        # Se não houver monstros com chance > 0, retorna None
        if not monstros_validos:
            return None, None

        # 2. Escolhe o monstro usando a distribuição de pesos (chances)
        # k=1 significa que apenas um item será escolhido
        monstro_escolhido = random.choices(monstros_validos, weights=pesos_validos, k=1)[0]

        # 3. Obtém a raridade do monstro escolhido
        raridade = chances_monstros[monstro_escolhido]["Raridade"]

        return monstro_escolhido, raridade

    # Roleta para decidir se um monstro vai aparecer (80% de chance de "Sim")
    aparece = random.choices(["Sim", "Não"], weights=[CHANCE_SPAWN, CHANCE_NADA], k=1)[0]

    if aparece == "Não":
        tempo_spawn = 3
        time.sleep(tempo_spawn)
        print("Nada apareceu dessa vez...")
    else:
        while True:
            # --- Interação com o Usuário para Escolha de Reino ---

            while True:
                print(f"=== \33[36m{"Reino".upper()}\33[0m ===")
                for i, nome in enumerate(lista_regioes, start=1):
                    print(f"[{i}] - {nome}")
        
                print("[0] - Voltar/Sair")

                opcao = input("\nEscolha: ")

                if opcao == "0":
                    print("Finalizando o programa!")
                    return

                try:
                    opcao = int(opcao)
                except ValueError:
                    print("Digite apenas números.")
                    continue

                if opcao < 1 or opcao > len(lista_regioes):
                    print("Reino inválido.")
                    continue

                reino = lista_regioes[opcao - 1]
                break

            nome_reino = reino

            # Escolha do local dentro da região
            lista_locais = list(regioes[reino].keys())

            while True:
                print(f"\n=== \33[36mREGIÃO DE {nome_reino.upper()}\33[0m ===")
                for i, regiao in enumerate(lista_locais, start=1):
                    print(f"[{i}] - {regiao}")

                print("[0] - Sair")

                opcao_regiao = input("\nEscolha: ")

                if opcao_regiao == "0":
                    print("Finalizando o programa!")
                    return

                try:
                    opcao_regiao = int(opcao_regiao)
                except ValueError:
                    print("Digite apenas números.")
                    continue

                if opcao_regiao < 1 or opcao_regiao > len(lista_locais):
                    print("Região inválido.")
                    continue

                regiao = lista_locais[opcao_regiao - 1]
                break

            nome_regiao = regiao

            # Escolha do horário
            while True:
                print(f"\n=== \33[36m{"Horário".upper()}\33[0m ===")
                print("[1] - Dia")
                print("[2] - Noite")
                print("[3] - Madrugada")
                print("[0] - Sair")
                horario_opcao = input("\nEscolha: ")

                if horario_opcao == "0":
                    print("\nFinalizando o programa!")
                    return

                horarios = {"1": "Dia", "2": "Noite", "3": "Madrugada"}
                horario = horarios.get(horario_opcao, None)

                if not horario:
                    print("\nHorário inválido. Reinicie o programa e tente novamente.")
                    continue
                break

            print()
            print('='*20)

            # Tempo de espera antes do spawn
            tempo_espera = 5
            print(f"Aguarde {tempo_espera} segundos...")
            time.sleep(tempo_espera)

            # Lógica de Spawn
            monstro_apareceu, raridade = escolher_monstro(reino, regiao, horario)

            print('='*30)
            if monstro_apareceu:
                # Pega a cor correspondente à raridade, ou usa a cor padrão (reset)
                cor = cores_raridade.get(raridade, "\033[0m")
                print(f"\nUm {cor}{monstro_apareceu}\033[0m "
                f"({raridade}) apareceu na {nome_regiao} de {nome_reino} durante a {horario}!")
            else:
                print("\nNada apareceu dessa vez...") # Nada apareceu, pois as chances somadas eram 0 ou a roleta não parou em um monstro válido.
            print()
            print('='*30)

            voltar = input(
                "\nDeseja calcular novamente? (s/n): "
            ).lower()

            if voltar == "s":
                limpar()
                continue

            else:
                break

if __name__ == "__main__":
    executar() 