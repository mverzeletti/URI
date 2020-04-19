lados = [float(i) for i in input().split(" ")]
ordenados = sorted(lados)

if (ordenados[0] + ordenados[1]) > ordenados[2]:
    print("Perimetro = {:.1f}".format(sum(lados)))

else:
    area = ((lados[0] + lados[1]) * lados[2]) / 2
    print("Area = {:.1f}".format(area))