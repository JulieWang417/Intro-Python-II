class Item:
    def __init__(self, name, descrp):
        self.name = name
        self.descrp = descrp

    def on_take(self):
        print(f"You took the {self.name}.")

    def on_drop(self):
        print(f"You dropped the {self.name}.")

    def __str__(self):
        return f"{self.name}: {self.descrp}"