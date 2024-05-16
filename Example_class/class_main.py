from variable import Person

# for accessing the class variable we need to access by CLASS.Variable name
# other way is to access the value of the class variable within the constructor, you can use self to access the class variable instead of using the class name
# print(self.Company_name)
print(Person.Company_Name)

# Creating the instances of the person class
person1 = Person("Chethana", "Project Engineer") # objects
person2 = Person("Arun", "Devops" )

person1.greet()      # greet is the method for person 1 & person 2
person2.greet()

person1.years(2)
person2.years(6)

# 
Person.Company_Name = "Wipro Limited"

print(Person.Company_Name)

person1.years(2)
person2.years(6)
# accessing the static method for getting the count of persons, the data will be coming from the instances
Person.total_persons()