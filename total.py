list_num = [float(x) for x in input("Nhập các số thực (cách nhau bởi dấu cách): ").split()]
total = 0
for num in list_num:
    total += num
print(total)