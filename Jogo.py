import random
from logging import exception


class jogoadivinhacao:
    def __init__(self):
        self.__numero_secretro = random.randint(1, 100)
        self.__tentativas = 0

    def jogar(self):
        print('Bem vindo ao jogo de adivinhação')
        print('tente adivinhar o numero entre 1 e 100.\n')

        while True:
            try:
                palpite = int(input('Digite um numero'))
                self.__tentativas += 1

                if palpite < self.__numero_secretro:
                    print('Muito baixo')
                elif palpite > self.__numero_secretro:
                    print('Muito alto')
                else:
                    print(f'Você acertou em {self.__tentativas} tentativas.')
                    break
            except ValueError:
                print('Digite um numero valido')

jogo = jogoadivinhacao()
jogo.jogar()
