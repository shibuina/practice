import random
#tạo dữ liệu trong file
# with open(r'C:\Users\Dell\Desktop\Học\CSD202\practice\Bài toán 11\data.txt','a+') as datafile:
#     for _ in range (1000):
#         datafile.write(f"{round(random.random(),3)}\n")
#bucket sort
class BucketSort():
    def getfile(self):
        numList = []
        with open(r'C:\Users\Dell\Desktop\Học\CSD202\practice\Bài toán 11\data.txt','r') as datafile:
            for lines in datafile:
                numList.append(float(lines))
        return numList
    def BucketSort(self,x):
        res = []
        arr = []
        buckets = 10
        for _ in range(buckets):
            arr.append([])
        for number in x:
            arr[int(number*buckets)].append(number)
        for bucket in range(buckets):
            arr[bucket] = sorted(arr[bucket])
        for bucket in range(buckets):
            for number in range(len(arr[bucket])):
                res.append(arr[bucket][number])
        return res
#chạy code
main = BucketSort()
data = main.getfile()
print(data)
print(main.BucketSort(data))