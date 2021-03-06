# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self,name,descrp,n_to=None, s_to=None,
                 e_to=None, w_to=None, inventory=[]):
        self.name = name
        self.descrp = descrp
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.inventory = inventory

    def add_item(self, *item):
        self.inventory.append(item)


    def __str__(self):
        return f"{self.name}: {self.descrp}"
       