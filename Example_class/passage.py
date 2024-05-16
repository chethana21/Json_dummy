# para = """The Indian cricket team’s journey is a reflection of the nation’s evolving sporting culture. The team’s success has not only brought glory to the nation but also inspired countless young individuals to pursue cricket as a career. As the team continues to push the boundaries of cricketing excellence, the future of Indian cricket looks brighter than ever.

# In essence, the Indian cricket team is not just a group of players; it is a symbol of national pride, unity, and the indomitable spirit of India. The team’s journey from humble beginnings to global dominance is a testament to the power of perseverance, talent, and the unyielding spirit of a nation that lives and breathes cricket."""

# a = para.count('The')
# print(a)

class Emp:
    empid = (x for x in range(1,100000))
    def __init__ (self,name,age):
        self.name = name
        
        self.age = age
        self.empid = self.update()
    def update(self):
        print("Emp class update method"
              )
        return next (Emp.empid)
    
e1 = Emp("Chethun",24)
e1.__dict__

print(e1)