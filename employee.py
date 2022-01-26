class Employee:
    def __init__(self, firstName, lastName, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay
        self.email = firstName + '.' + lastName + '@gmail.com'
    
    def fullName(self):
        return f'{self.firstName} {self.lastName}'

emp1 = Employee('Thais','Queiroz',20000)
print(emp1)
emp1.fullName()
print(Employee.fullName(emp1))
