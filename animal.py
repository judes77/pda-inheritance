# Parent class - Animal
class Animal:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def animal_name(self):
        return f"{self.name} is such a lovely name."

    def feed_animals(self):
        return "Hope you're hungry!"

# Child class 1 - Cat
class Cat(Animal):
    def __init__(self, name, age, breed, fur, toy):
        super().__init__(name, age, breed)
        self.fur = fur
        self.toy = toy

    def feed_animals(self):
        return "Meow"

    def plays_with_toy(self):
        return f"{self.name} I can't seem to find your {self.toy} anywhere."
        
# Child class 2 - Chicken
class Chicken(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, breed)
        
    def feed_animals(self):
        return "cluck cluck cluck"

    def sell_chicken(self):
        return f"I'm sorry {self.name} but we wanted a Sebright not a {self.breed}."

# Test output - i.e. print class properties and methods to terminal
cat = Cat("Toby", 4, "tabby", "brown", "mouse")
print(cat.name)
print(cat.feed_animals())
print(Animal.animal_name(cat))
print(cat.plays_with_toy())
chicken = Chicken("Sheila", 2, "Brahma")
print(chicken.name)
print(Animal.animal_name(chicken))
print(chicken.sell_chicken())
