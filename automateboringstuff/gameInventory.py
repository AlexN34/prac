def displayInventory(inventory):
   total = 0
   print('Inventory') 
   for k, v in inventory.items():
       print ("%d %s" % (v, k))
       total += v
   print ('Total number of unique items: %d' % (len(inventory))) #items has no len
   print ('Total inventory: %d' % (total)) #items has no len
#input: dict - inventory addedItems - list
def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(inventory)
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(inventory, dragonLoot)
displayInventory(inventory)
