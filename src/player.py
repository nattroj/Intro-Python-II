# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
    
    def move(self, direction):
        if room := getattr(self.current_room, f'{direction}_to'):
            self.current_room = room
        else:
            print('Error: There is no room there!')
    
    def getItem(self, item_name):
        obtained = self.current_room.getItem(item_name)

        if obtained:
            self.inventory.append(obtained)
            obtained.on_take()
        else:
            print('Error: that item does not exist in this room')
    
    def dropItem(self, item_name):
        dropped = None
        for i, item in enumerate(self.inventory):
            if item_name == item.name:
                dropped = self.inventory.pop(i)
                break
        
        if dropped:
            self.current_room.addItem(dropped)
            dropped.on_drop()
        else:
            print('Error: that item is not in the inventory')


    def viewInventory(self):
        print('Inventory:')

        if not len(self.inventory):
            print('(empty)')
            print()
            return
        print("\n".join(map(lambda x: f'{x.name}: {x.description}', self.inventory)))