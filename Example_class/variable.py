class Person:
#company name variable is a class variable, and it is shared among all instances of the person class.
    Company_Name = "Wipro"
    Total_number_of_person = 0
    
    def __init__(self,name,designation):
        self.name = name
        self.design = designation
        Person.Total_number_of_person +=1
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I am working as {self.design}")
    
    def years(self,experience):
        print(f"Hi this is {self.name}, I have {experience} years of experience from {Person.Company_Name}")
    
    @staticmethod
    def total_persons():
        print(f'Total Number of persons {Person.Total_number_of_person}')
