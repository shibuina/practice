while True:
    try:
        dat = open(input(),'r')
        for lines in dat:
            lines = lines.split()
            print(f"MSSV: {lines[0]} \nTên: {lines[1]} \nĐiểm: {lines[2]}")
        break
    except:
        print("Mời bạn nhập lại tên file!")

