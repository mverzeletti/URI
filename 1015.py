# -*- coding: utf-8 -*-

def main():
    ponto1 = input()
    ponto2 = input()
    ponto1 = ponto1.split(' ')
    p1_x = float(ponto1[0])
    p1_y = float(ponto1[1]) 
    ponto2 = ponto2.split(' ')
    p2_x = float(ponto2[0])
    p2_y = float(ponto2[1]) 

    distancia = (((p2_x - p1_x) ** 2) + ((p2_y - p1_y) ** 2))  ** (0.5)

    print('{0:.4f}'.format(distancia))


if __name__ == "__main__":
    main()