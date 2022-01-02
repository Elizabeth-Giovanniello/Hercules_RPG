
class Enemy:
    def __init__(self, name, health, attack_power, attacks):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.attacks = attacks
    
    def enemy_attack(self):
        

    def injured(self, attack_points):
        self.health -= attack_points
        if self.health <= 0:
            print(f"The {self.name} cries out in pain. You see him grasp feebily at his wounds, as he wheezes his final breaths. He suddenly falls to the floor, at last succumbing to his injuries. You have defeated him!")
        else:
            self.attack() #TRYING TO CALL ITS OWN ATTACK METHOD WITHIN THE INJURY METHOD. FIX THIS LATER
