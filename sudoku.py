import time
def is_valid(bo, num, x, y):
    #Kiểm tra hàng, cột (all board) 
    #nếu có số nào trùng với số nhập vào -> false
    for i in range(9):
        if bo[x][i] == num :
            return False
        if bo[i][y] == num:
            return False
    #Kiểm tra box 3x3  
    #Mỗi một box nhỏ có tọa độ (x,y) | x,y thuộc 0->2
    #Tọa độ gốc là điểm trên cùng bên trái của board
    start_box_x = (x // 3)*3 #Tọa độ gốc của một điểm nằm trong box 3x3
    start_box_y = (y // 3)*3
    for i in range(3):
        for j in range(3):
            if bo[start_box_x + i][start_box_y + j] == num: #Duyệt qua từng ô trong box 3x3
                return False #Bỏ các số trùng
    return True 


def solve_board(bo):
    find = empty_board(bo) #Lấy data ô trống đầu tiên
    if not find: 
        return True #Nếu không còn ô trống -> sudoku đã được giải
    else:
        x,y = find #Tọa độ ô trống
    for i in range(1,10):
        if is_valid(bo, i, x, y): #Các số thỏa mãn trong hàm
            bo[x][y] = i #Thêm số thỏa mãn vào bảng
            if solve_board(bo): #Dùng đệ quy để lấy thêm data
                return True #Nếu đệ quy giải được, trả về True
            bo[x][y] = 0 #Backtracking - Nếu số sai (trả về False), trả lại về 0 và thử số khác
    return False #Không có số nào hợp lệ tức bảng sudoku không thể giải

def print_board(bo): #In bảng
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - ")
        for j in range(9):
            if j % 3 == 0 :
                print(" | ", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(bo[i][j] , "", end="")
            

def empty_board(bo): #Tìm ô trống
    for i in range(9):
        for j in range(9):
            if bo[i][j] == 0:
                return (i,j)
    return None


bo = [
    [7, 0, 0, 0, 0, 6, 2, 4, 0],
    [0, 0, 2, 0, 1, 0, 0, 9, 0],
    [0, 8, 0, 9, 0, 5, 7, 0, 0],
    [6, 0, 3, 0, 4, 0, 0, 0, 8],
    [0, 0, 9, 0, 8, 0, 5, 0, 0],
    [5, 0, 0, 0, 9, 0, 6, 0, 4],
    [0, 0, 6, 4, 0, 9, 0, 5, 0],
    [0, 5, 0, 0, 6, 0, 4, 0, 0],
    [0, 4, 7, 1, 0, 0, 0, 0, 6]
]

print("Bảng Sudoku ban đầu")
print_board(bo)
solve_board(bo)
print("--------------------------------------")
print("Generating....")
time.sleep(2)
print("Bảng Sudoku đã giải" )
print_board(bo)               

