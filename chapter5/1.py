"""  
Fantasy Game Inventory
You are creating a fantasy video game. The data structure to model the
player’s inventory will be a dictionary where the keys are string values
describing the item in the inventory and the value is an integer value detailing how many of that item the player has. For example, the dictionary value
{'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the
player has 1 rope, 6 torches, 42 gold coins, and so on.
120 Chapter 5
Write a function named displayInventory() that would take any possible
“inventory” and display it like the following:
Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62
Hint: You can use a for loop to loop through all the keys in a dictionary.
# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayInventory(inventory):
 print("Inventory:")
 item_total = 0
 for k, v in inventory.items():
 # FILL THIS PART IN
 print("Total number of items: " + str(item_total))
displayInventory(stuff)
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

if __name__ == '__main__':

    newPlayer = Player({'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12})

    print(newPlayer.displayInventory())
    newPlayer.addSomething('rope', 90)
    print('*' * 50)
    print(newPlayer.displayInventory())

