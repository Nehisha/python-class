# 1.Write a Python program to import a built-in array module and display the namespace of the said module.
import array

print(dir(array))  # In Python, dir() is a built-in function that:Returns a list of names in the current or specified namespace.


# 2. Create a Class and Display Its Namespace


class Student:
    school = "Informatics"

    def __init__(self, name, age):
        self.name = name
        self.age = age


print(Student.__dict__)  # shows the namespace — a dictionary containing all class-level names and their values.

# 3. Write a Python program to create an instance of a specified class and display the namespace of the said instance.


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Nehisha Hircahan", "19")
print(student1.__dict__)
