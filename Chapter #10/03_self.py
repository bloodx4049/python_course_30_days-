class Employee:
    
    # this is class attribute
 
    namgetInfoe = "awais"
    language = "py"
    salary  = 130000

    def getInfo(self):
        print(f"the language is {self.language}. the salary is {self.salary}")

    @staticmethod
    def greet():
            print("good morning")

awais = Employee()
awais.language = "javaScript" # this is an instance attribute 
awais.greet()
awais.getInfo()
#Employee.getInfo
