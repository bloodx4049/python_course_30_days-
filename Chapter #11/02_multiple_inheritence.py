class Employee: #this is base class
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"the name of the employee is {self.name} and the company is {self.company}")

class Coder:
    language = "python"
    def printLanguage(self):
        print(f"out of the all language here is your language: {self.language}")


class Programmer(Employee, Coder): # this is an inheretence class
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"the name is {self.company} and he is good with {self.language} language")
a = Employee()
b = Programmer()

print(a.company, b.company)
b.show()
b.showLanguage()
b.printLanguage()