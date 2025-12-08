class Animals:
    pass


class Pets(Animals):
    pass


class Dog(Pets):
    @staticmethod
    def bark():
        print("bow bow")

# Test the code
d = Dog()
Dog.bark()