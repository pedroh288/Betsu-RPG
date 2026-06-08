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
    print("\n=== SPAWN ===")

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
        with open("dados/spawn.json", "r", encoding="utf-8") as arquivo:
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


    def escolher_monstro(regiao, local, horario):
        """Escolhe um monstro baseado na região, local e horário usando roleta de chances."""

        # 1. Verifica se a combinação é válida
        if regiao not in regioes or local not in regioes[regiao] or horario not in ["Dia", "Noite", "Madrugada"]:
            return None, None

        chances_monstros = regioes[regiao][local]

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
        # --- Interação com o Usuário para Escolha de Local ---

        while True:
            print("\nEscolha a região:")
            for i, nome in enumerate(lista_regioes, start=1):
                print(f"[{i}] - {nome}")
    
            print("[0] - Voltar/Sair")

            opcao = input("Digite o número correspondente a região: ")

            if opcao == "0":
                print("Finalizando o programa!")
                return

            try:
                opcao = int(opcao)
            except ValueError:
                print("Digite apenas números.")
                continue

            if opcao < 1 or opcao > len(lista_regioes):
                print("Região inválida.")
                continue

            regiao = lista_regioes[opcao - 1]
            break

        nome_regiao = regiao
        print('='*20)

        # Escolha do local dentro da região
        lista_locais = list(regioes[regiao].keys())

        while True:
            print(f"\nEscolha o local dentro de {nome_regiao}:")
            for i, local in enumerate(lista_locais, start=1):
                print(f"[{i}] - {local}")

            print("[0] - Sair")

            opcao_local = input("Escolha o local: ")

            if opcao_local == "0":
                print("Finalizando o programa!")
                return

            try:
                opcao_local = int(opcao_local)
            except ValueError:
                print("Digite apenas números.")
                continue

            if opcao_local < 1 or opcao_local > len(lista_locais):
                print("Local inválido.")
                continue

            local = lista_locais[opcao_local - 1]
            break

        nome_local = local
        print('='*20)

        # Escolha do horário
        while True:
            print("\nEscolha o horário:")
            print("[1] - Dia")
            print("[2] - Noite")
            print("[3] - Madrugada")
            print("[0] - Sair")
            horario_opcao = input("Digite 1, 2 ou 3: ")

            if horario_opcao == "0":
                print("Finalizando o programa!")
                return

            horarios = {"1": "Dia", "2": "Noite", "3": "Madrugada"}
            horario = horarios.get(horario_opcao, None)

            if not horario:
                print("Horário inválido. Reinicie o programa e tente novamente.")
                continue
            break

        print('='*20)

        # Tempo de espera antes do spawn
        tempo_espera = 5
        print(f"Aguarde {tempo_espera} segundos...")
        time.sleep(tempo_espera)

        # Lógica de Spawn
        monstro_apareceu, raridade = escolher_monstro(regiao, local, horario)

        print('='*30)
        if monstro_apareceu:
            # Pega a cor correspondente à raridade, ou usa a cor padrão (reset)
            cor = cores_raridade.get(raridade, "\033[0m")
            print(f"Um {cor}{monstro_apareceu}\033[0m "
            f"({raridade}) apareceu na {nome_local} de {nome_regiao} durante a {horario}!")
        else:
            print("Nada apareceu dessa vez...") # Nada apareceu, pois as chances somadas eram 0 ou a roleta não parou em um monstro válido.
        print('='*30)

if __name__ == "__main__":
    executar() 