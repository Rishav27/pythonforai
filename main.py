class Dog:
  def __init__ (self, name, breed):
    self.name = name
    self.breed = breed
  def bark(self):
    print( f"{self.name} woof!")

dog1 = Dog("tommy", "bulldog")
dog2 = Dog("rocky", "labrador")

print(dog1.name,dog1.breed)
print(dog2.name,dog2.breed)
dog1.bark()
print(dog1.breed)
dog2.bark()
print(dog2.breed)