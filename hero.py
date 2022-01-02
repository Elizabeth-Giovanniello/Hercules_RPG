import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 1
        self.attacks = {
            "Jab with sword": 5,
            "Chop neck with sword": 10,
            "Throw sword": 20,
            "Punch": 1,
            "Kick": 2
        }
        self.throw_accuracy = 3
    def restore_health(self):
        self.health = 100

    def increase_attack_power(self):
        self.attack_power += 1

    def select_attack(self):
        self.attack_keys_list = list(self.attacks)  #list of just the names of the attacks without their values
        self.attack_values = list(self.attacks.values())
        num = 1
        print("Attack options menu: ")
        for item in self.attack_keys_list:
            print(f"{str(num)}. {item}")
            num += 1
        self.attack_index = int(input("Enter the number of the attack you wish to use: ")) - 1 #may come back and make it so that if the inputted number is greater or less than the length of the list, it says it's invalid and runs the method again
        if self.attack_index == 2:
            if random.randint(10) > self.throw_accuracy:
                print("You throw your sword with all your might at your opponent. It soars through the air with deadly speed and power... and flies right past your enemy, disappearing into the misty lake behind him. Your overconfidence in your throwing abilities has just cost you your only weapon. ")
                for item in self.attacks:
                    if "sword" in item:  #removing all sword options for the attack menu because sword has been lost
                        self.attacks.remove(item)
            else:
                print("Knowing it may be your only chance to defeat your enemy, you launch your sword into the air like a javelin. It cuts through the air with unbelievable speed... and with a deafening thud lands squarely in your enemy's chest. ")
                #OK NOW WE HAVE TO MAKE IT SO THAT THE ENEMY IS WOUNDED BY THE CHOICE. SO GO CREATE A CLASS FOR THE ENEMY AND INCLUDE AN INJURY METHOD

