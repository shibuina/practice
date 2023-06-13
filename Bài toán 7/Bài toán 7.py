class Store:
    def __init__(self):
        self.customers = []
        self.prods = []
        self.transactions = []
    def input_prods(self):
        prods = {}
        num_prods = int(input(f"How many products do you want?"))
        for prod in range(num_prods):
            prods[prod] = []
            print(f"Product ID: {prod}")
            prods[prod].append(input("Product name:"))
            prods[prod].append(float(input("Product cost:")))
            with open(r"C:\Users\Dell\Desktop\Học\CSD202\practice\Bài toán 7\Products.txt","a+") as prod_file:
                prod_file.write(f"{prod} {prods[prod][0]} {prods[prod][1]} \n")
    def input_cus(self):
        cust = {}
        num_cus= int(input(f"How many customers do you have?"))
        for cus in range(num_cus):
            cust[cus] = []
            print(f"Product ID: {cus}")
            cust[cus].append(input("Customer name:"))
            with open(r"C:\Users\Dell\Desktop\Học\CSD202\practice\Bài toán 7\Customers.txt","a+") as cus_file:
                cus_file.write(f"{cus} {cust[cus][0]} \n")
    def input_trans(self):
        trans = {}
        num_ord = int(input(f"How many orders do you have?"))
        for ord in range(num_ord):
            trans[ord] = []
            print(f"Transaction ID: {ord}")
            trans[ord].append(input("Customer ID:"))
            trans[ord].append(input("Product ID:"))
            trans[ord].append(int(input("Amount of products bought:")))
            with open(r"C:\Users\Dell\Desktop\Học\CSD202\practice\Bài toán 7\Transactions.txt","a+") as trans_file:
                trans_file.write(f"{ord} {trans[ord][0]} {trans[ord][1]} {trans[ord][2]} \n")
    def read_data(self):
        with open(r"C:\Users\Dell\Desktop\Học\CSD202\practice\Bài toán 7\Customers.txt", 'r') as file1:
            for line in file1:
                line = line.strip().split()
                self.customers.append(line)
        with open(r"C:\Users\Dell\Desktop\Học\CSD202\practice\Bài toán 7\Products.txt", 'r') as file2:
            for line in file2:
                line = line.strip().split()
                self.prods.append(line)
        with open(r"C:\Users\Dell\Desktop\Học\CSD202\practice\Bài toán 7\Transactions.txt", 'r') as file3:
            for line in file3:
                line = line.strip().split()
                self.transactions.append(line)
        print(self.customers)
        print(self.prods)
        print(self.transactions)
        
    def value_of_customer(self):
        customer_value = []
        for id_cus in self.customers:
            point = 0
            for id_buy in self.transactions:
                if id_cus[0] == id_buy[1]:
                    for id_good in self.prods:
                        if id_good[0] == id_buy[2]:
                            point += float(id_good[2])*int(id_buy[3])
            customer_value.append([id_cus, point])
        return customer_value
    
    def sort_bubble(self):
        array = self.value_of_customer()
        for i in range(len(array)):
            for j in range(i, len(array)):
                if array[j][1] > array[i][1]:
                    array[i], array[j] = array[j], array[i]
        return array

    def selection_sort(self):   
        array = self.value_of_customer() 
        for i in range(len(array)):
            max_position =i
            for j in range(i +1, len(array)):
                if array[max_position][1] < array[j][1]:
                    max_position =j
            array[i], array[max_position] = array[max_position], array[i]

        return array

    def insertion_sort(self):   
        array = self.value_of_customer() 
        for i in range(1,len(array)):
            value = array[i]
            position = i-1
            while position >=0 and value[1] > array[position][1]:
                array[position+1] = array[position]
                position -=1
            array[position +1] =value
        return array
main = Store()
main.input_prods()
main.input_cus()
main.input_trans()
main.read_data()
print(main.value_of_customer())
print(main.sort_bubble())
print(main.selection_sort())
print(main.insertion_sort())