# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def viewInventory(self):
        print('Inventory:')
        if not len(self.inventory):
            print('(empty)')
            print()
            return

        print("\n".join(map(lambda x: x.name, self.inventory)))
        print()