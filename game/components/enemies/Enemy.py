import pygame
import random
import secrets

from game.utils.constants import ENEMY_1, ENEMY_2, SCREEN_WIDTH, SCREEN_HEIGHT, FONT
from pygame.sprite import Sprite

scales_enemies = [(40, 60), (50, 70)]
mov = 15
movement_x = [mov, mov*2, mov*3, mov*4, mov*5, mov*6, mov*7, mov*8]

class Enemy(Sprite):
    def __init__(self, label, movement, enemy):
        super(Enemy, self).__init__()
        x_pos_init = [0, SCREEN_WIDTH / 1, SCREEN_WIDTH / 2, SCREEN_WIDTH / 3, SCREEN_WIDTH / 4, SCREEN_WIDTH / 5, SCREEN_WIDTH / 6, SCREEN_WIDTH / 7, SCREEN_WIDTH - scales_enemies[enemy][0]-20]
        self.enemy = enemy
        self.enemies = [ENEMY_1, ENEMY_2]
        self.enemies = pygame.transform.scale(self.enemies[self.enemy], scales_enemies[self.enemy])
        self.rect_enemy = self.enemies.get_rect()
        self.rect_enemy.x, self.rect_enemy.y = (x_pos_init[random.randint(0, 8)], 0)
        self.label = FONT.render(f'ENEMY: {label}', True, (240, 50, 50))
        self.movement = movement
        self.cont = 0
        self.movement_pixels = 0  # Contador de píxeles movidos
        
    def moving(self):
        #print('CONTADOR:', self.cont)
        if self.cont == 0:
            self.movement_x = random.randint(20, 100)
            self.rand = secrets.choice([True, False])
        
    def movement_enemy(self):

        self.moving()
        #print('CONTADOR:', self.cont, 'MOV_X:', self.movement_x)
        #print('FLAG',self.rand)

        if (self.cont <= self.movement_x and self.rand) or (self.rect_enemy.x <= 0):
            self.cont += 1
            self.move_right()
            
        elif (self.cont <= self.movement_x and not self.rand) or (self.rect_enemy.x >= SCREEN_WIDTH - scales_enemies[self.enemy][1]):
            self.cont += 1
            self.move_left()
            
        else:
            self.cont = 0
            
        print('WIDTH', SCREEN_WIDTH, 'POSI', self.rect_enemy.x)
            
    def move_left(self):
        self.rect_enemy.x -= self.movement
    
    def move_right(self):
        self.rect_enemy.x += self.movement
        
    def move_down(self):
        self.rect_enemy.y += self.movement

    def draw(self, screen):
        if self.rect_enemy.y <= SCREEN_HEIGHT:
            screen.blit(self.enemies, (self.rect_enemy.x, self.rect_enemy.y))
            screen.blit(self.label, (self.rect_enemy.x - (scales_enemies[self.enemy][0] / 3.8), self.rect_enemy.y - (scales_enemies[self.enemy][1] // 6)))
            self.move_down()
            self.movement_enemy()