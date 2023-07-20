class Power:
    def __init__(self, power_shield_counter, flag_shield, hearts):
        self.i = 5
        self.power_shield_counter = power_shield_counter
        self.spaceship_shield = flag_shield
        self.spaceship_hearts = hearts
    
    def collisions_shield(self):
        self.i -= 1
        print('I:', self.i)
        if self.i == 0:
            self.power_shield_counter = 0
            self.i = 5
                
    def manage_shield(self):
        if not self.spaceship_shield:
            self.spaceship_hearts -=1
        else:
            self.collisions_shield()
        if self.power_shield_counter < 5:
            print('CORRECTO')
            self.power_shield_counter = 0