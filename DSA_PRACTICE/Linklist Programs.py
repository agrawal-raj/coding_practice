
class Node:
    def __init__(self, data):
        self.data= data
        self.next= None
        
        
node1= Node(3)
node2= Node(15)
node3 = Node(5)
node4 = Node(2)
    
node1.next= node2
node2.next= node3
node3.next= node4
    
current_node= node1
while current_node:
    print(current_node.data, end="->")
    current_node = current_node.next
        
print("Null")



# =============================================================================================================================================

class Node :
    def __init__(self, data):
        self.data= data
        self.next= None
        self.prev = None
        
node1 =Node(5)
node2 = Node(13)
node3 = Node(2)
node4 = Node(9)

node1.next= node2

node2.prev= node1
node2.next= node3

node3.prev= node2
node3.next= node4

node4.prev= node3

print("\nTraversing Forward ")
current_node= node1
while current_node:
    print(current_node.data, end="->")
    current_node = current_node.next

print("null")   

print("\nTraversing Backward ")
current_node= node4
while current_node:
    print(current_node.data, end="->")
    current_node= current_node.prev

print("null")

# =======================================================================================================================================================
class Node:
    def __init__(self, data):
        self.data= data
        self.next= None
        

node1= Node(3)
node2= Node(18)
node3= Node(6)
node4= Node(12)

node1.next=  node2
node2.next= node3
node3.next= node4
node4.next= node1 # circular link

current_node= node1
start_node= node1
print(current_node.data, end="->")
current_node= current_node.next

while current_node !=  start_node:
    print(current_node.data, end="->")
    current_node= current_node.next 

print("...")


# ==============================================================================================================================================

class Node:
    def __init__(self,data):
        self.data= data
        self.next= None
        self.prev= None
        
node1= Node(3)
node2= Node(18)
node3= Node(6)
node4= Node(12)

node1.next= node2
node1.prev= node4

node2.next= node3
node2.prev = node1


node3.next= node4
node3.prev= node2

node4.next= node1
node4.prev = node3

print("\nTraversing Forward")
current_node= node1
start_node = node1
print(current_node.data, end="->")
current_node= current_node.next

while current_node != start_node:
    print(current_node.data, end="->")
    current_node = current_node.next

print("...")
    
    
print("\nTraversing Backward")
current_node = node4
start_node= node4
print(current_node.data, end="->")
current_node= current_node.prev

while current_node != start_node:
    print(current_node.data, end="->")
    current_node= current_node.prev
    
print("...")