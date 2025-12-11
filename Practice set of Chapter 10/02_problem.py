class Calculater:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"the square is {self.n*self.n}")
    def cube(self):
        print(f"the square is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"the square is {self.n**1/2}")


a = Calculater(4)
a.square()
a.cube()
a.squareroot()
    