class House(object):
    def accept(self,visitor):
        visitor.visit(self)

    def work_on_hvac(self, hvac_specialist):
        print(self, "worked on by ", hvac_specialist)
    
    def work_on_electricity(self, electrician):
        print(self, "worked on by ", electrician)

    def __str__(self):
        return self.__class__.__name__

class Visitor(object):
    def __str__(self):
        return self.__class__.__name__

class HvacSpecialist(object):
    def visit(self, house):
        house.work_on_hvac(self)

class Electrician(object):
    def visit(self, house):
        house.work_on_electricity(self)

hv = HvacSpecialist()
e = Electrician()

# Create a house
home = House()

# Let the house accept the hvac specialist
home.accept(hv)
home.accept(e)