from instance_person import Person

# Creating the instances of the person class
person1 = Person("Chethana", "Project Engineer") # objects
person2 = Person("Arun", "Devops" )

# Access attributes of the instances 
print(person1.name)    # name is the attributes of person1 (instances)
print(person2.design)  # design is the attributes of person2 

person1.greet()      # greet is the method for person 1 & person 2

person2.greet()


person1.introduce(person2)
person2.introduce(person1)

