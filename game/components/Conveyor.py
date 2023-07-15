import pygame
import time
from game.utils.constants import CONVEYOR, SCREEN_WIDTH, SCREEN_HEIGHT, CONVEYOR_MOV
from game.components.Spaceship import Spaceship as sp

class Conveyor:
    con_width, conv_height = 230, 266
    
    def __init__(self):
        self.assets = CONVEYOR
        self.assets.set_clip(pygame.Rect(652, 11, self.con_width, self.conv_height))
        self.image = self.assets.subsurface(self.assets.get_clip())
        self.rect = self.image.get_rect()
        self.should_draw = True
        self.spaceship = sp()
        self.disem = True
        
    def event_run(self):
        if self.rect.bottom >= 0 - self.conv_height:
            if self.disem == True:
                self.rect.bottom -= CONVEYOR_MOV
            
        elif self.rect.top == (SCREEN_HEIGHT - 80):
            self.disem = False
            
        else:
            self.should_draw = False
            
    def update_player(self, keys):
        self.spaceship.update(keys)
    
    def draw(self, screen):
        if self.should_draw:
            self.event_run()
            screen.blit(self.image, ((SCREEN_WIDTH //2) - (self.con_width //2), SCREEN_HEIGHT))
            
        if not self.disem:
            time.sleep(3)
            self.spaceship.draw(screen)
            self.disem = True