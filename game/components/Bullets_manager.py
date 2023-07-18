import pygame 
from game.utils.constants import SHIELD_TYPE, SPACESHIP

class BulletManager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []
        
    def update(self):          
        for bullet in self.bullets:
            bullet.update(self.bullets)
        
    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
            
        for bullet in self.bullets:
            bullet.draw(screen)
            
    def add_bullet(self, bullet):
        if bullet.owner == 'player':
            self.bullets.append(bullet)