# stuff = {'rope':7, 'torch':2,'gold coin':42,'dagger':1,'arrow':12}

# def displayInventory(inventory):
#     print("Inventory: ")
#     item_total = 0

#     for k,v in inventory.items():
#         item_total = item_total + v
#         print(f'{v} {k}' )
#     print("Total Number of items: " + str(item_total))


# displayInventory(stuff)

'''Write a function that update inventory from a list of loots.'''

def addToInventory (inventory, addedItems):
    print("Inventory:")
    print('----------')
    item_total = 0

    for k,v in inventory.items():
        item_total = item_total + v 
        print(f'{k} {v}')
    #Write Code here

    # We need to Iterate over list and update the dictionary according to the list. HOW???!!!

inv = {"gold coin":42, 'rope':1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(inv,dragonLoot)
