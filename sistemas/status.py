def escolha(pergunta):

    while True:
        try:
            valor = int(input(pergunta))

            if valor < 0:
                print("\nDigite um valor válido.\n")
                continue

            return valor

        except ValueError:
            print("\nDigite apenas números.\n")


def executar():

    print('Olá, vamos fazer os devidos cálculos dos ATRIBUTOS do seu personagem!\n')

    while True:

        print('\n=== INTELIGÊNCIA ===')
        I = escolha("Me diga a sua INTELIGÊNCIA\nDigite aqui: ")

        print('\n=== CARISMA ===')
        Ca = escolha('Agora o CARISMA?\nDigite aqui: ')

        print('\n=== FORÇA ===')
        F = escolha('Sobre a FORÇA?\nDigite aqui: ')

        print('\n=== AGILIDADE ===')
        A = escolha('Me diga agora a sua AGILIDADE?\nDigite aqui: ')

        print('\n=== CONSTITUIÇÃO ===')
        Co = escolha('Por último, sobre sua CONSTITUIÇÃO?\nDigite aqui: ')

        print('\n=== NÍVEL ===')
        nivel = escolha('Agora, me diga o seu NÍVEL: ')

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

        print("\n===== RESULTADO =====")

        print(f"Mana: {mana}")
        print(f"Vida: {vida}")
        print(f"Stamina: {stamina}")
        print(f"Fio de Razão: {Fr}%")

        print(f"\nResistência Física: {rf}")
        print(f"Resistência Mágica: {rm}")

        print(f"\nMovimentação: {m}")
        print(f"Alcance Mágico: {am}")
        print(f"Alcance Físico: {af}")

        continuar = input(
            "\nDeseja calcular novamente? (s/n): "
        ).lower()

        if continuar != "s":
            break