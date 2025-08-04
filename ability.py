# ability.py
import random

class Ability:


    
    def __init__(self, name, max_damage):
   	# implement code here
        self.name = name
        self.max_damage = max_damage

    def attack(self):
    # implement code here
        '''Return a random value between 0 and max_damage'''
        return random.randint(0, self.max_damage)


# testing!
fireball = Ability("Fireball", 500)
print(fireball.attack())
