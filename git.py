purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

def total_revenue(purchases):
    revenue = 0
    for i in purchases:
        revenue += i["price"] * i["quantity"]
    return revenue

def items_by_category(purchases):
    category_item = {}
    for i in purchases:
        category = i["category"]
        item = i["item"]
        if category not in category_item:
            category_item[category] = []

        if item not in category_item[category]:
            category_item[category].append(item)
    return category_item

def expensive_purchases(purchases, min_price):
    lst = []
    for i in purchases:
        if i["price"] > min_price:
            lst.append(i)
    return lst

def average_price_by_category(purchases):
    category_price = {}
    for i in purchases:
        category = i["category"]
        price = i["price"]
        if category not in category_price:
            category_price[category] = []
        if price not in category_price:
            category_price[category].append(price)
    for i in category_price:
        category_price[i] = sum(category_price[i])/len(category_price[i])
    return category_price

def most_frequent_category(purchases):
    sum_category = {}
    for key in purchases:
        category = key["category"]
        if category not in sum_category:
            sum_category[category] = key["quantity"]
        else:
            sum_category[category] += key["quantity"]
    best_category = ''
    best_category_sum = 0
    for key, values in sum_category.items():
        if values > best_category_sum:
            best_category_sum = values
            best_category = key
    return best_category

print(f'Общая выручка: {total_revenue(purchases)}') #не знаю, почему общая выручка в решении написано у вас 21, должно быть 23.5
print(f'Товары по категориям: {items_by_category(purchases)}')
print(f'Покупки дороже 1.0: {expensive_purchases(purchases, 1.0)}')
print(f'Средняя цена по категориям: {average_price_by_category(purchases)}')
print(f'Категория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}')