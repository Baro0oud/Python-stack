class Animal:
    def __init__(self, name, age, health=100, happiness=100):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Health: {self.health}, Happiness: {self.happiness}")

    def feed(self):
        self.health += 10
        self.happiness += 10


class Lion(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, health=90, happiness=80)


class Tiger(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, health=80, happiness=70)


class Bear(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, health=70, happiness=60)


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self, animal):
        self.animals.append(animal)

    def print_all_info(self):
        print("-" * 30, self.name, "-" * 30)
        for animal in self.animals:
            animal.display_info()


# Create a zoo
zoo1 = Zoo("John's Zoo")

# Add animals to the zoo
zoo1.add_animal(Lion("Nala", 5))
zoo1.add_animal(Lion("Simba", 4))
zoo1.add_animal(Tiger("Rajah", 6))
zoo1.add_animal(Tiger("Shere Khan", 7))
zoo1.add_animal(Bear("Baloo", 8))

# Feed the animals
for animal in zoo1.animals:
    animal.feed()

# Display information about all animals in the zoo
zoo1.print_all_info()
