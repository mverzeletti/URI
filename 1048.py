salario = float(input())

if salario > 0 and salario <= 400:
    reajuste = 0.15

elif salario <= 800:
    reajuste = 0.12

elif salario <= 1200:
    reajuste = 0.1

elif salario <= 2000:
    reajuste = 0.07

else:
    reajuste = 0.04

novo_salario = salario * (1 + reajuste)
ganho = salario * reajuste

print("Novo salario: {:.2f}".format(novo_salario))
print("Reajuste ganho: {:.2f}".format(ganho))
print("Em percentual: {:.0f} %".format(reajuste * 100))