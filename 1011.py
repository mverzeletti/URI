# -*- coding: utf-8 -*-

def main():
    raio = float(input())
    pi = 3.14159
    volume = (4 / 3) * pi * (round(raio, 2) ** 3)

    print('VOLUME = {0:.3f}'.format(volume))


if __name__ == "__main__":
    main()