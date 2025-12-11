class Employee: #this is base class
    company = "ITC"
    def show(self):
        print(f"the name of the employee is {self.name} and the salary is {self.salary}")


# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#          print(f"the name is {self.name} and the salary is {self.salary}")

#          def show_anguage(self):
#               print(f"the name is {self.name} and the salary is {self.salary}")

class Programmer(Employee): # this is an inheretence class
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"the name is {self.name} and he is good with {self.language} language")
a = Employee()
b = Programmer()

print(a.company, b.company)