#Bài toán số 3
n=int(input())

stack=[]

#hàm trả ra giá trị nhị phân dùng stack
def bina(a):
  result=""
  while a >= 2:
      i=a%2
      stack.append(i)
      a=int(a/2)
  stack.append(a)
  for i in range (len(stack)):
      result+=str(stack[len(stack)-i-1])
  return result
print(bina(n))

    