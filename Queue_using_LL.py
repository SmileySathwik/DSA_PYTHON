class Node:
    def __init__(self,val=0):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self,val):
        new_node = Node(val)
        self.size+=1
        if self.front==None and self.rear == None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
        return

    def dequeue(self):
        if self.front==None and self.rear==None:
            return "Queue is empty"
        self.size -=1
        val = self.front.val
        if self.front == self.rear:
            self.front = None
            self.rear = None
            return val
        self.front = self.front.next
        return val

    def peek(self):
        if self.front==None:
            return "Queue is Empty"
        return self.front.val

    def isEmpty(self):
        if self.front==None:
            return True
        return False

    def get_size(self):
        return self.size

if __name__ == "__main__":
    q = Queue()
    print(q.dequeue())  # Queue is empty
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print(q.peek())  # 10
    print(q.dequeue())  # 10
    print(q.get_size())  # 2
    print(q.dequeue())  # 20
    print(q.dequeue())  # 30
    print(q.dequeue())  # Queue is empty
    print(q.isEmpty())  # True

    for i in range(5):
        print(" "* (5 - i - 1), end="")
        for j in range(5):
            print("* ",end="")
        print()

#     * * * * *
#    * * * * *
#   * * * * *
#  * * * * *
# * * * * *

