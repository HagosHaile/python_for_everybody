class PartyAnimal:

   def __init__(self, nam):
     self.x = 0
     self.name = nam
     print(self.name,'constructed')

   def party(self) :
     self.x = self.x + 1
     print(self.name,'party count',self.x)

an = PartyAnimal('Daniel')
an.party()
# print(type(an))

#print(dir(an))

# user_defined = [attr for attr in dir(an) if not attr.startswith('__')]
# print(user_defined)
