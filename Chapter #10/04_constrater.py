class Employee:
    
    # this is class attribute
 
    namgetInfoe = "awais"
    language = "py"
    salary  = 130000


    def __init__(self, name, salary, language): #dunder methods which is automatically called 
         self.name = name 
         self.salary = salary
         self.language = language
         print("i am creating a object")

    def getInfo(self):
        print(f"the language is {self.language}. the salary is {self.salary}")

    @staticmethod
    def greet():
            print("good morning")

awais = Employee("awais", 120000, "javascript")
# awais.name = ("awais")
print(awais.name, awais.salary, awais.language)
#Employee.getInfo
