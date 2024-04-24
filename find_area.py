import math
def area(a,b,c):
    if a <= 0 or b <= 0 or c <= 0 or not (a+b>c and a+c>b and b+c>a):
        return False
    p = (a+b+c)/2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return s
t,v,u = map(float, input("Nhập độ dài ba cạnh của tam giác thứ nhất: ").split())
x,y,z = map(float, input("Nhập độ dài ba cạnh của tam giác thứ hai: ").split())
m,q,r = map(float, input("Nhập độ dài ba cạnh của tam giác thứ ba: ").split())

tg1 = area(t,v,u) 
tg2 = area(x,y,z) 
tg3 = area(m,q,r) 
def find_max(x,y,z):
    max = x
    if y > max:
        max = y
    if z > max:
        max = z
    return max
max_area = find_max(tg1,tg2,tg3)

print("Diện tích tam giác 1 là: ", tg1)
print("Diện tích tam giác 2 là: ", tg2)
print("Diện tích tam giác 3 là: ", tg3)
print("Diện tích tam giác lớn nhất là: ", max_area)
