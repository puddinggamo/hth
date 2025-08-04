import random 
from ability import Ability
from armor import Armor 

class Hero:
    def __init__(self, name, starting_health=100):
        '''Initialize Hero with a name and health values'''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = [] 
        self.armor = []

    def battle(self, opponent): 	
        '''Fight another hero and randomly declare a winner'''
        # add your implementation here
        winner = random.choice([self.name, opponent.name])
        print(f"the winner is {winner}")

    def add_ability(self, ability):
        '''
        This method should allow you to add an ability to the hero’s abilities list. You’ll be appending the Ability object passed into the method to the hero’s list of abilities.
        '''
        self.abilities.append(ability)
        

    def add_armor(self, armor):
        self.armor.append(armor)

    def sum_of_attacks(self):
        '''
        This method will loop through all the abilities stored in the hero’s abilities list and call each ability's attack() method to calculate total damage.
        After looping through all abilities, this method should return the total damage value, which is the sum of all individual attacks.
        Remember, each ability is a class and has its own attack method. How do we use this for our purposes here? 
        '''
        total_damage = 0 
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage 
    
    def defend(self):

        total_defense = 0 
        for armor in self.armor:
            total_defense += armor.block()
        return total_defense 
    
    def take_damage(self, damage): 
    
        defense_amount = self.defend()
        damage_taken = max(0, damage - defense_amount)
        self.current_health -= damage_taken 

    def is_alive(self):
        return self.current_health > 0 
    


# Testing Section 
if __name__ == "__main__":
    # Test abilities
    print("--- Testing Abilities ---")
    hero1 = Hero("Wonder Woman", 150)
    ability1 = Ability("Lasso of Truth", 70)
    ability2 = Ability("Bracelets of Submission", 40)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    print(f"{hero1.name}'s total attack damage: {hero1.sum_of_attacks()}") # Expect a random number

    # Test armor
    print("\n--- Testing Armor ---")
    hero2 = Hero("Iron Man", 200)
    armor1 = Armor("Iron Suit", 80)
    armor2 = Armor("Iron Suit Helmet", 30)
    hero2.add_armor(armor1)
    hero2.add_armor(armor2)
    print(f"{hero2.name}'s total defense: {hero2.defend()}") # Expect a random number

    # Test take_damage and is_alive
    print("\n--- Testing Damage and Health ---")
    hero3 = Hero("Captain America", 120)
    shield = Armor("Vibranium Shield", 60)
    hero3.add_armor(shield)

    print(f"{hero3.name} starts with {hero3.current_health} health.")
    hero3.take_damage(50)
    print(f"{hero3.name} takes 50 damage (with defense). Current health: {hero3.current_health}")
    print(f"Is {hero3.name} alive? {hero3.is_alive()}")

    hero3.take_damage(100) # Take more damage to potentially defeat the hero
    print(f"{hero3.name} takes 100 more damage. Current health: {hero3.current_health}")
    print(f"Is {hero3.name} alive? {hero3.is_alive()}")

    hero4 = Hero("Deadpool", 50)
    hero4.take_damage(20)
    print(f"{hero4.name} current health: {hero4.current_health}")
    print(f"Is {hero4.name} alive? {hero4.is_alive()}")
    hero4.take_damage(60) # Should be enough to defeat Deadpool
    print(f"{hero4.name} current health: {hero4.current_health}")
    print(f"Is {hero4.name} alive? {hero4.is_alive()}")

    # Test battle (simplified)
    print("\n--- Testing Battle ---")
    hero1.battle(hero2)

    # Now we have added our abilities, next are our armors. Just like before, we will need to add two methods to our hero class, one that lets us add_armor(self, armor) and another that allows our hero to defend(self) themselves. These will be very similar to the two methods we just wrote. Make sure you are testing them once you finish writing.
