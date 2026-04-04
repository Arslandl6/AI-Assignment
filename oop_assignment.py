# 1. Student Class
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name, self.marks)

s1 = Student("Ali", 90)
s1.display()

# 2. Laptop Constructor
class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

l1 = Laptop("HP", 50000)
print(l1.brand, l1.price)

# 3. Rectangle Area
class Rectangle:
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

r = Rectangle(5, 4)
print("Area:", r.area())

# 4. Employee Class Variable
class Employee:
    company_name = "ABC Ltd"

    def __init__(self, name):
        self.employee_name = name

e1 = Employee("John")
print(e1.employee_name, Employee.company_name)

# 5. Static Method
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

print(Calculator.add(5, 3))

# 6. Inheritance
class Animal:
    def sound(self):
        print("Animal sound")

class Cat(Animal):
    def sound(self):
        print("Meow")

c = Cat()
c.sound()

# 7. Multilevel Inheritance
class Person:
    def __init__(self, name):
        self.name = name

class Employee1(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

class Manager(Employee1):
    def __init__(self, name, emp_id, dept):
        super().__init__(name, emp_id)
        self.dept = dept

m = Manager("Aman", 101, "IT")
print(m.name, m.emp_id, m.dept)

# 8. Multiple Inheritance
class Father:
    def showFather(self):
        print("Father")

class Mother:
    def showMother(self):
        print("Mother")

class Child(Father, Mother):
    pass

ch = Child()
ch.showFather()
ch.showMother()

# 9. Method Overriding
class BankAccount:
    def withdraw(self, amount):
        print("Withdraw:", amount)

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        print("Maintain minimum balance!")

sa = SavingsAccount()
sa.withdraw(1000)

# 10. Encapsulation
class Account:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amt):
        self.__balance += amt

    def withdraw(self, amt):
        if amt <= self.__balance:
            self.__balance -= amt
        print("Balance:", self.__balance)

acc = Account()
acc.deposit(1000)
acc.withdraw(500)

# 11. Polymorphism
class Circle:
    def area(self):
        return 3.14 * 5 * 5

class Square:
    def area(self):
        return 4 * 4

shapes = [Circle(), Square()]
for s in shapes:
    print(s.area())

# 12. Abstract Class
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Bike(Vehicle):
    def start(self):
        print("Bike started")

class Car(Vehicle):
    def start(self):
        print("Car started")

Bike().start()
Car().start()

# 13. Division by Zero
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")

# 14. Invalid Input
try:
    x = int("abc")
except ValueError:
    print("Invalid input")

# 15. Calculator Exception
try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(a / b)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")

# 16. File Handling
try:
    f = open("test.txt", "w")
    f.write("Hello")
finally:
    f.close()

# 17. Custom Exception
class InsufficientBalanceError(Exception):
    pass

balance = 500
try:
    withdraw = 600
    if withdraw > balance:
        raise InsufficientBalanceError("Not enough balance")
except InsufficientBalanceError as e:
    print(e)

# 18. Voting Eligibility
try:
    age = 16
    if age < 18:
        raise Exception("Not eligible to vote")
except Exception as e:
    print(e)

# 19. Index Error
try:
    lst = [1,2,3]
    print(lst[5])
except IndexError:
    print("Index out of range")

# 20. Try-Except-Else
try:
    x = 10 / 2
except:
    print("Error")
else:
    print("Result:", x)

# 21. Theory (print)
print("ML uses algorithms like Linear Regression, SVM.")
print("DL uses Neural Networks like CNN, RNN.")