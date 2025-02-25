queue= []

queue.append('A')
queue.append('B')
queue.append('C')
queue.append('D')

print("enqueue:", queue)

pop_element= queue.pop()
print("dequeue:", pop_element)

peek_element= queue[0]
print("peek:", peek_element)

bool_element= not bool(queue)
print("bool:", bool_element)

size_element= len(queue)
print("size:", size_element)

# ==========================================================================================================================================================
class Queue:
    def __init__(self):
        self.queue= []
        
    def enqueue(self, element):
        self.queue.append(element)
        
    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.queue.pop(0)
        
    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(queue)
    
my_queue= Queue()

my_queue.enqueue('A')
my_queue.enqueue('B')
my_queue.enqueue('C')
my_queue.enqueue('D')
print("enqueue:", my_queue.queue)

print("dequeue:", my_queue.dequeue())

print("Peek:", my_queue.peek())

print("isEmpty:", my_queue.isEmpty())

print("size:", my_queue.size())


# =====================================================================================================================================================================================
