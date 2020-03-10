class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f'you have picked up {self.name}.')

    def on_drop(self):
        print(f'you have dropped {self.name}.')