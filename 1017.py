# -*- coding: utf-8 -*-

def main():
    tempo = int(input())
    velocidade = int(input())
    media = 12
    distancia = tempo * velocidade
    consumo = distancia / media

    print('{0:.3f}'.format(consumo))


if __name__ == "__main__":
    main()