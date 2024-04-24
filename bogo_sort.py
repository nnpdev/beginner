import random
import time
def is_sorted(lst):
    """
    Kiểm tra xem một danh sách đã được sắp xếp hay chưa.
    """
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

def bogo_sort(lst):
    """
    Sắp xếp danh sách bằng thuật toán Bogo Sort.
    """
    while not is_sorted(lst):
        random.shuffle(lst)
    return lst
# Ví dụ sử dụng:
my_list = [i for i in range(20)]
my_list += [1]
print("Danh sách trước khi sắp xếp:", my_list)
start_time = time.time()
sorted_list = bogo_sort(my_list)
print("Danh sách sau khi sắp xếp:", sorted_list)
end_time = time.time()
print(end_time - start_time)
