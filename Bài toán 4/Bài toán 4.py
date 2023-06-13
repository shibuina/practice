#Bài toán 4
def ban_ve_bong_da():
  name_queue=[]
  ticket_queue=[]
  while True:
    name=input("Nhập tên: ")
    name_queue.append(name)
    try:
      tickets=int(input("Nhập số vé mua: "))
      ticket_queue.append(tickets)
    except:
      print("Nhập số: ")
    opt= input("Bạn có muốn tiếp tục? ")
    opt= opt.upper()
    if opt== "N":
      print("Vé của bạn đã được ghi lại")
      break
    elif opt== "Y":
      continue
    else:
      print("Vé của bạn đã được ghi lại")
      break
  remain= int(input("Nhập số vé được phát hành "))
  lst=[]
  for i in range (len(name_queue)):
    pair=[]
    pair.append(name_queue[i])
    if remain >= ticket_queue[i]: 
      remain-=ticket_queue[i]
      pair.append(ticket_queue[i])
    elif remain > 0:
      pair.append(remain)
      remain=0  
    elif remain==0:
      pair.append(remain)
    lst.append(pair)
  print(lst)  
ban_ve_bong_da()