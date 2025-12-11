class Employee:
    
    # this is class attribute
 
    language = "py"
    salary  = 130000

    def getInfo():
        print

awais = Employee()
awais.language = "javaScript" # this is an instance attribute 
print(awais.language, awais.salary)
