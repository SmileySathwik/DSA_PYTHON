class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Single_linked_list:
    def __init__(self):
        self.head = None
    def insert_at_begin(self,data):
        node = Node(data)
        if(self.head==None):
            self.head = node
        else:
            node.next = self.head
            self.head = node
    def display(self):
        if(self.head==None):
            print("No Data")
            return 
        temp = self.head
        while(temp!=None):
            print(temp.data , "-> " ,end="")
            temp = temp.next
        print("None")

s1 = Single_linked_list()
s1.insert_at_begin(1)
s1.insert_at_begin(2)
s1.display()

        


