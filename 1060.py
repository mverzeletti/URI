dados = []
dados.append(float(input()))
dados.append(float(input()))
dados.append(float(input()))
dados.append(float(input()))
dados.append(float(input()))
dados.append(float(input()))

n = 0

for i in dados:

    if i > 0:

        n = n + 1

print("{} valores positivos".format(n))