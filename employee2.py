class Employee:
      nums_of_emp = 0
      raise_amount = 1.04
      
      def __init__(self, first, last, pay):
        self.first = first 
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
      
        Employee.nums_of_emp += 1
      
      def fullName(self):
        return f'{self.first} {self.last}'
      
      def applyRaise(self):
          self.pay =  int(self.pay * self.raise_amount)
 
emp1 =  Employee('Thais','Queiroz',5000)
emp2 =  Employee('Pedro','Rodrigues',15000)
 
print(Employee.fullName(emp2))
 
print(emp2.pay)
emp2.applyRaise()
print(emp2.pay)
print()
 
print(Employee.__dict__)
print(emp1.__dict__)
print()
 
emp1.applyRaise = 2.0
print(emp1.__dict__)
print(emp1.applyRaise)
 
print(Employee.nums_of_emp)
