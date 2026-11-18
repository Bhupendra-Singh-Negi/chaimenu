import random

product_item = []

names = [
    "Veg Sandwich",
    "Samosa",
    "Masala Dosa",
    "Veg Biryani",
    "Chole Bhature",
    "Paneer Roll",
    "Masala Chai",
    "Cold Coffee",
    "Fresh Lime Soda",
    "Mango Lassi"
]

categories = [
    "Snacks",
    "Snacks",
    "Breakfast",
    "Main Course",
    "Main Course",
    "Snacks",
    "Hot Drinks",
    "Cold Drinks",
    "Cold Drinks",
    "Cold Drinks"
]

descriptions = [
    "Grilled sandwich with fresh vegetables and chutney",
    "Crispy fried pastry stuffed with spiced potatoes",
    "Crispy rice crepe served with sambar and coconut chutney",
    "Fragrant basmati rice cooked with vegetables and spices",
    "Spicy chickpea curry served with fluffy fried bread",
    "Soft paratha wrapped around spiced paneer filling",
    "Traditional Indian tea brewed with milk and spices",
    "Chilled coffee blended with milk and ice cream",
    "Refreshing lime drink with soda, sweet or salted",
    "Thick and creamy yogurt drink blended with mango"
]

for i in range(1, 10001):

    index = random.randint(0, 9)

    product = {
        "id": i,
        "name": names[index],
        "category": categories[index],
        "description": descriptions[index],
        "available": random.choice([True, False])
    }

    product_item.append(product)

print("Total Products:", len(product_item))
print(product_item[:5])