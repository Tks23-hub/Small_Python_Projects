#1. Hello World
print ("hello world")

# No need for ; at the end.
# Indentation is crucial (no {} or ; for code blocks).



#2. Variables and Data Types
x = 5  # int
y = 3.14  # float
name = "Alice"  # str
is_active = True  # bool
print(type(x))

# No need to declare types (dynamic typing).
# Use type() to check variable types.



#3. Basic I/O
name = input("Enter your name: ")  # User input
print(f"Hello, {name}!")  # f-strings for formatting


# 4. Conditional Statements
age = 20

if age >= 18:
    print("Adult")
elif age > 12:
    print("Teen")
else:
    print("Child")

# elif is Python’s version of else if.
# Indentation defines blocks (no end or } needed).




# 5. Loops

for i in range(5):
    print(i)  # 0 to 4

count = 0
while count < 5:
    print(count)
    count += 1

# range(n) gives 0 to n-1.
# No need for ++ or -- (use += or -=).





# 6. Functions

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# def defines a function.
# Functions return None by default if no return value is specified.




# 7. Lists (Arrays)

numbers = [1, 2, 3, 4]
numbers.append(5)
print(numbers[0])  # Access by index

# Lists are mutable, can hold mixed data types.



# 8. Dictionaries (Objects)

person = {"name": "Bob", "age": 30}
print(person["name"])
person["city"] = "New York"

# Key-value pairs like JavaScript objects.



# 9. List Comprehensions

squares = [x**2 for x in range(10)]
print(squares)
# Quick way to generate lists.



# 10. Classes (OOP)

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return "Woof!"

dog = Dog("Rex")
print(dog.bark())
# __init__ is the constructor.
# self is used to refer to the instance.