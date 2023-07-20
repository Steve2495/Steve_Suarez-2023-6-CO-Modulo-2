import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, SPACESHIP_MOV, FONT, COUTER_FONT, SPACESHIP_SHIELD, SHOOT
from game.components.bullets import Bullet

pygame.init()
pygame.font.init()

class Spaceship(Sprite):
    scale_x, scale_y = 40, 60
    
    def __init__(self, label):
        super(Spaceship, self).__init__()
        self.label_1 = label
        self.hearts = 10
        self.deaths = 0
        self.type = 'player'
        self.asset = SPACESHIP
        self.asset = pygame.transform.scale(self.asset, (self.scale_x, self.scale_y))
        self.asset_rect = self.asset.get_rect()
        self.asset_rect.x, self.asset_rect.y = SCREEN_WIDTH // 2, SCREEN_HEIGHT - 80
        self.bullet = Bullet(self.type, self.asset_rect.x, self.asset_rect.y)
        self.label = FONT.render(f'PLAYER: {label}', True, (12, 159, 254))
        self.bullets = []
        self.k_state = 0
        self.buller_counter = 0
        self.shield = False
        self.cloack = False
        self.update_counter_text()
        self.shoot_effect = pygame.mixer.Sound(SHOOT)
        self.tricks_active = False
        self.spaceship_move = SPACESHIP_MOV
        self.incremented_once = False
        
    def manage_cloack(self):
        if self.cloack:
            self.asset = pygame.transform.scale(self.asset, (0, 0))
        
    def asset_spaceship(self, counter):
        if counter == 5:
            self.shield = True
            self.asset = SPACESHIP_SHIELD
            self.asset = pygame.transform.scale(self.asset, (self.scale_x + 20, self.scale_y + 10))
            return True
            
        else:
            self.shield = False
            self.asset = SPACESHIP
            self.asset = pygame.transform.scale(self.asset, (self.scale_x, self.scale_y))
            return False
            
        
    def move_left(self):
        if self.asset_rect.left > 0:
            self.asset_rect.left -= self.spaceship_move
        else:
            self.asset_rect.left = (SCREEN_WIDTH - self.scale_x)
            
    def move_right(self):
        if self.asset_rect.right < SCREEN_WIDTH:
            self.asset_rect.left += self.spaceship_move
        else:
            self.asset_rect.left = 0
            
    def move_up(self):
        if self.asset_rect.top > 0:
            self.asset_rect.top -= self.spaceship_move
            
    def move_down(self):
        if self.asset_rect.bottom < SCREEN_HEIGHT:
            self.asset_rect.bottom += self.spaceship_move
            
    def is_on_off(self, power):
        return 'On' if power else 'Off'
            
    def update_counter_text(self):
        self.desplaze_x = 7
        self.target_count = COUTER_FONT.render(f'KILLED_ENEMIES: {self.buller_counter}', True, (12, 159, 254))
        self.target_powers = COUTER_FONT.render('POWERS:', True, (12, 159, 254))
        self.target_power_1 = COUTER_FONT.render(f'Shield: {self.is_on_off(self.shield)}', True, (12, 159, 254))
        self.target_power_2 = COUTER_FONT.render(f'Cloack: {self.is_on_off(self.cloack)}', True, (12, 159, 254))

    def shoot(self):
        if not self.bullets or self.asset_rect.y - self.bullets[-1].rect.y > 50:
            self.shoot_effect.play()
            bullet = Bullet(self.type, self.asset_rect.x, self.asset_rect.y)
            self.bullets.append(bullet)
    
    def tricks(self, screen):
        if self.tricks_active:
            if self.tricks_active and not self.incremented_once:
                self.spaceship_move += 5
                self.incremented_once = True
            self.target_tricks = FONT.render('TRICKS ACTIVATED', True, (12, 159, 254))
            screen.blit(self.target_tricks, (0,0))
    
    def update(self, user_input): #determinate a key event, to call the respective method
        if user_input[pygame.K_LEFT]:
            self.move_left()
        if user_input[pygame.K_RIGHT]:
            self.move_right()
        if user_input[pygame.K_UP]:
            self.move_up()
        if user_input[pygame.K_DOWN]:
            self.move_down()
        if user_input[pygame.K_LCTRL] and user_input[pygame.K_F3] and user_input[pygame.K_j]:
            self.tricks_active = True
        if user_input[pygame.K_SPACE] and self.k_state == 0:
            self.shoot()
            self.k_state = 1

        if not user_input[pygame.K_SPACE]:
            self.k_state = 0    
    
        for e in self.bullets:
            e.update()
        for e in self.bullets:
            if e.rect.y < 0:
             self.bullets.remove(e)
        # self.bullet.update()

    def draw_components(self):
        desplazamiento_y = self.scale_y // 7
        self.elements_to_draw = [
            (self.label, (self.asset_rect.x - (self.scale_x // 2), self.asset_rect.y - (self.scale_y // 5))),
            (self.target_count, (self.asset_rect.x + self.scale_x, self.asset_rect.y + desplazamiento_y)),
            (self.target_powers, (self.asset_rect.x + self.scale_x, self.asset_rect.y + desplazamiento_y + 10)),
            (self.target_power_1, (self.asset_rect.x + self.scale_x + self.desplaze_x, self.asset_rect.y + desplazamiento_y + 20)),
            (self.target_power_2, (self.asset_rect.x + self.scale_x + self.desplaze_x, self.asset_rect.y + desplazamiento_y + 30))]

    def draw(self, screen, counter):
        self.update_counter_text()
        self.draw_components()
        self.tricks(screen)
        for element, position in self.elements_to_draw:
            screen.blit(element, position)
        if not self.asset_spaceship(counter):
            self.manage_cloack()
            screen.blit(self.asset, (self.asset_rect.x, self.asset_rect.y))
        else:
            screen.blit(self.asset, (self.asset_rect.x - 20, self.asset_rect.y))
        for e in self.bullets:
            e.draw(screen)

    