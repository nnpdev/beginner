p = 10**9 + 7
n = int(input())
y =[int(x) for x in input().split()]
sum = 0
for x in y:
    sum = x%p + sum
sum = sum%p
print(sum)