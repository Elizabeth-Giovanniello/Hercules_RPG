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
    def restore_health(self):
        self.health = 100

    def increase_attack_power(self):
        self.attack_power += 1

    def select_attack(self):
        self.keys_list = list(self.attacks)
        num = 1
        print("Attack options menu: ")
        for item in self.keys_list:
            print(f"{str(num)}. {item}")
            num += 1
        self.attack_index = int(input("Enter the number of the attack you wish to use: ")) - 1
        

