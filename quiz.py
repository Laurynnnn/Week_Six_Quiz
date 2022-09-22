# create a credit card class with the following attributes: card number, 
# expiration date, and security code. Create a method that will print out the card number, 
# expiration date, and security code. Create an instance of the class and call the method.

class CreditCard:
    def __init__(self, card_number, expiration_date, security_code):
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.security_code = security_code

    def __repr__(self):
        return f"Card Number: {self.card_number} \n Expiration Date: {self.expiration_date} \
            \n Security Code: {self.security_code}"

creditcard = CreditCard("CD1000000000", "20/08/2022", "202110")
print(creditcard)

# create Animal class and Dog class. Make the Dog class inherit from the Animal class. 
# Add a bark method to the Dog class. Create an instance of the Dog class and call the bark method.

class Animal:
    def __init__(self):
        pass

class Dog(Animal):
    def __init__(self):
        super().__init__()

    def bark(self):
        print("I am a dog and I can bark.")

dog = Dog()
dog.bark()


# create a class called Queue. The class should have the following methods: enqueue, dequeue, and size. 
# The enqueue method should add an item to the queue. The dequeue method should remove an item from the queue. 
# The size method should return the size of the queue.

class Queue:
    def __init__(self):
        self.queue = [20, 23]

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        self.queue.pop()
    
    def size(self):
        return len(self.queue)
    
    def show(self):
        return self.queue

q = Queue()
q.isEmpty()
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
print("Before dequeue, size: ")
print(q.size())
q.dequeue()
print("After dequeue, size: ")
print(q.size())
print(q.show())
# print("Size of queue is {}".format(len(self.queue)))


# create a class called Stack. The class should have the following methods: push, pop, and size. 
# The push method should add an item to the stack. The pop method should remove an item from the stack. 
# The size method should return the size of the stack.

class Stack:
    def __init__(self):
        self.stack = [9,0]

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            return ("Stack is empty. Stack Underflow :(")
        return self.stack.pop()

    def size(self):
        return len(self.stack)
    
    def show(self):
        return self.stack

s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.show())
print(s.pop())
print(s.show())
print(s.size())

# create a class called Person. The class should have the following attributes: name, age, and address. 
# The class should have the following methods: eat, sleep, and work. 
# The eat method should print out the name of the person and the word "is eating". 
# The sleep method should print out the name of the person and the word "is sleeping". 
# The work method should print out the name of the person and the word "is working".

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __repr__(self):
        return f"Name: {self.name} \n Age: {self.age} \n Address: {self.address}"

    def eat(self):
        print("{} is eating".format(self.name))

    def sleep(self):
        print("{} is sleeping".format(self.name))

    def work(self):
        print("{} is working".format(self.name))

person = Person("Lauryn", 21, "Kazinga")
print(person)
person.eat()
person.sleep()
person.work()

# create a class called Employee. The class should have the following attributes: name, age, and salary. 
# The class should have the following methods: eat, sleep, and work. 
# The eat method should print out the name of the person and the word "is eating". 
# The sleep method should print out the name of the person and the word "is sleeping". 
# The work method should print out the name of the person and the word "is working". 
# Create a subclass of Employee called Programmer. The Programmer class should have the following attributes: 
# name, age, salary, and programming language. The Programmer class should have the following methods: eat, 
# sleep, work, and code. The code method should print out the name of the person and the word "is coding in" 
# and the programming language. Create an instance of the Programmer class and call all the methods.

# create a class called Vehicle. The class should have the following attributes: make, model, and year. 
# The class should have the following methods: start, stop, and drive. The start method should print out 
# the make, model, and year of the vehicle and the word "is starting". The stop method should print out 
# the make, model, and year of the vehicle and the word "is stopping". The drive method should print out 
# the make, model, and year of the vehicle and the word "is driving". Create a subclass of Vehicle called Car.
# The Car class should have the following attributes: make, model, year, and color. The Car class should 
# have the following methods: start, stop, drive, and park. The park method should print out the make, model, 
# year, and color of the car and the word "is parking". Create an instance of the Car class and call all the 
# methods.

# create a class called Animal. The class should have the following attributes: name, color, and age. 
# The class should have the following methods: eat, sleep, and make_sound. 
# The eat method should print out the name of the animal and the word "is eating". 
# The sleep method should print out the name of the animal and the word "is sleeping". 
# The make_sound method should print out the name of the animal and the word "is making a sound". 
# Create a subclass of Animal called Dog. 
# The Dog class should have the following attributes: name, color, age, and breed. 
# The Dog class should have the following methods: eat, sleep, make_sound, and bark. 
# The bark method should print out the name of the dog and the word "is barking". 
# Create an instance of the Dog class and call all the methods.

# create a class of your choice. It should have at least 3 attributes and 3 methods where one of the methods 
# is a static method. Implement polymorphism, encapsulation, and inheritance.

class Cities:
    
    def __init__(self, name, temp, population, park):
        self.name = name
        self.temp = temp
        self.population = population
        self.park = park
        self.__country = "Uganda"

    def __repr__(self):
        return f"Name: {self.name} \n Temperature: {self.temp} \n Population: {self.population} \
         \n Park: {self.park}"
    # static method     
    def area(x, y):
        return x * y
    
#abstraction
    def naming(self):
        print("Cities of {}".format(self.__country))

    def setCountry(self, countryy):
        self.__country = countryy

    def getCountry(self):
        return self.__country
        
    def name_to_initial(self, initial):
        # initial = input("Enter initials of city name: ")
        self.name = initial
        print("Initial created: ")
        return self.name

class Central(Cities):
    def __init__(self, name, temp, population, park):
        super().__init__(name, temp, population, park)
    
    def popun(self):
        print("The central cities are densely populated.")

    def get_name(self):
        return self.name

    def get_detail(self):
        return 0

#Polymorphism
class Kampala(Central):
    def __init__(self, name, temp, population, park, num):
        super().__init__(name, temp, population, park)
        self.num = num

    def get_detail(self):
        return self.num

class Wakiso(Central):
    def __init__(self, name, temp, population, park, weather):
        super().__init__(name, temp, population, park)
        self.weather = weather

    def get_detail(self):
        return self.weather

#getting input for attributes 
city_name = input("Enter name of city: ")
city_temp = input("Enter temperature of city: ")
city_popn = input("Enter population of city: ")
city_park = input("Enter park name of city: ")        

print("Area is:")
print(Cities.area(5, 6000000))
#creating objects 
central = Central(city_name, city_temp, city_popn, city_park)
city = Cities(city_name, city_temp, city_popn, city_park)

#showing abstraction, inheritance
print(central) 

initial = central.name_to_initial(input("Enter initials of city name: "))
print(initial)


central.setCountry("Rwanda") #changing value of private variable

#inheriting parent methods
central.naming() 
central.popun()

#showing polymorphism
def print_detail(Central):
    print("{}'s details: {}".format(Central.get_name(), Central.get_detail()))

k = Kampala("Kamapala", 20, 200000, "centenary", "Numbers")
w = Wakiso("Wakiso", 15, 300000, "Ria", "Weather")

print(k)
print_detail(k)

print(w)
print_detail(w)
