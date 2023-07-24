import pygame
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, HEART

class Healt_Bar:
    def __init__(self, hp):
        self.heart = HEART
        self.image = pygame.transform.scale(self.heart, (40, 40))
        self.x_pos = SCREEN_WIDTH - 150
        self.y_pos = SCREEN_HEIGHT - 40
        self.with_bar, self.height_bar = 120, 20
        self.hp,  self.max_hp = hp, 10
    
    def update(self):
        self.ratio = self.hp / self.max_hp 
    
    def draw(self, screen):
        self.update()
        pygame.draw.rect(screen, "black", (self.x_pos, self.y_pos, self.with_bar, self.height_bar))
        pygame.draw.rect(screen, "red", (self.x_pos, self.y_pos, self.with_bar * self.ratio, self.height_bar))
        screen.blit(self.image, (self.x_pos - 25, self.y_pos - 10))
        