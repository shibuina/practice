import random
# tạo dữ liệu trong file
# with open(r'C:\Users\Dell\Desktop\Học\CSD202\practice\Bài toán 12\data.txt','a+') as datafile:
#     for _ in range (1000):
#         datafile.write(f"{random.randint(1,1000)}\n")
# bucket sort
class CountingSort():
    def getfile(self):
        numList = []
        with open(r'C:\Users\Dell\Desktop\Học\CSD202\practice\Bài toán 12\data.txt','r') as datafile:
            for lines in datafile:
                numList.append(int(lines))
        return numList
    def CountingSort(self,x):
        ln = len(x)
        lns = max(x)-min(x)+1
        res = [0 for _ in range(ln)]
        count = [0 for _ in range(lns)]
        for _ in range(ln):
            count[x[_]-min(x)] += 1
        for _ in range (1,lns):
            count[_] += count[_-1]
        for _ in range (ln-1,-1,-1):
            res[count[x[_]-min(x)]-1] = x[_]
            count[x[_]-min(x)] -=1
        return res
#chạy code
main = CountingSort()
data = main.getfile()
print(data)
print(main.CountingSort(data))