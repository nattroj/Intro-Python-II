# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.items = items if items else []
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
    
    def addItem(self, item):
        self.items.append(item)

    def viewContents(self):
        print(f'Contents: {", ".join(map(lambda x: x.name, self.items))}')
        print()