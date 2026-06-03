## CÓDIGO PARA SISTEMA DE SPAWN DE MONSTROS ##

import random
import time

# Definir as cores para cada raridade (ANSI escape codes)
cores_raridade = {
    "Comum": "\033[32m",    # Verde
    "Incomum": "\033[33m",  # Amarela
    "Raro": "\033[31m",      # Vermelho
    "Épico": "\033[35m",    # Roxo/Magenta
    "Mítico": "\033[36m",   # Ciano
    "Calamidade": "\033[35m" # Magenta
}

# Definição das regiões, locais e monstros com chances de spawn por horário
regioes = {
    "1": {  # Askelon
        "nome": "Askelon",
        "locais": {
            "1": {"nome": "Floresta Densa", "monstros": {
                "Gambá": {"raridade": "Comum", "Dia": 60, "Noite": 60, "Madrugada": 60},
                "Morcego Gigante": {"raridade": "Incomum", "Dia": 0, "Noite": 25, "Madrugada": 25},
                "Asa-Assasina": {"raridade": "Incomum", "Dia": 25, "Noite": 25, "Madrugada": 25},
                "Rato Gigante": {"raridade": "Incomum", "Dia": 25, "Noite": 25, "Madrugada": 25},
                "Rei dos Ratos (Elite)": {"raridade": "Raro", "Dia": 10, "Noite": 10, "Madrugada": 10},
                "Bandido": {"raridade": "Incomum", "Dia": 25, "Noite": 25, "Madrugada": 25}
            }},
            "2": {"nome": "Província", "monstros": {
                "Gambá": {"raridade": "Comum", "Dia": 60, "Noite": 60, "Madrugada": 60},
                "Lobo": {"raridade": "Incomum", "Dia": 25, "Noite": 25, "Madrugada": 25},
                "Bandido": {"raridade": "Incomum", "Dia": 25, "Noite": 25, "Madrugada": 25},
                "Rato Gigante": {"raridade": "Incomum", "Dia": 25, "Noite": 25, "Madrugada": 25},
                "Rei dos Ratos (Elite)": {"raridade": "Raro", "Dia": 10, "Noite": 10, "Madrugada": 10},
            }},
            "3": {"nome": "Caverna da Floresta Densa", "monstros": {
                "Morcego Gigante": {"raridade": "Incomum", "Dia": 0, "Noite": 25, "Madrugada": 25},
                "Aranha gigante": {"raridade": "Incomum", "Dia": 25, "Noite": 25, "Madrugada": 25},
                "Aranha gigante (Elite)": {"raridade": "Raro", "Dia": 10, "Noite": 10, "Madrugada": 10},
                "Morcego gigante": {"raridade": "Incomum", "Dia": 25, "Noite": 25, "Madrugada": 25},
                "Rato Gigante": {"raridade": "Incomum", "Dia": 25, "Noite": 25, "Madrugada": 25},
                "Rei dos Ratos (Elite)": {"raridade": "Raro", "Dia": 10, "Noite": 10, "Madrugada": 10},
            }}
        }
    },
    "2": {  # Netanya
        "nome": "Netanya",
        "locais": {
            "1": {"nome": "Floresta Temperada", "monstros": {
                "Esquilo": {"raridade": "Comum", "Dia": 35, "Noite": 25, "Madrugada": 0},
                 "Corvo": {"raridade": "Comum", "Dia": 35, "Noite": 25, "Madrugada": 25},
                "Coelho": {"raridade": "Comum", "Dia": 35, "Noite": 25, "Madrugada": 0},
                "Urso Pardo": {"raridade": "Incomum", "Dia": 25, "Noite": 25, "Madrugada": 25},
                "Urso Colossal": {"raridade": "Épico", "Dia": 4, "Noite": 4, "Madrugada": 4}
            }},
            "2": {"nome": "Área Sul", "monstros": {
                "Esquilo": {"raridade": "Comum", "Dia": 35, "Noite": 25, "Madrugada": 0},
                "Coelho": {"raridade": "Comum", "Dia": 35, "Noite": 25, "Madrugada": 0},
                "Raposa": {"raridade": "Comum", "Dia": 40, "Noite": 45, "Madrugada": 30},
                "Lobo": {"raridade": "Incomum", "Dia": 25, "Noite": 35, "Madrugada": 40},
                "Javalin Impetuoso": {"raridade": "Incomum", "Dia": 30, "Noite": 30, "Madrugada": 30},
                "Matilha de Gatos": {"raridade": "Incomum", "Dia": 35, "Noite": 30, "Madrugada": 30},
                "Gambá Peçonhento": {"raridade": "Incomum", "Dia": 35, "Noite": 30, "Madrugada": 30},
                "Falcão Críptico": {"raridade": "Incomum", "Dia": 35, "Noite": 25, "Madrugada": 25},
                "Zevantes": {"raridade": "Raro", "Dia": 10, "Noite": 10, "Madrugada": 10},
            }},
            "3": {"nome": "Arredores do Cedro Ancestral", "monstros": {
                "Esquilo": {"raridade": "Comum", "Dia": 40, "Noite": 40, "Madrugada": 0},
                "Coelho": {"raridade": "Comum", "Dia": 40, "Noite": 40, "Madrugada": 0},
                "Raposa Escarlate": {"raridade": "Incomum", "Dia": 35, "Noite": 30, "Madrugada": 25},
                "Espírito Verdejante": {"raridade": "Incomum", "Dia": 30, "Noite": 30, "Madrugada": 30},
                "Zevantes": {"raridade": "Raro", "Dia": 10, "Noite": 10, "Madrugada": 10},
                "Avatar do Cedro Ancestral": {"raridade": "Épico", "Dia": 4, "Noite": 4, "Madrugada": 4}
            }},
            "4": {"nome": "Área Norte", "monstros": {
                "Esquilo": {"raridade": "Comum", "Dia": 30, "Noite": 30, "Madrugada": 30},
                "Coelho": {"raridade": "Comum", "Dia": 30, "Noite": 30, "Madrugada": 30},
                "Raposa": {"raridade": "Comum", "Dia": 30, "Noite": 35, "Madrugada": 30},
                "Javelin Alabarda": {"raridade": "Incomum", "Dia": 30, "Noite": 30, "Madrugada": 30},
                "Raposa Branca": {"raridade": "Incomum", "Dia": 30, "Noite": 35, "Madrugada": 30},
                "Gambá Friento": {"raridade": "Incomum", "Dia": 30, "Noite": 30, "Madrugada": 30},
                "Zevantes": {"raridade": "Raro", "Dia": 10, "Noite": 10, "Madrugada": 10},
                "Harpia de Brumas Gélidas": {"raridade": "Raro", "Dia": 15, "Noite": 15, "Madrugada": 15},
                "Urso Colossal": {"raridade": "Épico", "Dia": 5, "Noite": 5, "Madrugada": 5}

            }}
        }
    },
    "3": {  # Bayovia
        "nome": "Bayovia",
        "locais": {
            "1": {"nome": "Portões de Beloozero", "monstros": {
                "Coelho": {"raridade": "Comum", "Dia": 35, "Noite": 25, "Madrugada": 0},
                "Esquilo": {"raridade": "Comum", "Dia": 35, "Noite": 25, "Madrugada": 0},
                "Raposa Branca": {"raridade": "Incomum", "Dia": 30, "Noite": 35, "Madrugada": 30},
                "Gambá Friento": {"raridade": "Incomum", "Dia": 30, "Noite": 30, "Madrugada": 30},
                "Harpia de Brumas Gélidas": {"raridade": "Raro", "Dia": 15, "Noite": 15, "Madrugada": 15},
                "Gigante Glacial": {"raridade": "Épico", "Dia": 5, "Noite": 5, "Madrugada": 5}
            }},
            "2": {"nome": "Tundra", "monstros": {
                "Coelho": {"raridade": "Comum", "Dia": 40, "Noite": 40, "Madrugada": 0},
                "Esquilo": {"raridade": "Comum", "Dia": 35, "Noite": 25, "Madrugada": 0},
                "Raposa Branca": {"raridade": "Incomum", "Dia": 30, "Noite": 35, "Madrugada": 35},
                "Gambá Friento": {"raridade": "Incomum", "Dia": 30, "Noite": 30, "Madrugada": 30},
                "Grolok Almiscarado": {"raridade": "Incomum", "Dia": 40, "Noite": 25, "Madrugada": 25},
                "Corvo Gélido": {"raridade": "Incomum", "Dia": 30, "Noite": 30, "Madrugada": 30},
                "Coruja Nebulosa": {"raridade": "Incomum", "Dia": 16, "Noite": 35, "Madrugada": 35},
                "Sneegk": {"raridade": "Incomum", "Dia": 35, "Noite": 30, "Madrugada": 30},
                "Urso Das Neves": {"raridade": "Incomum", "Dia": 35, "Noite": 30, "Madrugada": 20},
                "Harpia de Brumas Gélidas": {"raridade": "Raro", "Dia": 15, "Noite": 15, "Madrugada": 15},
                "Gigante Glacial": {"raridade": "Épico", "Dia": 3, "Noite": 3, "Madrugada": 3}
            }},
            "3": {"nome": "Caminho dos Ecos Distorcidos", "monstros": {
                "Espectro Congelado": {"raridade": "Incomum", "Dia": 0, "Noite": 40, "Madrugada": 40},
                "Carcaça Congelada": {"raridade": "Incomum", "Dia": 0, "Noite": 35, "Madrugada": 35},
                "Ghoul de Gelo": {"raridade": "Incomum", "Dia": 0, "Noite": 30, "Madrugada": 30},
                "Fantasma Desesperado": {"raridade": "Incomum", "Dia": 0, "Noite": 25, "Madrugada": 25},
                "Necro-Amálgama": {"raridade": "Raro", "Dia": 0, "Noite": 10, "Madrugada": 14},
                "Cavalaria Espectral e Bakotsu": {"raridade": "Épico", "Dia": 0, "Noite": 4, "Madrugada": 7}


            }},
            "4": {"nome": "Tundra Congelada", "monstros": {
                "Esquilo": {"raridade": "Comum", "Dia": 30, "Noite": 30, "Madrugada": 30},
                "Coelho": {"raridade": "Comum", "Dia": 30, "Noite": 30, "Madrugada": 30},
                "Raposa": {"raridade": "Comum", "Dia": 30, "Noite": 35, "Madrugada": 30},
                "Javelin Alabarda": {"raridade": "Incomum", "Dia": 30, "Noite": 30, "Madrugada": 30},
                "Raposa Branca": {"raridade": "Incomum", "Dia": 30, "Noite": 35, "Madrugada": 30},
                "Gambá Friento": {"raridade": "Incomum", "Dia": 30, "Noite": 30, "Madrugada": 30},
                "Zevantes": {"raridade": "Raro", "Dia": 10, "Noite": 10, "Madrugada": 10},
                "Harpia de Brumas Gélidas": {"raridade": "Raro", "Dia": 15, "Noite": 15, "Madrugada": 15},
                "Urso Colossal": {"raridade": "Épico", "Dia": 5, "Noite": 5, "Madrugada": 5}

            }},
            "5": {"nome": "Floresta de Coniferas", "monstros": {
                "Esquilo": {"raridade": "Comum", "Dia": 30, "Noite": 30, "Madrugada": 30},
                "Coelho": {"raridade": "Comum", "Dia": 30, "Noite": 30, "Madrugada": 30},
                "Raposa": {"raridade": "Comum", "Dia": 30, "Noite": 35, "Madrugada": 30},
                "Javelin Alabarda": {"raridade": "Incomum", "Dia": 30, "Noite": 30, "Madrugada": 30},
                "Raposa Branca": {"raridade": "Incomum", "Dia": 30, "Noite": 35, "Madrugada": 30},
                "Gambá Friento": {"raridade": "Incomum", "Dia": 30, "Noite": 30, "Madrugada": 30},
                "Zevantes": {"raridade": "Raro", "Dia": 10, "Noite": 10, "Madrugada": 10},
                "Harpia de Brumas Gélidas": {"raridade": "Raro", "Dia": 15, "Noite": 15, "Madrugada": 15},
                "Urso Colossal": {"raridade": "Épico", "Dia": 5, "Noite": 5, "Madrugada": 5}


            }}
        }
    },
    "4": {  # Cavernas Profundas
        "nome": "Cavernas Profundas",
        "locais": {
            "1": {"nome": "Garganta Congelada", "monstros": {
                "Morcego de Cristal": {"raridade": "Comum", "Dia": 45, "Noite": 45, "Madrugada": 45},
                "Verme de Gelo": {"raridade": "Incomum", "Dia": 30, "Noite": 30, "Madrugada": 25},

            }},
            "2": {"nome": "Veias de Tugstênio", "monstros": {
                "Lagarto de Tugstênio": {"raridade": "Incomum", "Dia": 30, "Noite": 30, "Madrugada": 30},
                "Aranha de Vapor": {"raridade": "Incomum", "Dia": 25, "Noite": 35, "Madrugada": 30},
                "Escorpião de Tugstênio": {"raridade": "Incomum", "Dia": 30, "Noite": 30, "Madrugada": 30},
                "Gosma de Vapor": {"raridade": "Incomum", "Dia": 30, "Noite": 30, "Madrugada": 30},
                "Wyrm Filhote": {"raridade": "Incomum", "Dia": 20, "Noite": 20, "Madrugada": 20},

            }},
            "3": {"nome": "Câmara de Lava", "monstros": {
                "Larva de Lava": {"raridade": "Incomum", "Dia": 30, "Noite": 30, "Madrugada": 30},
                "Wyrm Filhote": {"raridade": "Incomum", "Dia": 27, "Noite": 27, "Madrugada": 27},
                "Wyrm Jovem": {"raridade": "Incomum", "Dia": 18, "Noite": 18, "Madrugada": 18},
                "Wyrm Adulto": {"raridade": "Raro", "Dia": 12, "Noite": 12, "Madrugada": 12},
                "Titã de Lava": {"raridade": "Raro", "Dia": 12, "Noite": 12, "Madrugada": 12},
                "Elemental de Lava": {"raridade": "Épico", "Dia": 7, "Noite": 7, "Madrugada": 7},
                "O Coração Vivo": {"raridade": "Épico", "Dia": 2, "Noite": 2, "Madrugada": 2},


            }}
        }
    },
    "5": {  # Praias
        "nome": "Praias",
        "locais": {
            "1": {"nome": "Heliya", "monstros": {
                "Côco-Ranguejo": {"raridade": "Incomum", "Dia": 35, "Noite": 30, "Madrugada": 25},
                "Cefalópode-Terrestre": {"raridade": "Incomum", "Dia": 30, "Noite": 30, "Madrugada": 25},
                "Aguareia-Viva": {"raridade": "Incomum", "Dia": 30, "Noite": 30, "Madrugada": 25},
                "Quelante-de-Cristais": {"raridade": "Raro", "Dia": 12, "Noite": 12, "Madrugada": 12},
                "Karkinos": {"raridade": "Épico", "Dia": 5, "Noite": 5, "Madrugada": 5},
            }}
        }
    }
}


def escolher_monstro(regiao, local, horario):
    """Escolhe um monstro baseado na região, local e horário usando roleta de chances."""

    # 1. Verifica se a combinação é válida
    if regiao not in regioes or local not in regioes[regiao]["locais"] or horario not in ["Dia", "Noite", "Madrugada"]:
        return None, None

    chances_monstros = regioes[regiao]["locais"][local]["monstros"]

    # Extrai os nomes dos monstros e suas chances para o horário escolhido
    monstros = list(chances_monstros.keys())
    # O valor de chance é obtido usando dados[horario], que é a chave 'Dia', 'Noite' ou 'Madrugada'
    pesos = [dados[horario] for dados in chances_monstros.values()]

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
    raridade = chances_monstros[monstro_escolhido]["raridade"]

    return monstro_escolhido, raridade

# Roleta para decidir se um monstro vai aparecer (80% de chance de "Sim")
aparece = random.choices(["Sim", "Não"], weights=[80, 20], k=1)[0]

if aparece == "Não":
    tempo_spawn = 3
    time.sleep(tempo_spawn)
    print("Nada apareceu dessa vez...")
else:
    # --- Interação com o Usuário para Escolha de Local ---

    # Escolha da região
    tempo_spawn = 5
    print("Aguarde 5 segundos...")
    time.sleep(tempo_spawn) # Espera antes de começar a interagir

    print("\nEscolha a região:")
    for num, info in regioes.items():
        print(f"{num} - {info['nome']}")
    regiao = input("Digite 1 ou 2: ")

    if regiao not in regioes:
        print("Região inválida. Reinicie o programa e tente novamente.")
        exit()

    nome_regiao = regioes[regiao]["nome"]
    print('='*20)

    # Escolha do local dentro da região
    print(f"Escolha o local dentro de {nome_regiao}:")
    for num, info in regioes[regiao]["locais"].items():
        print(f"{num} - {info['nome']}")
    local = input("Digite o número correspondente ao local: ")

    if local not in regioes[regiao]["locais"]:
        print("Local inválido. Reinicie o programa e tente novamente.")
        exit()

    nome_local = regioes[regiao]["locais"][local]["nome"]
    print('='*20)

    # Escolha do horário
    print("Escolha o horário:")
    print("1 - Dia")
    print("2 - Noite")
    print("3 - Madrugada")
    horario_opcao = input("Digite 1, 2 ou 3: ")

    horarios = {"1": "Dia", "2": "Noite", "3": "Madrugada"}
    horario = horarios.get(horario_opcao, None)

    if not horario:
        print("Horário inválido. Reinicie o programa e tente novamente.")
        exit()
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
        print(f"Um {cor}{monstro_apareceu}\033[0m apareceu na {nome_local} de {nome_regiao} durante a {horario}!")
    else:
         print("Nada apareceu dessa vez...") # Nada apareceu, pois as chances somadas eram 0 ou a roleta não parou em um monstro válido.
    print('='*30)