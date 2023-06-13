class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()
    def InorderTraversal(self,root):
        res = []
        if root:
            res = self.InorderTraversal(root.left)
            res.append(root.data)   
            res += self.InorderTraversal(root.right)
        return res
    def PreorderTraversal(self,root):
        res1 = []
        if root:
            res1.append(root.data)   
            res1 += self.PreorderTraversal(root.left)
            res1 += self.PreorderTraversal(root.right)
        return res1
    def PostorderTraversal(self,root):
        res2 = []
        if root:
            res2 = self.PostorderTraversal(root.left)
            res2 += self.PostorderTraversal(root.right)
            res2.append(root.data)   
        return res2
#5.1
arr = []
while True:
    ans = input(f"Continue inserting numbers? [Y/N]")
    if ans.upper() == "Y":
        n = int(input("Insert number: "))
        if n in arr:
            print("Please resubmit!")
            continue
        else:
            arr.append(n)
    elif ans.upper() == "N":
        print(f"Thanks for using our system.")
        break
    else:
        print(f"Please resubmit!")
#5.2
root = Node(arr[0])
for i in range(1,len(arr)):
    root.insert(arr[i] )
#5.3
print(f"The tree read by Preorder Traversal is: {root.PreorderTraversal(root)}")
print(f"The tree read by Postorder Traversal is: {root.PostorderTraversal(root)}")
print(f"The tree read by Inorder Traversal is: {root.InorderTraversal(root)}")
#5.4
X = int(input())
if X in root.InorderTraversal(root):
    print(f"X is in the tree")
else:
    print(f"X is not in the tree")