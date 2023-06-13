def quicksort(a):
    if len(a) <= 1:
        return a
    else:
        pivot = a[len(a)//2]
        left = [i for i in a if i < pivot]
        mid = [i for i in a if i == pivot]
        right = [i for i in a if i > pivot]
    return quicksort(left) + mid + quicksort(right)
        
def merge_sort(a):
    if len(a) > 1:
        left = a[:len(a)//2]
        right = a[len(a)//2:]
        
        merge_sort(left)
        merge_sort(right)
        
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1
    
    return a
#input the data
with open('Bài toán 9\data.txt','r') as a:
    a = [int(i) for i in a.read().split()]
    print(f"Kết quả khi dùng Quick Sort là: {quicksort(a)}")
    print(f"Kết quả khi dùng Merge Sort là: {merge_sort(a)}")
