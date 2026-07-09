## CÓDIGO PARA SISTEMA DE SPAWN DE MONSTROS ##

import random
import time
import os
import json
import utils

def executar():
    while True:
        utils.menu_spawn()
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

            if not utils.sn ("Deseja fazer um novo spawn de ininmigo?"):
                return
            continue
        else:

            # --- Interação com o Usuário para Escolha de Reino ---

            reino = utils.escolher_opcao(
                lista_regioes,
                "Reino"
            )

            if reino is None:
                return

            nome_reino = reino

            # Escolha do local dentro da região
            lista_locais = list(regioes[reino].keys())

            regiao = utils.escolher_opcao(
                lista_locais,
                f"Região de {nome_reino}"
            )

            if regiao is None:
                return

            nome_regiao = regiao


        # Escolha do horário

            horario = utils.escolher_opcao(
            ["Dia", "Noite", "Madrugada"],
            "Horário"
        )

            if horario is None:
                return

            print()
            print('='*20)

            print("Carregando inimigo", end="", flush=True)
            utils.anima_carregando()

            # Lógica de Spawn
            monstro_apareceu, raridade = escolher_monstro(
                reino,
                regiao,
                horario
            )

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

            if not utils.sn ("Deseja fazer um novo spawn de ininmigo?"):
                return
        
            
if __name__ == "__main__":
    executar() 