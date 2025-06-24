class Node:
    def __init__(self,val = 0):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self,data):
        node = Node(data)
        self.size+=1
        if self.head!=None:
            node.next = self.head
            self.head = node
            return
        self.head = node
        return

    def pop(self):
        if self.head!=None:
            val = self.head.val
            self.head = self.head.next
            self.size-=1
            return val
        return "Stack is Empty"

    def peek(self):
        if self.head!=None:
            return self.head.val
        return "Stack is empty"

    def isEmpty(self):
        if self.head == None:
            return True
        return False
    def get_size(self):
        return self.size

def main():
    s = Stack()
    print(s.isEmpty())  # True
    s.push(10)
    s.push(20)
    s.push(30)
    print(s.peek())  # 30
    print(s.pop())  # 30
    print(s.get_size())  # 2
    print(s.pop())  # 20
    print(s.pop())  # 10
    print(s.pop())  # Stack is Empty
    print(s.isEmpty())  # True

if __name__ == "__main__":
    main()












