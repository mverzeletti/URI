# -*- coding: utf-8 -*-

def main():
    distancia = int(input())
    combustivel = float(input())
    combustivel = round(combustivel, 1)
    consumo = distancia / combustivel

    print('{0:.3f}'.format(consumo)+' km/l')


if __name__ == "__main__":
    main()