Python Coding Questions :
1.Write a Python program to check if a number is even or odd.

def check_even_odd(num):
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

# Example
check_even_odd(7)
check_even_odd(10)


2.Write a Python function to reverse a string without using built-in functions.

def reverse_string(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

# Example
print(reverse_string("hello"))  # Output: "olleh"


3.Write a Python program to find the largest number in a given list.

def find_largest(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

# Example
print(find_largest([3, 7, 2, 9, 5]))  # Output: 9


4.Write a Python function to check if a given string is a palindrome.

def is_palindrome(s):
    s = s.lower()  # Making it case-insensitive
    return s == s[::-1]

# Example
print(is_palindrome("Madam"))  # Output: True
print(is_palindrome("Hello"))  # Output: False


5.Write a Python program to count the occurrences of each character in a given string.

def count_characters(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

# Example
print(count_characters("banana"))  # Output: {'b': 1, 'a': 3, 'n': 2}


Difference Between Class and Object
 A class is a blueprint for creating objects, defining attributes and behaviors. An object is an instance of a class with specific values assigned to its attributes. Example:

 class Car: pass  
my_car = Car()  # Object of Car class  


Inheritance Example
 Inheritance allows a class to inherit properties and methods from another class. Example:

 class Animal:  
    def speak(self):  
        print("Animal speaks")  

class Dog(Animal):  
    def speak(self):  
        print("Dog barks")  

d = Dog()  
d.speak()  # Output: Dog barks  


Method Overriding Example
 Method overriding occurs when a subclass provides a new implementation for a method inherited from a parent class.

 class Parent:  
    def show(self):  
        print("Parent method")  

class Child(Parent):  
    def show(self):  
        print("Child method")  

c = Child()  
c.show()  # Output: Child method  


Instance, Class, and Static Methods


Instance method: Operates on instance data.
Class method: Works on class-level data (@classmethod).
Static method: Independent function inside a class (@staticmethod).
class Demo:  
    def instance_method(self): pass  
    @classmethod  
    def class_method(cls): pass  
    @staticmethod  
    def static_method(): pass  


Encapsulation Example
 Encapsulation restricts access to certain data using private variables (__var). Example:

 class BankAccount:  
    def __init__(self, balance):  
        self.__balance = balance  

    def get_balance(self):  
        return self.__balance  

account = BankAccount(1000)  
print(account.get_balance())  # Output: 1000  .

