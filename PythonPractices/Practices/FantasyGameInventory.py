stuff = {'rope':7, 'torch':2,'gold coin':42,'dagger':1,'arrow':12}

def displayInventory(inventory):
    print("Inventory: ")
    item_total = 0

    for k,v in inventory.items():
        item_total = item_total + v
        print(f'{v} {k}' )
    print("Total Number of items: " + str(item_total))


displayInventory(stuff)

