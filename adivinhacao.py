print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite o seu Numero : ")

print("Você digitou:", chute_str)

chute = int(chute_str)

acertou = (chute == numero_secreto)
maior = (chute > numero_secreto)
menor = (chute < numero_secreto)

if acertou:
    print("Parabens voce acertou!")
else:
    if maior:
        print("voce errou! O seu chute foi maior do que o número secreto")
    elif menor:
        print("voce errou! O seu chute foi menor do que o número secreto")

print("Fim do Jogo!")