def inteiro(a, b):

    return int(a/b)

def resto(a, b):

    return(a % b)

dias = int(input())
anos = inteiro(dias, 365)
dias = resto(dias, 365)
meses = inteiro(dias, 30)
dias = resto(dias, 30)

print(str(anos)+' ano(s)')
print(str(meses)+' mes(es)')
print(str(dias)+' dia(s)')