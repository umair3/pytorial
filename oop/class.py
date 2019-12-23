class Animal:
    """optional class documentation string"""
    count = 0

    def __init__(self, name):
        self.name = name
        Animal.count += 1

    def display(self):
        print(Animal.count)
        print(self.name)

    def __del__(self):
        print(__class__, "destroyed")

    pass


tiger = Animal("Tiger")
tiger.display()
cat = Animal("Cat")
cat.display()

print(Animal.__name__)
print(Animal.__module__)
print(Animal.__bases__)
print(Animal.__doc__)
print(Animal.__dict__)

