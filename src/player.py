# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    def __init__(self,name,initial):
        self.name = name
        self.currently = initial
        self.inventory = []


    def direction(self,coord):
        coordinates = {
            'n': self.currently.n_to, 's': self.currently.s_to,
            'e': self.currently.e_to,'w': self.currently.w_to}
        if coordinates[coord] != None:
            self.currently = coordinates[coord]

    def take_item(self, item):
        self.inventory.append(item)

    def drop_item(self, item):
        self.inventory.delete(item)
    

    def __str__(self):
        return f"{self.name}{self.currently}{self.inventory}"