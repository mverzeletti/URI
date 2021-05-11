renda = float(input())

if renda <= 2000:

    print("Isento")

elif renda > 2000 and renda <= 3000:

    print("R$ {:.2f}".format((renda - 2000) * 0.08))

elif renda > 3000 and renda <= 4500:

    print("R$ {:.2f}".format((3000 - 2000) * 0.08 + (renda - 3000) * 0.18))

else:

    print("R$ {:.2f}".format((3000 - 2000) * 0.08 + (4500 - 3000) * 0.18 + (renda - 4500) * 0.28))