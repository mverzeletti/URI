n = int(input())
h = int(n / 60 ** 2)
m = int((n - (h * 60 ** 2)) / 60)
s = n - (h * 60 ** 2) - (m * 60)

print('{}:{}:{}'.format(h,m,s))