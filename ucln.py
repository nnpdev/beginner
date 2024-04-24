a,b = map(int,input("Nhập vào hai số tự nhiên: ").split())
while b != 0:
    num = a
    a = b
    b = num%b
print(a)