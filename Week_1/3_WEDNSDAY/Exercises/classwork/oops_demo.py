print(" ")
print(" ")

class Dog:

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        return f"{self.name} says : WOOF"
    
    def describe(self):
        return f"{self.name} is a {self.age} year old {self.breed}"
    



# d=Dog(
# print(type(d))

Rex=Dog("Rex", "German Shepard", 3)
print(Rex.name)
print(Rex.describe())
print(Rex.bark())

luna = Dog("Luna", "Golden Retriever", 5)
print(luna.describe())

print(" ")
print(" ")
