class Employee:
    
    # this is class attribute
 
    language = "py"
    salary  = 130000

awais = Employee()
awais.name = "awais" # this is an instance attribute 
print(awais.name, awais.language, awais.salary)

matee = Employee()
matee.name = "matee"  
print(matee.name, matee.language, matee.salary)

#here name is instance attribute and salary and name language are class attribute
#as they directly belong to the class