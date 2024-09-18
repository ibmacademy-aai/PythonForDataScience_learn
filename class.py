class Person:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality
    def greet(self):
        return f"Hi, I'm {self.name}. I am {self.age} years old. I am from {self.nationality}"

person1 = Person("Alice", 30, 'Germany') # objek 1
person2 = Person("Arifian", 22, 'Indonesia') # objek 2
person3 = Person("IShowSpeed", 25, 'USA') # objek 3
print(person1.greet())
print(person2.greet())
print(person3.greet())


class Car:
    def __init__(self, brand, model, year=2021):
        self.brand = brand
        self.model = model
        self.year = year

# Membuat objek dari class Car dengan dan tanpa tahun
car1 = Car("Mazda", "CX-5") # Tanpa diinisiasi tahun
car2 = Car("Ford", "Mustang", 1967)

print(car1.year)  
print(car2.year)  

# Rumus persegi panjang
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height # Rumus luas

    def perimeter(self):
        return 2 * (self.width + self.height) # Rumus keliling

# Membuat objek dari class Rectangle
rect = Rectangle(10, 5)

# Luas
print(rect.area())

# Keliling
print(rect.perimeter())  