import os

def limpar():
    os.system("clear")  # Linux
    # os.system("cls")  # Windows

def escolha(pergunta):

    while True:
        entrada = input(pergunta)

        if entrada == "0":
            print("\nFinalizando o programa!")
            return None
        try:
            valor = int(entrada)

            if valor < 0:
                print("\nDigite um valor válido.\n")
                continue

            return valor

        except ValueError:
            print("\nDigite apenas números.\n")


def executar():
    limpar()
    print('Olá, vamos fazer os devidos cálculos dos ATRIBUTOS do seu personagem!\nDigite [0] a qualquer momento para sair')

    while True:

        print('\n=== \33[34mINTELIGÊNCIA\33[0m ===')
        I = escolha("Me diga a sua INTELIGÊNCIA\nDigite aqui: ")

        if I is None:
            return

        print('\n=== \33[34mCARISMA\33[0m ===')
        Ca = escolha('Agora o CARISMA?\nDigite aqui: ')

        if Ca is None:
            return

        print('\n=== \33[34mFORÇA\33[0m ===')
        F = escolha('Sobre a FORÇA?\nDigite aqui: ')

        if F is None:
            return

        print('\n=== \33[34mAGILIDADE\33[0m ===')
        A = escolha('Me diga agora a sua AGILIDADE?\nDigite aqui: ')

        if A is None:
            return

        print('\n=== \33[34mCONSTITUIÇÃO\33[0m ===')
        Co = escolha('Por último, sobre sua CONSTITUIÇÃO?\nDigite aqui: ')

        if Co is None:
            return

        print('\n=== \33[34mNÍVEL\33[0m ===')
        nivel = escolha('Agora, me diga o seu NÍVEL: ')

        if nivel is None:
            return

        N = nivel - 1

        mana = 20 + 5 * (I + Ca) + (10 * N)
        vida = 20 + (5 * Co) + (5 * N)
        stamina = 20 + 5 * (A + F) + (10 * N)
        Fr = 100 + ((I // 5) * 5 + (Ca // 5) * 5)

        rf = Co + F * 2
        rm = Co + I

        m = 3 + A
        am = 4 + I
        af = 1

        print("\n===== \33[1;96mRESULTADO\33[0m =====")

        print(f"\n\33[36mMana\33[0m: \33[32m{mana}\33[0m")
        print(f"\33[36mVida\33[0m: \33[32m{vida}\33[0m")
        print(f"\33[36mStamina\33[0m: \33[32m{stamina}\33[0m")
        print(f"\33[36mFio de Razão\33[0m: \33[32m{Fr}%\33[0m")

        print(f"\n\33[36mResistência Física\33[0m: \33[32m{rf}\33[0m")
        print(f"\33[36mResistência Mágica\33[0m: \33[32m{rm}\33[0m")

        print(f"\n\33[36mMovimentação\33[0m: \33[32m{m}\33[0m")
        print(f"\33[36mAlcance Mágico\33[0m: \33[32m{am}\33[0m")
        print(f"\33[36mAlcance Físico\33[0m: \33[32m{af}\33[0m")

        continuar = input(
            "\nDeseja calcular novamente? (s/n): "
        ).lower()

        if continuar != "s":
            limpar()
            break

if __name__ == "__main__":
    executar() 
