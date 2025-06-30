menu = {'pizza':2.99, 'burger': 3.99, 'Hot dog': 1.99, 'cheese':0.59, 'ice cream': 1.49, 'churro': 0.79, 'soda':0.89}
def total_price(cheese, ice cream):
"""
calculates the total price of two menu items

Args:
cheese (str): The name of the pizza.
ice cream (str): The name of the burger.

Returns: 
float: The sum of te prices of the two items.
"""
price1 = menu[item1_name]
price2 = menu[item2_name]
total = price1 + price2
return total