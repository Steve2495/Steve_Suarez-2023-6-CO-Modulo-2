import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, SPACESHIP_MOV, FONT, COUTER_FONT
from game.components.bullets import Bullet

pygame.init()
pygame.font.init()

class Spaceship(Sprite):
    scale_x, scale_y = 40, 60
    
    def __init__(self, label):
        super(Spaceship, self).__init__()
        self.type = 'player'
        self.asset = SPACESHIP
        self.asset = pygame.transform.scale(self.asset, (self.scale_x, self.scale_y))
        self.asset_rect = self.asset.get_rect()
        self.asset_rect.x, self.asset_rect.y = SCREEN_WIDTH // 2, SCREEN_HEIGHT - 80
        self.label = FONT.render(f'PLAYER: {label}', True, (12, 159, 254))
        self.bullet = Bullet(self.type, self.asset_rect.x, self.asset_rect.y)
        self.bullets = []
        self.k_state = 0
        self.buller_counter = 0
        self.update_counter_text()
        
    def move_left(self):
        if self.asset_rect.left > 0:
            self.asset_rect.left -= SPACESHIP_MOV
        else:
            self.asset_rect.left = (SCREEN_WIDTH - self.scale_x)
            
    def move_right(self):
        if self.asset_rect.right < SCREEN_WIDTH:
            self.asset_rect.left += SPACESHIP_MOV
        else:
            self.asset_rect.left = 0
            
    def move_up(self):
        if self.asset_rect.top > 0:
            self.asset_rect.top -= SPACESHIP_MOV
            
    def move_down(self):
        if self.asset_rect.bottom < SCREEN_HEIGHT:
            self.asset_rect.bottom += SPACESHIP_MOV
            
    def update_counter_text(self):
        self.target_count = COUTER_FONT.render(f'BULLETS: {self.buller_counter}', True, (12, 159, 254))

    def shoot(self):
        if not self.bullets or self.asset_rect.y - self.bullets[-1].rect.y > 50:
            bullet = Bullet(self.type, self.asset_rect.x, self.asset_rect.y)
            self.bullets.append(bullet)
            self.buller_counter += 1
            self.update_counter_text()
    
    def update(self, user_input): #determinate a key event, to call the respective method
        if user_input[pygame.K_LEFT]:
            self.move_left()
        if user_input[pygame.K_RIGHT]:
            self.move_right()
        if user_input[pygame.K_UP]:
            self.move_up()
        if user_input[pygame.K_DOWN]:
            self.move_down()
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

    def draw(self, screen):
        screen.blit(self.label, (self.asset_rect.x - (self.scale_x // 2), self.asset_rect.y - (self.scale_y // 5)))
        screen.blit(self.target_count, (self.asset_rect.x + self.scale_x, self.asset_rect.y + (self.scale_y // 7)))
        screen.blit(self.asset, (self.asset_rect.x, self.asset_rect.y))
        for e in self.bullets:
            e.draw(screen)

    