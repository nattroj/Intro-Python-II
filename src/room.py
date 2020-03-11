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
        print(f'Contents: {list(map(lambda x: x.name, self.items))}')
        print()


'''
# PYTHON
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

torch = Item('torch', 'light the way')
bag = Item('bag', 'holds things')

items = [torch, bag]

def getItemName(item):
    return f'{item.name}: {item.description}'

print(map(getItemName, items))

# JS
class Item {
    constructor(name, description) {
        this.name = name;
        this.description = description;
    }
}

const item1 = Item('torch', 'light the way')
const item2 = Item('bag', 'holds things')

console.log(item1.name)

const items = [torch, bag];

console.log(items.map(thingy => thingy.name));

'''