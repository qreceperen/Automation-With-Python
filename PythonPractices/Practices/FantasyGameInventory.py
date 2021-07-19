
'''Setdefault komutunu ogren'''

# displayInventory(stuff)

'''Write a function that update inventory from a list of loots.'''


##### SOLUTION ######


#  Problem: List to Dictionary Function for Fantasy Game Inventory
#  The url of the problem: https://automatetheboringstuff.com/chapter5/
 
def displayInventory(inventory):
    print('Inventory:')
    print('----------')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('\nTotal number of items: ' + str(item_total))
    
def addToInventory(inventory, addedItems):
    for Item in addedItems:
        inventory.setdefault(Item,0)
        inventory[Item] += 1
    return inventory

 
# inventory and addedItems
inv = {'gold coin': 42, 'rope': 1}
dragonloot = ['gold coin', 'dragger', 'gold coin', 'gold coin', 'ruby','rusty sword','dragon teeth'] 
 
# Update the inventory
inv = addToInventory(inv, dragonloot)
displayInventory(inv)