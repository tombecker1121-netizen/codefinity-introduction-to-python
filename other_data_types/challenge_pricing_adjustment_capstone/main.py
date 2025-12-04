grocery_inventory = {
    "Milk": ("Dairy", 3.5, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)    
}
#manage eggs
#print("The price of Eggs is:", grocery_inventory["Eggs"][1])
if grocery_inventory["Eggs"][1] > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    old = grocery_inventory["Eggs"]
    new_price = old[1] -1    
    grocery_inventory["Eggs"] = (old[0], new_price,old[2])    
else:
    print("The price of Eggs is reasonable")
#add tomatoes
grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print("Inventory after adding Tomatoes:", grocery_inventory)
#check milk
print("The stock of Milk is:", grocery_inventory["Milk"][2])
if grocery_inventory["Milk"][2] < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    old = grocery_inventory["Milk"]
    new_stock = old[2] + 20
    grocery_inventory["Milk"] = (old[0], old[1], new_stock)
else:
    print("Milk has sufficient stock")
#manage apples
if grocery_inventory["Apples"][1] > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")
print("Updated inventory:", grocery_inventory)

    


    