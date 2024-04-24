p = 10**9 + 7
n = int(input())
y = [int(x) for x in input().split()]
tich = 1
for x in y:
    tich = (tich * x) % p
print(tich)