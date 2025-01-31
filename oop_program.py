class Circle:
    def __init__(self, radius):
        self.radius= radius
        
    def area(self):
        return (22/7) * self.radius ** 2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius
    
c1= Circle(int(input()))
print(c1.area())
print(c1.perimeter())

# ======================================================================================================================================================
class Employee:
    def __init__(self, role, dept, salary):
        self.role= role
        self.dept= dept
        self.salary= salary
    
    def show_details(self):
        print("role = ", self.role)
        print("dept = ", self.dept)
        print("salary = ", self.salary)
    
class Engineer(Employee):
    def  __init__(self, name, age):
        self.name= name
        self.age= age
        super().__init__("Engineer", "IT", "80000")
        
emp1=Employee("Manager", "Finance", "60000")
emp1.show_details()

emp2= Engineer("Raj", "22")
emp2.show_details()

# ======================================================================================================================================================
class Order:
    def __init__(self, item, price):
        self.item= item
        self.price= price
    
    def __gt__(self, ord2):
        return self.price > ord2.price

ord1=  Order("Chips", "30")
ord2= Order("Biscuit", "20")

print(ord1 > ord2)

# ===================================================================================================================
class solution:
    
    def __init__(self, name):
        self.name= name
    
    


s1= solution("raj")
print(s1.name)
del s1.name
print(s1.name)
# =========================================================================================================================================
class person:
    
    __name= "raj" # private message define __name
    def __hello(self):
        print("hello user")
    
    def welcome(self):
        self.__hello()
        
    
s1= person()
print(s1.welcome())
# print(s1.__name)        # this print massage is not work because of the private message 
    
    
# =========================================================================================================================================
# Inheritance program

class car:
    @staticmethod
    def start():
        print("Car Started..")
    
    def  stop():
        print("Car Stopped..")
    
class brand(car):
     
    def __init__(self, name):
        self.name= name

class model(brand):
    
    def __init__(self, type):
        self.type= type
        
        
c2= brand("Toyota Fortuner")
c1= model("Diesel")
print(c2.name)
print(c1.type)
print(c1.start()) 

# ======================================================================================================================================
# multiple inheritance

class A:
    varA="Welcome to class A"

class B:
    varB="Welcome to class B"

class C(A, B):
    varC="Welcome to class C"

c1= C()
print(c1.varA)   
print(c1.varB)
print(c1.varC)

# =====================================================================================================================================
# super method program
class car:
    def __init__(self,type):
        self.type=type
    
    @staticmethod
    def start():
        print("Car Started..")
    
    @staticmethod
    def stop():
        print("Car Stoped..")
 
class brand(car):      
    def __init__(self, name, type):
        super().__init__(type)
        self.name=name
        super().start()
            
c1= brand("Toyota", "diesel")
print(c1.name,c1.type)

# ======================================================================================================================================================
# classmethod program

class person:
    name= "rahul kumar"

# two ways to print name using __class__ or classmethod
    # def change_name(self, name):
    #     self.__class__.name=name
    @classmethod
    def change_name(cls, name):
        cls.name= name
    
    
s1= person()
s1.change_name("raj")
print(s1.name)
print(person.name)

# =======================================================================================================================================================
# property method program

class student:
    def  __init__(self, phy, chem, math):
        self.phy=phy
        self.chem=chem
        self.math=math
    
    @property
    def percentage(self):
        return (self.phy + self.chem + self.math)/ 3 
    
s1= student(98, 85, 97)
print(f"{s1.percentage:.2f}".format(s1.percentage))

s1.chem= 95
print(s1.percentage)


# =======================================================================================================================================================
# Polymorphism program
class Complex:
    def __init__(self, real, img):
        self.real= real
        self.img= img
        
    def show_num(self):
        print(self.real,"i +", self.img ,"j")
    
    def __add__(self, num2):
        newReal= self.real + num2.real
        newImg= self.img + num2. img
        return Complex(newReal, newImg)
    
    def __sub__(self, num2):
        newReal= self.real - num2.real
        newImg= self.img - num2. img
        return Complex(newReal, newImg)
    
c1= Complex(5,8)
c1.show_num()

c2= Complex(4,6)
c2.show_num()

# c3= c1.add(c2)
c3 = c1 + c2
c3.show_num()

c4 = c1 - c2
c4.show_num()

# ================================================================================================================
class Student:
    college_name= "SGBAU"
   
    def __init__(self, name, marks):
        self.name= name
        self.marks= marks
    
    def welcome(self):
        print("Welcome",self.name, "your Percentage is", self.marks)
    
    @staticmethod #use static method to print Hello Student without using self and any parameter
    def Hello():
        print("Hello Student")
    

s1= Student("sagar", 98)
# print(s1.name, s1.marks) # this print function can print name and marks only
s1.welcome()
s1.Hello()
s2= Student("karen", 75)
print(s2.name, s2.marks)

# Two ways to print college_name
# print(s2.college_name)
print(Student.college_name)



# ================================================================================================================
class Solution:
    def __init__(self, name, marks):
        self.name= name
        self.marks= marks
    
    def avg(self):
        sum=0
        for val in self.marks:
            sum += val
            total =sum /3
        print("Hi", self.name, "your average score is {:.2f}".format(total)) 
        # print("hi", self.name, "your average score is", sum/3 )
    
        
    
    
s1 = Solution("Raj", [87,78,98])
print(s1.name, s1.marks)
s1.avg()

