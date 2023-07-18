from typing import Any
import pygame
from pygame.sprite import Sprite
from game.utils.constants import BULLET, BULLET_ENEMY, SCREEN_HEIGHT

bullets_assets = {'player': BULLET, 'enemy': BULLET_ENEMY}
bullet_player_scales = (15,20)
bullet_enemy_scales = (10,15)
bullet_movement = (5,4)

class Bullet(Sprite):
    def __init__(self, bullet_type, x_pos , y_pos):
        super().__init__()
        self.bullets = []
        self.bullet_type = bullet_type
        self.bullet_movement = bullet_movement[0] if self.bullet_type == "player" else bullet_movement[1]
        self.image = BULLET if self.bullet_type == "player" else BULLET_ENEMY
        self.image = pygame.transform.scale(self.image, bullet_player_scales if self.bullet_type == "player" else bullet_enemy_scales)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x_pos, y_pos
        self.counter = 0
        self.is_showable = False
            
    def add_bullet(self):
        if self.bullet_type == 'player' and self.is_showable :
                self.rect.y -= self.bullet_movement
        elif self.bullet_type == 'enemy' and self.is_showable:
            self.rect.y += self.bullet_movement
        
    def update(self):
        pass
        
    def draw(self, screen):
        if self.counter >= 1:
            if self.rect.y < SCREEN_HEIGHT:
                screen.blit(self.image, (self.rect.x, self.rect.y))
            else:
                self.is_showable = False
            

        
    
