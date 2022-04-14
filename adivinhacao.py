import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = int(random.randrange(1,101)) ## Pegar numero randomico de 1 a 100
    total_de_tentativas = 0
    pontos = 1000

    rodada = 1
    print("Qual nivel de dificuldade?")
    print("(1) Fácil (2) Médio (3) Díficil")

    nivel =  int(input("Defina um nível: "))
    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else: 
        total_de_tentativas = 5


    for rodada in range(1,total_de_tentativas + 1): 
        print("Tentativas {:02d} de {:02d}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100 : ")
        print("Você digitou:", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = (chute == numero_secreto)
        maior = (chute > numero_secreto)
        menor = (chute < numero_secreto)

        if (acertou):
            print("Parabens voce acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("voce errou! O seu chute foi maior do que o número secreto")
            elif (menor):
                print("voce errou! O seu chute foi menor do que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do Jogo!")
if(__name__ == "__main__"):
    jogar()