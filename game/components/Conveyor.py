import pygame
from game.utils.constants import CONVEYOR, SCREEN_WIDTH, SCREEN_HEIGHT, CONVEYOR_MOV, FPS
from game.components.Spaceship import Spaceship as sp
from game.components.enemies.Enemy import Enemy as en

class Conveyor:
    con_width, conv_height = 230, 266
    
    def __init__(self):
        self.assets = CONVEYOR
        self.assets.set_clip(pygame.Rect(652, 11, self.con_width, self.conv_height))
        self.image = self.assets.subsurface(self.assets.get_clip())
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = ((SCREEN_WIDTH //2) - (self.con_width //2) + 20), SCREEN_HEIGHT
        self.should_draw = True
        self.spaceship = sp("Steve")
        self.disem = False
        self.time = 0
        #self.enemies = en("EN1", 4, 0)
        self.enemies_1 = en("EN2", 4, 1)
        
    def move_conveyor(self):
        if self.rect.y >= 0 - self.conv_height:
            if not self.disem:
                self.rect.y -= CONVEYOR_MOV 
                 
            if self.rect.y == 383:
                self.time += 1
                self.disem = True
                
        else:
            self.should_draw = False
    
    def draw(self, screen, keys):
        if self.time == (FPS * 2):
            self.spaceship.draw(screen)
            self.spaceship.update(keys)
            self.disem = False
            
        if self.should_draw:
            self.move_conveyor()           
            screen.blit(self.image, (self.rect.x, self.rect.y))
            
        else:
            #self.enemies.draw(screen)
            self.enemies_1.draw(screen)
            