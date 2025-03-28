class Node:
    def __init__(self,data):
        self.data= data
        self.next = None
        
        
class Queue:
    def __init__(self):
        self.front= None
        self.rear = None
        self.length= 0
        
    def enqueue(self, element):
        new_node= Node(element)
        if self.rear is None:
            self.front = self.rear = new_node
            self.length +=1
            return
        self.rear.next = new_node
        self.rear = new_node
        self.length +=1
        
    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty" 
        temp = self.front
        self.front = temp.next
        self.length -= 1
        if self.front is None:
            self.rear= None
        return temp.data
        
    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.front.data
    
    def isEmpty(self):
        return self.length == 0
    
    def size(self):
        return self.length
    
    def queueprint(self):
        queue_node = self.front
        while queue_node:
            print(queue_node.data, end="->")
            queue_node = queue_node.next
        print("...")
            
my_queue= Queue()

my_queue.enqueue('A')
my_queue.enqueue('B')
my_queue.enqueue("C")
my_queue.enqueue('D')



print("Queue:", end="")
my_queue.queueprint()

print("dequeue :", my_queue.dequeue())
print("Peek:", my_queue.peek())

print('isEmpty:', my_queue.isEmpty())
print("size:", my_queue.size())