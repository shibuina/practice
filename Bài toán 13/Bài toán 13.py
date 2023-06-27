class StudentList():
    #lấy dữ liệu từ file
    def getfile(self):
        StuList = []
        with open(r'C:\Users\Dell\Desktop\Học\CSD202\practice\Bài toán 13\data.txt','r',encoding= 'utf8') as datafile:
            for lines in datafile:
                lines = lines.split("_")
                StuList.append([lines[0],lines[1]] + [float(lines[i]) for i in range (2,len(lines))]+[(float(lines[2])+float(lines[3]))*2+float(lines[4])])
        return StuList
    #lấy thông tin HS
    def GetStudentInfo(self,StuList):
        SId = input(f"Nhập số báo danh của học sinh cần tìm:\n")
        for students in StuList:
            if SId == students[0]:
                print(f"Bạn đã tìm học sinh có SBD {SId}")
                print(f"Tên của học sinh là {students[1]}")
                print(f"Điểm 3 môn Toán, Văn, Anh của học sinh là Toán: {students[2]}, Văn: {students[3]}, Anh: {students[4]}")
                print(f"Tổng ĐXT của học sinh là: {students[5]}")
    #Xếp hạng HS
    def RankStudents(self,StuList):
        for i in range(len(StuList)):
            for j in range(len(StuList)):
                if StuList[i][5] > StuList[j][5]:
                    StuList[i],StuList[j] = StuList[j],StuList[i]
        return StuList

#chạy code
main = StudentList()
data = main.getfile()
#Q1
print(f"Chào mừng đến với trang tra cứu thông tin tuyển sinh vào 10!")
while True:
    print(f"Bạn có muốn tiếp tục tìm kiếm? [Y/N]")
    choice = input()
    if choice.lower() == 'y':
        main.GetStudentInfo(data)
    elif choice.lower() == 'n':
        print(f"Cảm ơn bạn đã sử dụng dịch vụ của chúng tôi!")
        print(f"Hẹn gặp lại!")
        break
#Q2
print(f"Chào mừng đến với trang thông tin tuyển sinh vào 10!")
input(f"Nhập tên trường: \n")
grade = float(input(f"Nhập điểm xét tuyển: \n"))
StudentNum = int(input(f"Nhập số lượng tuyển sinh: \n"))
stu = 0
for students in main.RankStudents(data):
    if stu == StudentNum:
        break
    if students[2] <= 1 or students[3] <= 1 or students[4] <=1:
        continue
    elif students[5]>grade:
        print(students)
        stu += 1
