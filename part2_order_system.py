
print()
print()
print("Task 1 — Explore the Menu")
# Restaurant menu data
menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}


print()
print("RESTAURANT MENU")
print("====================")

# categories list
categories = ["Starters", "Mains", "Desserts"]

# print menu category wise
for category in categories:
    print()
    print("===== " + category + " =====")
    print()

    for item in menu:
        if menu[item]["category"] == category:
            price = menu[item]["price"]
            available = menu[item]["available"]

           
            if available == True:
                status = "Available"
            else:
                status = "Unavailable"

            print(item, "₹" + format(price, ".2f"), "[" + status + "]")

print("_______________________________")
# total items in menu
total_items = len(menu)
print("\nTotal number of items on the menu:", total_items)

# count available items
available_count = 0
for item in menu:
    if menu[item]["available"] == True:
        available_count = available_count + 1

print("Total number of available items:", available_count)

# finding most expensive item
max_price = 0
max_item = ""

for item in menu:
    if menu[item]["price"] > max_price:
        max_price = menu[item]["price"]
        max_item = item

print("Most expensive item:", max_item, "₹" + format(max_price, ".2f"))

# items under 150
print("Items priced under ₹150:")

for item in menu:
    if menu[item]["price"] < 150:
        print(item, "₹" + format(menu[item]["price"], ".2f"))


print("--------------------------------------------------------------------------------------------------------------------------------")


#Task 2 

print()
print()
print("Task 2 — Cart Operations")
print()
menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

cart = []

# Add Paneer Tikka x 2
item_name = "Paneer Tikka"
quantity = 2

if item_name in menu:
    if menu[item_name]["available"] == True:
        found = False

        for item in cart:
            if item["item"] == item_name:
                item["quantity"] = item["quantity"] + quantity
                found = True
                break

        if found == False:
            cart.append({"item": item_name, "quantity": quantity, "price": menu[item_name]["price"]})

        print(item_name, "added to cart")
    else:
        print(item_name, "is unavailable")
else:
    print(item_name, "does not exist in menu")

print("Current Cart:")
if len(cart) == 0:
    print("Cart is empty")
else:
    for item in cart:
        print(item)
print()

print("___________________________________________________________")
# Add Gulab Jamun x 1
item_name = "Gulab Jamun"
quantity = 1

if item_name in menu:
    if menu[item_name]["available"] == True:
        found = False

        for item in cart:
            if item["item"] == item_name:
                item["quantity"] = item["quantity"] + quantity
                found = True
                break

        if found == False:
            cart.append({"item": item_name, "quantity": quantity, "price": menu[item_name]["price"]})

        print(item_name, "added to cart")
    else:
        print(item_name, "is unavailable")
else:
    print(item_name, "does not exist in menu")

print("Current Cart:")
if len(cart) == 0:
    print("Cart is empty")
else:
    for item in cart:
        print(item)
print()
print("___________________________________________________________")

# Add Paneer Tikka x 1
item_name = "Paneer Tikka"
quantity = 1

if item_name in menu:
    if menu[item_name]["available"] == True:
        found = False

        for item in cart:
            if item["item"] == item_name:
                item["quantity"] = item["quantity"] + quantity
                found = True
                break

        if found == False:
            cart.append({"item": item_name, "quantity": quantity, "price": menu[item_name]["price"]})

        print(item_name, "added to cart")
    else:
        print(item_name, "is unavailable")
else:
    print(item_name, "does not exist in menu")

print("Current Cart:")
if len(cart) == 0:
    print("Cart is empty")
else:
    for item in cart:
        print(item)
print()
print("___________________________________________________________")

# Try to add Mystery Burger
item_name = "Mystery Burger"
quantity = 1

if item_name in menu:
    if menu[item_name]["available"] == True:
        found = False

        for item in cart:
            if item["item"] == item_name:
                item["quantity"] = item["quantity"] + quantity
                found = True
                break

        if found == False:
            cart.append({"item": item_name, "quantity": quantity, "price": menu[item_name]["price"]})

        print(item_name, "added to cart")
    else:
        print(item_name, "is unavailable")
else:
    print(item_name, "does not exist in menu")

print("Current Cart:")
if len(cart) == 0:
    print("Cart is empty")
else:
    for item in cart:
        print(item)
print()
print("___________________________________________________________")
# Try to add Chicken Wings
item_name = "Chicken Wings"
quantity = 1

if item_name in menu:
    if menu[item_name]["available"] == True:
        found = False
         
 
        for item in cart:
            if item["item"] == item_name:
                item["quantity"] = item["quantity"] + quantity
                found = True
                break

        if found == False:
            cart.append({"item": item_name, "quantity": quantity, "price": menu[item_name]["price"]})

        print(item_name, "added to cart")
    else:
        print(item_name, "is unavailable")
else:
    print(item_name, "does not exist in menu")

print("Current Cart:")
if len(cart) == 0:
    print("Cart is empty")
else:
    for item in cart:
        print(item)
print()
print("___________________________________________________________")

# Remove Gulab Jamun
remove_item = "Gulab Jamun"
found = False

for item in cart:
    if item["item"] == remove_item:
        cart.remove(item)
        found = True
        print(remove_item, "removed from cart")
        break

if found == False:
    print(remove_item, "is not in cart")

print("Current Cart:")
if len(cart) == 0:
    print("Cart is empty")
else:
    for item in cart:
        print(item)
print()
print("___________________________________________________________")

# update quantity example
update_item = "Paneer Tikka"
new_quantity = 3
found = False

for item in cart:
    if item["item"] == update_item:
        item["quantity"] = new_quantity
        found = True
        print("Quantity updated for", update_item)
        break

if found == False:
    print(update_item, "is not in cart")

print("Current Cart:")
if len(cart) == 0:
    print("Cart is empty")
else:
    for item in cart:
          print(item)

print()
print("___________________________________________________________")



# Final Order Summary
print("========== Order Summary ==========")

subtotal = 0

for item in cart:
    item_total = item["quantity"] * item["price"]
    subtotal = subtotal + item_total
    print(item["item"], "x" + str(item["quantity"]), "₹" + format(item_total, ".2f"))

print("------------------------------------")

gst = subtotal * 0.05
total_payable = subtotal + gst

print("Subtotal: ₹" + format(subtotal, ".2f"))
print("GST (5%): ₹" + format(gst, ".2f"))
print("Total Payable: ₹" + format(total_payable, ".2f"))
print("====================================")


print()
print("--------------------------------------------------------------------------------------------------------------------------------")
print()
print()

print("Task 3 — Inventory Tracker with Deep Copy")
print()
print()
import copy

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

# final cart from task 2
cart = [
    {"item": "Paneer Tikka", "quantity": 3, "price": 180.0}
]

# making backup using deep copy
inventory_backup = copy.deepcopy(inventory)

# manual change to show backup stays safe

inventory["Paneer Tikka"]["stock"] = 2

print("Inventory after manual change:")
print("Paneer Tikka stock:", inventory["Paneer Tikka"]["stock"])

print("\nInventory backup:")
print("Paneer Tikka stock:", inventory_backup["Paneer Tikka"]["stock"])

inventory = copy.deepcopy(inventory_backup)

# restoring inventory
print("\nInventory restored:")
print("Paneer Tikka stock:", inventory["Paneer Tikka"]["stock"])

# deducting stock using final cart
for item in cart:
    item_name = item["item"]
    quantity = item["quantity"]

    if item_name in inventory:
        if inventory[item_name]["stock"] >= quantity:
            inventory[item_name]["stock"] = inventory[item_name]["stock"] - quantity
        else:
            print("Warning:", item_name, "has less stock")
            print("Only", inventory[item_name]["stock"], "unit(s) available")
            inventory[item_name]["stock"] = 0

# checking reorder alerts
print("\nReorder Alerts:")
alert_found = False

for item_name in inventory:
    stock = inventory[item_name]["stock"]
    reorder_level = inventory[item_name]["reorder_level"]

    if stock <= reorder_level:
        print("Reorder Alert:", item_name, "- Only", stock, "unit(s) left (reorder level:", reorder_level, ")")
        alert_found = True

if alert_found == False:
    print("No reorder alerts")

print("\nFinal Inventory:")
print("---------------------------------------------------------")
for item_name in inventory:
    print(item_name, "- Stock:", inventory[item_name]["stock"], "Reorder Level:", inventory[item_name]["reorder_level"])

print("\nInventory Backup:")
print("---------------------------------------------------------")
for item_name in inventory_backup:
    print(item_name, "- Stock:", inventory_backup[item_name]["stock"], "Reorder Level:", inventory_backup[item_name]["reorder_level"])
print()
print("--------------------------------------------------------------------------------------------------------------------------------")
print()
print()

#Task 4
print ("Task 4 — Daily Sales Log Analysis")
print()

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}

print("Revenue Per Day:")
print("___________________")

best_day = ""
highest_revenue = 0

for date in sales_log:
    day_total = 0

    for order in sales_log[date]:
        day_total = day_total + order["total"]

    print(date, "- ₹" + format(day_total, ".2f"))

    if day_total > highest_revenue:
        highest_revenue = day_total
        best_day = date

print("\nBest-selling day:", best_day, "- ₹" + format(highest_revenue, ".2f"))

# find most ordered item
item_count = {}

for date in sales_log:
    for order in sales_log[date]:
        for item in order["items"]:
            if item in item_count:
                item_count[item] = item_count[item] + 1
            else:
                item_count[item] = 1

most_ordered_item = ""
max_count = 0

for item in item_count:
    if item_count[item] > max_count:
        max_count = item_count[item]
        most_ordered_item = item

print("Most ordered item:", most_ordered_item, "-", max_count, "times")

# adding  new day
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
]

print("\nUpdated Revenue Per Day:")
print("_____________________________")

best_day = ""
highest_revenue = 0

for date in sales_log:
    day_total = 0

    for order in sales_log[date]:
        day_total = day_total + order["total"]

    print(date, "- ₹" + format(day_total, ".2f"))

    if day_total > highest_revenue:
        highest_revenue = day_total
        best_day = date

print("\nUpdated best-selling day:", best_day, "- ₹" + format(highest_revenue, ".2f"))

# making one list of all orders
all_orders = []


for date in sales_log:
    for order in sales_log[date]:
        all_orders.append([date, order])

print("\nNumbered List of All Orders:")
print("___________________________________")

for number, entry in enumerate(all_orders, start=1):
    date = entry[0]
    order = entry[1]
    items_text = ", ".join(order["items"])

    print(str(number) + ". [" + date + "] Order #" + str(order["order_id"]) + " - ₹" + format(order["total"], ".2f") + " - Items: " + items_text)
    print()
print("--------------------------------------------------------------------------------------------------------------------------------")