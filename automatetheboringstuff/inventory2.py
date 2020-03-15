def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i not in inventory.keys():
            inventory[i] = 1
        else:
            inventory[i]+=1
    return inventory

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    
    for k, v in inventory.items():
        item_total+=v
        print(str(v) + " " + k)
    print("Total number of items: "  + str(item_total))

inv = {"gold coin" : 42, "rope":1}
dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
inv = addToInventory(inv,dragonLoot)
displayInventory(inv)
