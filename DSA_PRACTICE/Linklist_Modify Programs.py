class Node:
    def __init__(self , data):
        self.data= data
        self.next = None
        

def traversal_print(head):
    current_node= node1
    while current_node:
        print(current_node.data, end="->")
        current_node = current_node.next
        
    print("Null")
        

node1 = Node(3)
node2 = Node(16)
node3 = Node(9)
node4 = Node(12)

node1.next = node2
node2.next = node3
node3.next = node4

traversal_print(node1)


# ==================================================================================================================================================
class Values:
    def __init__(self, data):
        self.data = data
        self.next = None

def FindLowestValue(head):
    min_value= head.data
    current_value = head.next
    
    while current_value :
        if current_value.data < min_value:
            min_value= current_value.data
        current_value = current_value.next
            
    return min_value

value1= Values(18)
value2= Values(25)
value3= Values(15)
value4= Values(6)
value5= Values(10)

value1.next = value2
value2.next = value3
value3.next= value4
value4.next = value5

print("The Lowest value in the linklist: ", FindLowestValue(value1))

# =================================================================

class Node:
    def __init__(self, data):
        self.data= data
        self.next= None
        
def Traverse_print(head):
    current_node= head
    while current_node:
        print(current_node.data, end="->")
        current_node = current_node.next
    print("Null")
        
def del_value(head, del_node):
        if head ==  del_node:
            return head.next
        
        current_node = head
        while current_node.next and current_node.next != del_node:
            current_node =  current_node.next
            
        if current_node.next is None:
            return head
        
        current_node.next = current_node.next.next
        return head
        
        
node1 = Node(6)
node2= Node(11)
node3 = Node(16)
node4= Node(22)
node5 = Node(25)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


print("Before Deletion:")
Traverse_print(node1) 

node1 = del_value(node1, node4) 

print("\n After Deletion:")
Traverse_print(node1)

        
# ==============================================================================================================================================================
class Node:
    def __init__(self,data):
        self.data = data
        self.next= None
        
    
def Traversing_Print(head):
    current_node = head
    while current_node:
        print(current_node.data, end="->")
        current_node = current_node.next
    print("Null")
        
def insert_node(head, new_node, position):
    if position == 1:
        new_node.next = head
        return new_node
    
    current_node= head
    for _ in range(position - 2):
        if current_node is None:
            break
        current_node = current_node.next 
    
    
    new_node.next = current_node.next
    current_node.next = new_node
    
    return head
    
node1 = Node(6)
node2= Node(11)
node3 = Node(16)
node4= Node(22)
node5 = Node(25)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


print("Before Inserting:")
Traversing_Print(node1)


newnode= Node(96)
node1 = insert_node(node1, newnode, 2)

print("\nAfter Inserting:")
Traversing_Print(node1)

