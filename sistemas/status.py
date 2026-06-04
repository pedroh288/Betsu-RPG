def executar():
    while True:
        print("\n=== STATUS ===")

        voltar = input("Voltar? (s/n):").lower

        if voltar == "s":
             break
        
# Introdução:
print('Olá, vamos fazer os devidos cálculos dos \33[33mATRIBUTOS\33[0m do seu personagem!\n')

def escolha(pergunta):

    while True:
            try:
                 valor = int(input(pergunta))

                 if valor <0:
                      print("\n Digite um valor válido (maior que zero).\n")
                      continue
                 return valor
            except ValueError:
                 print("\n Digite apenas números!\n")

while True:
    print('\n===\33[1;95mINTELIGÊNCIA\33[0m===')
    I = escolha("Me diga a sua INTELIGÊNCIA\nDigite aqui: ")

    print('\n===\33[1;95mCARISMA\33[0m===')
    Ca = escolha('Agora o CARISMA?\nDigite aqui: ')

    print('\n===\33[1;95mFORÇA\33[0m===')
    F = escolha('Sobre a FORÇA?\nDigite aqui: ')
    
    print('\n===\33[1;95mAGILIDADE\33[0m===')
    A = escolha('Me diga agora a sua AGILIDADE?\nDigite aqui: ')

    print('\n===\33[1;95mCONSTITUIÇÃo\33[0m===')
    Co = escolha('Por último, sobre sua CONSTITUIÇÃO?\nDigite aqui: ')

    print('\n===\33[1;95mNÍVEL\33[0m===')
    nivel = escolha('Agora, me diga o seu NÍVEL (começando do nível 1): ')

    #Cálculo dos atributos, resistências, movimentação, etc:
    print('\nVamos calcular os seus \033[34mstatus\033[0m agora: \n')

    N = nivel - 1

    mana = 20 + 5 * (I + Ca) + (10 * N) #20 + 5 x I e Ca
    vida = 20 + (5 * Co) + (5 * N) #20 + 5 x Co
    stamina = 20 + 5 * (A + F) + (10 * N) #20 + 5 x A e F
    Fr = 100 + ((I // 5) * 5 + (Ca // 5) * 5) # Base 100% e aumenta em 5% a cada 5 pontos em inteligência ou carisma.

    rf = Co + F * 2
    rm = Co + I

    m = 3 + A
    am = 4 + I
    af = 1

    # Entrega dos resultados:
    print('='*20)

    print('Sua \33[36mMANA\33[0m inicial é: \033[32m{}\033[0m'.format(mana))
    print('Sua \33[36mVIDA\33[0m inicial: \033[32m{}\033[0m'.format(vida))
    print('Sua \33[36mSTAMINA\33[0m é: \033[32m{}\033[0m'.format(stamina))
    print('Seu \33[36mFIO DE RAZÃO\33[0m é \033[32m{}%\033[0m'.format(Fr))

    print('='*20)

    print('\nAgora sobre suas \033[34mresistência\033[0m...')

    print('='*20)

    print('Sua \033[36mRESISTÊNCIA FÍSICA\033[0m é: \033[32m{}\033[0m'.format(rf))
    print('Sua \033[36mRESISTÊNCIA MÁGICA\33[0m é: \033[32m{}\033[0m'.format(rm))


    print('\nAgora sobre sobre os \033[34malcances\033[0m...')

    print('='*20)

    print('Sua \33[36mMOVIMENTAÇÃO\33[0m é: \033[32m{}\033[0m'.format(m))
    print('Seu \33[36mALCANCE MÁGICO\33[0m é: \033[32m{}\033[0m'. format(am))
    print('Seu \33[36mALCANCE FÍSICO\33[0m é: \033[32m{}\033[0m'.format(af))

    print('='*20)

    continuar = input("\nDeseja calcular novamente? (s/n): ").lower()

    if continuar != "s":
        print('\nPrograma encerrado.')
        break