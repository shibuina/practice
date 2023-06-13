data = []
while True:
    ans = input(f"Bạn có muốn tiếp tục nhập thông tin? [C/K]")
    if ans.upper() == "C":
        print(f"Mời bạn nhập liệu! ")
        print(f"Mời bạn nhập MSSV: ")
        sID = input()
        print(f"Mời bạn nhập tên sinh viên: ")
        name = input()
        print(f"Mời bạn nhập điểm: ")
        grad = input()
        data.append([sID, name, grad])
    elif ans.upper() == "K":
        print(f"Cảm ơn bạn đã sử dụng phần mềm nhập điểm của chúng tôi.")
        print(f"Hẹn gặp lại!")
        dat = open('data.txt','a')
        for i in range(len(data)):
            dat.write(data[i])
        dat.close()
        break
    else:
        print(f"Mời bạn nhập lại!")
        
        
        