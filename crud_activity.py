1. cookbook = []

def create(recipe):
    cookbook.append(recipe)
    print(cookbook)

create("pancakes")
create("pizza")
create("lagsana")

def read(index):
    item = cookbook[index]
    print(item)

read(2)

def update(index,recipe):
    cookbook[index] = recipe
    print(cookbook)
    
update(0, "bear")