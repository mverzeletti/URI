# -*- coding: utf-8 -*-

def main():
    distancia = int(input())
    velocidade1 = 60
    velocidade2 = 90
    diferenca_hora = abs(velocidade1 - velocidade2)
    diferenca_minuto = diferenca_hora / 60
    tempo_minutos = int(distancia / diferenca_minuto)

    print(str(tempo_minutos)+' minutos')


if __name__ == "__main__":
    main()