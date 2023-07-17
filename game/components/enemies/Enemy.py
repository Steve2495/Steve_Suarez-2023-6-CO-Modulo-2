import pygame
import random
import secrets

from game.utils.constants import ENEMY_1, ENEMY_2, SCREEN_WIDTH, SCREEN_HEIGHT, FONT
from pygame.sprite import Sprite

scales_enemies = [(40, 60), (50, 70)]
mov = 15

class Enemy(Sprite):
    def __init__(self, label, movement, enemy):
        super(Enemy, self).__init__()
        x_pos_init = [SCREEN_WIDTH - scales_enemies[enemy][0]-20, SCREEN_WIDTH / 1.5, SCREEN_WIDTH / 2, SCREEN_WIDTH / 3, SCREEN_WIDTH / 4, SCREEN_WIDTH / 5, SCREEN_WIDTH / 6, SCREEN_WIDTH / 7, 0]
        self.enemy = enemy
        self.enemies = [ENEMY_1, ENEMY_2]
        self.enemies = pygame.transform.scale(self.enemies[self.enemy], scales_enemies[self.enemy])
        self.rect_enemy = self.enemies.get_rect()
        self.rect_enemy.x, self.rect_enemy.y = (x_pos_init[random.randint(0, 8)], 0)
        self.label = FONT.render(f'ENEMY: {label}', True, (240, 50, 50))
        self.movement = movement
        self.cont = 0
        self.movement_x = random.randint(50, 100) #select the 
        self.rand = secrets.choice([True, False]) #flag to move at the left or right
        
    def movement_enemy(self):
        self.cont += 1
        if (self.cont >= self.movement_x and not self.rand) or (self.rect_enemy.x <= 0):
            self.rand = True
            
        elif (self.cont >= self.movement_x and self.rand) or (self.rect_enemy.x >= SCREEN_WIDTH - scales_enemies[self.enemy][1]):
            self.rand = False
            
        if self.cont >= self.movement_x:
            self.cont = 0
        
    def update(self):
        self.rect_enemy.y += self.movement - 2
        
        if self.rand:
            self.rect_enemy.x += self.movement 
            self.movement_enemy()
            
        else:
            self.rect_enemy.x -= self.movement
            self.movement_enemy()

    def draw(self, screen):
        if self.rect_enemy.y <= SCREEN_HEIGHT:
            screen.blit(self.enemies, (self.rect_enemy.x, self.rect_enemy.y))
            screen.blit(self.label, (self.rect_enemy.x - (scales_enemies[self.enemy][0] / 3.8), self.rect_enemy.y - (scales_enemies[self.enemy][1] // 6)))
            self.update()