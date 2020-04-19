valores = [int(i) for i in input().split(" ")]
ordem = sorted(valores)

if (ordem[1] % ordem[0]) == 0:
    print("Sao Multiplos")

else:
    print("Nao sao Multiplos")