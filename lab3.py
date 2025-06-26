# Lab 3 

# Task 1: Working with strings
food = 'Pesto Sandwhich'
print(food[:3])
print(food[-3:])
first_last = food [0] + food[-1]
print(first_last)
food_list = food.split()
print(food_list)
joined_food = ''.join(food_list)
print(joined_food)



# Task 2: Working with Lists
number_list = [45, 98767, -344, 0, 1]
number_list.append(3)
print(number_list)
number_list.insert(3,-10000000001)
print(number_list)
number_list.pop()
print(number_list)
number_list.remove(98767)
print(number_list)
print(number_list[:3])
print(number_list[-3:])

 # Task 3: Working with dictionary 

books = {'Dr. Seuss': 'Cat in the Hat', 'JK Rowling': 'Harry Potter','Suzanne Collin':'The Hunger Games', 'Jeff Kinne': 'Diary of the Wimpy Kid'}
print(books.keys())
print(books.values()) 
print(books.get('Dr. Seuss'))
books.pop('Suzanne Collin')
print(books)
del books['Dr. Seuss']
print(books)