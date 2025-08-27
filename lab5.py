# Lab 5 Candy Tang 

# step 1 Cat Function
def cat_greeting(word):
    print(f'Cat says meow')
    print('Cat says nothing')

cat_greeting("meow")

# Step 2 superhero
def generate_superhero_power():
    name = "Johnny"
    power = "flying"
    print(f"{name}'s power is {power}")

generate_superhero_power()

# Step 3 
def generate_superhero_power1():
    power = "Flying"
    return power

print (generate_superhero_power1())

# Step 4
def generate_superhero_power2(user_name, super_power):
    message = user_name + "has the power of" + super_power + "!"
    return message 

print(generate_superhero_power2("Jannifer", "telakinesis", "super strength", "mind control"))

# Step 5 
def cat_greeting_loop():
     for i in range(5):
        print(f'The cat says {greeting}')
        greetings = ["meow", "mo", "Meoiiw", "pur", "screech"]

        for i in greetings:
            print(" The cat says", i)

cat_greeting_loop()

    # Step 6 
def generate_multiple_power(powers):
        for i in powers:
            print()

powers_tests = ["flying","telakenesis", "super strength", "mind control"]

generate_multiple_power(powers_tests) 
