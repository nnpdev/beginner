def demand():
    print("Vui lòng chọn 1 trong 2 chế độ sau:")
    print("1. Tính tổng của một dãy số tuần hoàn", "\n2. Tính tích của một dãy số tuần hoàn")
    print("------")
print(demand())
def tong(a,b,c):
    s = 0
    for i in range(a,b+1,c):
        s += i
    return s

def tich(a,b,c):
    s = 1
    for i in range(a,b+1,c):
        s *= i
    return s
try:
    mode = int(input("Bạn chọn chế độ: "))
    if mode == 1:
        a, b, c = map(int, input("Nhập 3 số a,b,c lần lượt là số bắt đầu, số kết thúc và bước nhảy: ").split())
        result = tong(a,b,c)
        print("Tổng của dãy số là: ",result)
    elif mode == 2:
        a, b, c = map(int, input("Nhập 3 số a,b,c lần lượt là số bắt đầu, số kết thúc và bước nhảy: ").split())
        result = tich(a,b,c)
        print("Tích của dãy số là: ",result)
except:
    print("Lỗi định dạng!")
    print(demand())