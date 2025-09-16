"""
Demonstrate polymorphism by creating:

    A base class Animal with method move()
    Three derived classes: Fish, Bird, Dog with different implementations of move()
        fish swims, bird flies, dog runs
    A function that takes any animal and calls its move() method
"""

class Animal:
    def __init__(self,name):
        self.name = name

    def calls():
        pass

class Fish(Animal):
    def __init__(self,name):
        super().__init__(name)

    def calls(self):
        print("swim\n")

class Bird(Animal):
    def __init__(self,name):
        super().__init__(name)

    def calls(self):
        print("flies\n")

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)

    def calls(self):
        print("runs\n")


nemo = Fish("Nemo")
tweety = Bird("Tweety")
buddy = Dog("Buddy")

print(nemo.name)
nemo.calls()

print(tweety.name)
tweety.calls()

print(buddy.name)
buddy.calls()