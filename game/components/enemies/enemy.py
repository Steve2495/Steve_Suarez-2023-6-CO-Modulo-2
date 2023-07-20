import pygame
import random
import secrets

from game.utils.constants import ENEMY_1, ENEMY_2, SCREEN_WIDTH, SCREEN_HEIGHT, FONT
from game.components.bullets import Bullet
from pygame.sprite import Sprite

scales_enemies = [(40, 60), (50, 70)]
mov = 15

class Enemy(Sprite):
    def __init__(self, label, movement, type):
        super(Enemy, self).__init__()
        self.type = 'enemy'
        x_pos_init = [SCREEN_WIDTH - scales_enemies[type][0]-20, SCREEN_WIDTH / 1.5, SCREEN_WIDTH / 2, SCREEN_WIDTH / 3, SCREEN_WIDTH / 4, SCREEN_WIDTH / 5, SCREEN_WIDTH / 6, SCREEN_WIDTH / 7, 0]
        self.enemy = type
        self.enemies = [ENEMY_1, ENEMY_2]
        self.enemies = pygame.transform.scale(self.enemies[self.enemy], scales_enemies[self.enemy])
        self.rect_enemy = self.enemies.get_rect()
        self.rect_enemy.x, self.rect_enemy.y = (x_pos_init[random.randint(0, 8)], -scales_enemies[self.enemy][1])
        self.label = FONT.render(f'ENEMY: {label}', True, (240, 50, 50))
        self.movement = movement
        self.cont = 0
        self.movement_x = random.randint(50, 100) #select the movement
        self.rand = secrets.choice([True, False]) #flag to move at the left or right
        self.enemy_bullets = []
        self.destroy = False
        
    def movement_enemy(self):
        self.cont += 1
        if (self.cont >= self.movement_x and not self.rand) or (self.rect_enemy.x <= 0):
            self.rand = True
            
        elif (self.cont >= self.movement_x and self.rand) or (self.rect_enemy.x >= SCREEN_WIDTH - scales_enemies[self.enemy][1]):
            self.rand = False
            
        if self.cont >= self.movement_x:
            self.cont = 0
        
    def update(self, screen):
        self.rect_enemy.y += self.movement - 2
                    
        if self.rand:
            self.rect_enemy.x += self.movement 
        else:
            self.rect_enemy.x -= self.movement
        self.movement_enemy()
        
        for e in self.enemy_bullets:
            if e.rect.y < SCREEN_HEIGHT:
                e.add_bullet()
                e.draw(screen)
            else:
                self.enemy_bullets.remove(e)
                
    def update_position(self):
        self.rect_enemy.y = -scales_enemies[self.enemy][1]
            
    def shoot(self):
        if not self.enemy_bullets or self.enemy_bullets[-1].rect.y - self.rect_enemy.y > 150:
            bullet = Bullet(self.type, self.rect_enemy.x, (self.rect_enemy.y + scales_enemies[self.enemy][1]))
            self.enemy_bullets.append(bullet)

    def draw(self, screen):
        if self.rect_enemy.y <= SCREEN_HEIGHT and not self.destroy:
            rect_x = self.rect_enemy.x - (scales_enemies[self.enemy][0] / 3.8)
            rect_y = self.rect_enemy.y - (scales_enemies[self.enemy][1] // 6)
            screen.blit(self.enemies, (self.rect_enemy.x, self.rect_enemy.y))
            screen.blit(self.label, (rect_x, rect_y))
            self.shoot()
            self.update(screen)
            