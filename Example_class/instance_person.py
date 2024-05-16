class Person:
# self -- instance of person class
    def __init__(self,name,designation ):
        self.name = name                    # atrributes / variables
        self.design = designation

# name & designation are attributes of the instance calling the greet method
    def greet(self):
        print(f"Hello, my name is {self.name} and I am working as {self.design}")

    def introduce(self, other_person):
        print(f"Hello, {other_person.name} I'm {self.name}. Nice to meet you")



















