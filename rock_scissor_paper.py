from random import randint 
print("Bạn đang tham gia trò chơi búa lá kéo")
player = input("Vui lòng chọn 'Búa' hoặc 'Kéo' hoặc 'Lá': ")
computer = randint(0,2)
if computer == 0:
    computer = "Búa"
if computer == 1:
    computer = "Lá"
if computer == 2:
    computer = "Kéo"
print("------")
print("Bạn chọn: {}".format(player))
print("Máy chọn: {}".format(computer))
print("------")
if player == computer:
    print("Game hòa")
elif player == "Kéo":
    if computer == "Búa":
        print("Bạn thua rồi!!")
    elif computer == "Lá":
        print("Bạn thắng rồi, yayy!")
elif player == "Búa":
    if computer == "Lá":
        print("Bạn thua rồi!")
    elif computer == "Kéo":
        print("Bạn thắng rồi, yayy!")
elif player == "Lá":
    if computer == "Kéo":
        print("Bạn thua rồi!!")
    elif computer == "Búa":
        print("Bạn thắng rồi, yayy!")
else:
    print("Lỗi định dạng, vui lòng nhập lại!!")
    

