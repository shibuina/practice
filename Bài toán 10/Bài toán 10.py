def radix_sort(nums):
    digits = 10
    max_length = False
    tmp, placement = -1, 1

    while not max_length:
        max_length = True
        buckets = [list() for _ in range(digits)]
        for i in nums:
            tmp = i // placement
            buckets[tmp % digits].append(i)
            if max_length and tmp > 0:
                max_length = False

        a = 0
        for b in range(digits):
            buck = buckets[b]
            for i in buck:
                nums[a] = i
                a += 1

        placement *= digits

    return nums
with open('Bài toán 10\data.txt','r') as a:
    a = [int(i) for i in a.read().split()]
    print(f"Kết quả khi dùng Radix Sort là: {radix_sort(a)}")
