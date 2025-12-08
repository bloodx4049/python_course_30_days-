class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p = Programmer("awais", 135000, 4049)
print(p.name, p.salary, p.company)
p = Programmer("mati", 125000, 3039)
print(p.name, p.salary, p.company)
