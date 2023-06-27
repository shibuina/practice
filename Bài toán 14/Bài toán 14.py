class Node:
    def __init__ (self, data = None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.size += 1

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1
    def search_value(self, value):
        current_node = self.head
        while current_node is not None:
            if value in current_node.data:
                return current_node.data
            current_node = current_node.next
        return None
def hash(x):
        return x%100
class StudentList():
    #lấy dữ liệu từ file
    def getfile(self):
        hash_table = {}
        for _ in range(100):
            hash_table[_] = LinkedList()
        with open(r'C:\Users\Dell\Desktop\Học\CSD202\practice\Bài toán 14\data.txt','r',encoding= 'utf8') as datafile:
            for lines in datafile:
                lines = lines.split("_")
                hash_table[hash(int(lines[0]))].add(lines)
        return hash_table
    #lấy thông tin HS
    def GetStudentInfo(self,StuList):
        SId = input(f"Nhập số báo danh của học sinh cần tìm:\n")
        if StuList[hash(int(SId))].search_value(SId):
            print(f"Học sinh bạn tìm kiếm là: {StuList[hash(int(SId))].search_value(SId)}")
        else:
            print(f"Không có học sinh bạn tìm kiếm")


#chạy code
main = StudentList()
data = main.getfile()
#Q1
print(f"Chào mừng đến với trang tra cứu thông tin tuyển sinh vào 10!")
while True:
    print(f"Bạn có muốn tiếp tục tìm kiếm? [Y/N]")
    choice = input()
    if choice.lower() == 'y':
        try:
            main.GetStudentInfo(data)
        except:
            print("Hãy nhập lại")
    elif choice.lower() == 'n':
        print(f"Cảm ơn bạn đã sử dụng dịch vụ của chúng tôi!")
        print(f"Hẹn gặp lại!")
        break