
stack= []

stack.append('A')
stack.append('B')
stack.append('C')
stack.append('D')
stack.append('E')
print("Push",stack)

popelement= stack.pop(2)

print("Pop:", popelement)

peekelement= stack[-1]
print("Peek",peekelement)

boolelement= not bool(stack)
print("Bool",boolelement)

sizeelement= len(stack)
print("Size",sizeelement)

# =========================================================================================================================================================


class Stack:
    def __init__(self):
        self.stack= []
        
    def push(self, element):
        self.stack.append(element)
        
    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        return self.stack.pop()
        
    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        return self.stack[-1]
            
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)

mystack = Stack()

mystack.push('A')
mystack.push('B')
mystack.push("C")
mystack.push('D')

print("Push:" , mystack.stack)


print("Pop Value:", mystack.pop())

print("Peek Value:" , mystack.peek())
print("IsEmpty:", mystack.isEmpty())

print("size of values:", mystack.size())


# =========================================================================================================================================================
class Node:
    def __init__(self, value):
        self.value= value
        self.next = None
        
    def __ini__(self, head):
        self.head= head
        self.size= 0
        
        def push(self, value):
            new_node= Node(value)
            if self.head:
                new_node.next= self.head
            self.head= new_node
            self.size += 1
        
        def pop(self):
            if self.isEmpty():
                return "Stack is Empty"
            
            pop_node= self.head
            self.head= pop_node.next
            self.size -=1
            return pop_node.value
        
        def peek(self):
            if self.isEmpty():
                return "Stack is Empty"
            return self.head.value
        
        def isEmpty(self):
            return self.size == 0
        
        def size(self):
            return self.size

stack_val= Stack()
stack_val.push('A')
stack_val.push('B')
stack_val.push('C')
stack_val.push('D')

print('new program')
print("pop:", stack_val.pop())
print("peek:", stack_val.peek())
print("isEmpty:", stack_val.isEmpty())
print("size:", stack_val.size())           
    



