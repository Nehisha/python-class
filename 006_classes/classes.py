1.
class Student:

    college = "sagarmatha"

    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"mero nam {self.name} ho!. Mero college {self.college}."


student1 = Student("sita")
student2 = Student("ram")
print(student1.introduce())
print(student2.introduce())
print(student1.college)


2.
class Janawar:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class dog(Janawar):
    def speak(self):  # type: ignore
        return f"{self.name} bhukchu: bhau bhau!"


class cat(Janawar):
    def speak(self):  # type: ignore
        return f"{self.name} myau garchu!"


dog = dog("kalu")  # type: ignore
cat = cat("kalo")  # type: ignore
print(dog.speak())  # type: ignore
print(cat.speak())  # type: ignore


3.
class Teacher:
    total_teacher = 0

    def __init__(self, name):
        self.name = name
        Teacher.total_teacher += 1

    @classmethod
    def get_total(cls):
        return f"Total Teachers: {cls.total_teacher}"


teacher1 = Teacher("ram")
teacher2 = Teacher("ramu")
print(Teacher.get_total())


4.
class Sadhan:
    def __init__(self, name):
        self.name = name

    def start(self):
        return f"{self.name} suru bhayo!!!"


class Gadi(Sadhan):
    def __init__(self, name, doors):
        super().__init__(name)
        self.doors = doors

    def honk(self):
        return "pi pip!"


mero_gadi = Gadi("Hyundai", 4)
print(mero_gadi.start())
print(mero_gadi.honk())
