control_variable = "yes"

while continue_checking == "yes":
    print("what is your age?")
    user_input = input()
    if user_input >= 18:
        print("yes you can vote")
    else:
        print("you can't vote")
        print("Would you like to check another age?")
        user_input2 = input()
        checking = user_input2
list1 = [3,-1,0,6,-4,]

for x in list1:
        if x > 0:
            print("Value s positive")
        elif x <= 0:
                print("Number is zero")
        else:
                print("Number is zero")

inventory = ["tnt", "glass", "grass", "netherite", "Waxed Lightly weathered Chiseled Copper Stairs"]

for item in range(inventory):
    if item == "Waxed Lightly weathered Chiseled Copper Stairs":
        print("Why do you have this in your inventory?")
    elif item == "tnt":
        print("Go bomb Johnny house")    
