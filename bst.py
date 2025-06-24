class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        new_node = Node(data)
        Left = False
        Right = False
        if self.root==None:
            self.root = new_node
            return
        temp = tempnxt = self.root
        if(temp.data>data):
            tempnxt = tempnxt.left
            Left = True
        else:
            tempnxt = tempnxt.right
            Right = True
        while(tempnxt!=None):
            temp = tempnxt
            if (temp.data > data):
                tempnxt = tempnxt.left
                Left = True
                Right = False
            else:
                tempnxt = tempnxt.right
                Left = False
                Right = True

        if (Left == True):
            temp.left = new_node
        else:
            temp.right = new_node
        return

    def inorder(self,node):
        if node==None:
            return
        self.inorder(node.left)
        print(node.data)
        self.inorder(node.right)

    def delete(self,data):
        temp = self.root
        temp_prv = temp
        found = False
        while(temp!=None):
            if temp.data == data:
                found = True
                break
            temp_prv = temp
            temp = temp.left if temp.data > data else temp.right
        if found:
            print(f"Deletion Successfull {data}")
            if temp.left == None and temp.right == None:    #leaf Node
                if temp_prv == temp:    #Root Node
                    self.root = None
                    return
                if temp_prv.data > data:
                    temp_prv.left = None
                    return
                else:
                    temp_prv.right = None
                    return
            elif temp.left == None and temp.right!=None:      #single Child
                if temp.data > temp_prv.data:
                    temp_prv.right = temp.right
                else:
                    temp_prv.left = temp.right
                return
            elif temp.right == None and temp.left!=None:
                if temp.data > temp_prv.data:
                    temp_prv.right = temp.left
                else:
                    temp_prv.left = temp.left
                return
            else:   #node contains 2 childs
                if temp.right.left == None:
                    temp.data = temp.right.data
                    temp.right = temp.right.right
                    return
                else:
                    temp1 = temp.right
                    temp2 = temp.right.left
                    while(temp2.left!=None):
                        temp1 = temp2
                        temp2 = temp2.left
                    temp1.left = None
                    temp.data = temp2.data
                    return
        else:
            print("Not found !!")





# MAIN INTERACTIVE LOOP
tree = BST()

print("Binary Search Tree Console")
print("Commands:")
print("1 <number> - Insert")
print("2 <number> - Delete/Search")
print("3 - Inorder Traversal")
print("0 - Exit")

while True:
    print("Binary Search Tree Console")
    print("Commands:")
    print("1 <number> - Insert")
    print("2 <number> - Delete/Search")
    print("3 - Inorder Traversal")
    print("0 - Exit")
    user_input = input("Enter command: ").strip()
    if user_input == "0":
        print("Exiting...")
        break
    parts = user_input.split()

    if not parts:
        continue

    cmd = parts[0]

    if cmd == "1" and len(parts) == 2:
        tree.insert(int(parts[1]))
    elif cmd == "2" and len(parts) == 2:
        tree.delete(int(parts[1]))
    elif cmd == "3":
        print("Inorder Traversal: ", end="")
        tree.inorder(tree.root)
        print()
    else:
        print("Invalid command.")
