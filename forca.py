from operator import index


def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        
        chute = input("Qual Letra?")
        chute = chute.strip()
        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("Encontrei  a letra {} na posição {}".format(letra, index))
            index = index + 1

        print("jogando...")

    print("Fim de Jogo")

if(__name__ == "__main__"):
    jogar()

