
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

# printing heading
print()
print("RESTAURANT MENU")
print("====================")

# list of categories
categories = ["Starters", "Mains", "Desserts"]

# print menu category wise
for category in categories:
    print()
    print("------------------------------")
    print("\n        " + category + "        ")
    print("-------------------------------")
    print()

    for item in menu:
        if menu[item]["category"] == category:
            price = menu[item]["price"]
            available = menu[item]["available"]

            # checking availability
            if available == True:
                status = "Available"
            else:
                status = "Unavailable"

            print(item, "₹" + format(price, ".2f"), "[" + status + "]")

print("_______________________________")
# total number of items in menu
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

# print items under 150
print("Items priced under ₹150:")

for item in menu:
    if menu[item]["price"] < 150:
        print(item, "₹" + format(menu[item]["price"], ".2f"))

#First, I stored all menu items in a dictionary.
#Then I made a list of categories: Starters, Mains, and Desserts.
#I used nested loops to print items category-wise.
#After that, I used len(menu) to count total items.
#Then I counted available items using a loop and if condition.
#To find the most expensive item, I compared prices one by one.
#Finally, I printed all items whose price is less than 150.