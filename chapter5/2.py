"""  
List to Dictionary Function for Fantasy Game Inventory
Imagine that a vanquished dragon’s loot is represented as a list of strings
like this:
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
Write a function named addToInventory(inventory, addedItems), where the
inventory parameter is a dictionary representing the player’s inventory (like
in the previous project) and the addedItems parameter is a list like dragonLoot.
The addToInventory() function should return a dictionary that represents the
updated inventory. Note that the addedItems list can contain multiples of the
same item. Your code could look something like this:
def addToInventory(inventory, addedItems):
 # your code goes here
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
Dictionaries and Structuring Data 121
The previous program (with your displayInventory() function from the
previous project) would output the following:
Inventory:
45 gold coin
1 rope
1 ruby
1 dagger
Total number of items: 48

"""

class Player:

    def __init__(self, inventory):
        self.inventory = inventory

    def displayInventory(self):
        print('INVENTORY')
        print('*' * 50)
        total = 0
        for k,v in self.inventory.items():
            print(f'{k} = {str(v)}')
            total += v
        return f'Total of items {total}'

    def addSomething(self, keyValue, number = 1):
        try:
            self.inventory[keyValue] = number
        except KeyError:
            return 'No key'

    def addToInventory(self, itemsAdded):
        
        for i in sorted(itemsAdded):
            if i in self.inventory.keys(): 
                self.inventory[i] += 1
            else:
                self.inventory[i] = 1

if __name__ == '__main__':

    newPlayer = Player({'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12})

    newPlayer.addToInventory(['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'])
    newPlayer.addToInventory(['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'])
    print(newPlayer.displayInventory())

