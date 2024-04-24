import math as m
def ptb1(a,b):
    if a == 0:
        if b == 0:
            return "Phương trình có vô số nghiệm"
        return "Phương trình vô nghiệm"
    return "Phương trình có một nghiệm duy nhất: x = {}".format(-b/a)
def ptb2(a,b,c):
    d = b*b - 4*a*c
    if d < 0:
        return "Phương trình vô nghiệm"
    elif a == 0:
        return ptb1
    elif d == 0:
        return "Phương trình có 2 nghiệm kép x1 = x2 = {}".format(-b/2*a)
    else:
        x1 = (-b - m.sqrt(d)/2*a)
        x2 = (-b + m.sqrt(d)/2*a)
        return "Phương trình có 2 nghiệm phân biệt lận lượt là: \nx1 = {} \nx2 = {}".format(x1, x2)

def error():
    print("Vui lòng chọn một trong hai chức năng: ")
    print("1. Giải phương trình bậc nhất có dạng ax + b = 0", "\n2. Giải phương trình bậc hai có dạng ax^2 + bx + c = 0")
print(error())   
try:
    mode = int(input("Chọn mode: "))
    if mode == 1:
        print("Bạn chọn giải phương trình bậc nhất")
        a, b = map(float, input("Hệ số a, b lần lượt là: ").split())
        print(ptb1(a, b))
    else:
        print("Bạn chọn giải phương trình bậc hai")
        a, b, c = map(float, input("Hệ số a, b, c lần lượt là: ").split())
        print(ptb2(a ,b ,c))
except:
    print(error())
        