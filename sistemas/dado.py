from random import randint
import re
import utils

def rolar(expressao):
    padrao = r"(\d*)d(\d+)([+-]\d+)?"

    resultado = re.fullmatch(padrao, expressao)

    if resultado is None:
        raise ValueError("Expressão inválida.")

    quantidade = int(resultado.group(1) or 1)
    lados = int(resultado.group(2))
    bonus = int(resultado.group(3) or 0)

    if quantidade <= 0:
        raise ValueError("A quantidade de dados deve ser maior que zero.")
    
    elif quantidade > 100:
        raise ValueError("Máximo de 100 dados!")

    if lados <= 0:
        raise ValueError("O número de lados deve ser maior que zero.")
    
    elif lados > 1000:
        raise ValueError("Máximo de 1000 dados!")

    valores = []

    for _ in range(quantidade):
        valores.append(randint(1, lados))

    soma = sum(valores)
    total = soma + bonus

    return {
        "quantidade": quantidade,
        "lados": lados,
        "dados": valores,
        "bonus": bonus,
        "soma": soma,
        "total": total
    }


def executar():
    while True:
        try:
            utils.menu_dado()
            expressao = (input("Digite a rolagem (0 para sair): ")).lower().replace(" ", "")        

            if expressao == "0":
                print("\nFinalizando o programa!")
                return

            resultado = rolar(expressao)

            print("\nRolando os dados", end="", flush=True)
            utils.anima_carregando()

            print(f"\n\033[32mRolagem\033[0m: {expressao}")
            print(f"\033[32mDados\033[0m: {resultado['dados']}")
            print(f"\033[32mSoma\033[0m: {sum(resultado['dados'])}")

            if resultado["bonus"] != 0:
                print(f"\033[32mBônus\033[0m: {resultado['bonus']:+}")

            print(f"\033[32mTotal\033[0m: \033[31m{resultado['total']}\033[0m")

            print("=" * 30)

            if not utils.sn ("Deseja calcular novamente?"):
                return

        except ValueError:
            print("\nExpressão inválida.")
            print("Exemplos válidos:")
            print("  d20")
            print("  2d6")
            print("  3d8+4")
            print("  1d100-10")

            try:
                input("\nPressione ENTER para continuar...")
            except (ValueError, EOFError, KeyboardInterrupt):
                print ("\n\nProgrma encerrado.")
                break
            continue

        except (KeyboardInterrupt, EOFError):
            print("\n\nPrograma encerrado.")
            break

if __name__ == "__main__":
    executar()