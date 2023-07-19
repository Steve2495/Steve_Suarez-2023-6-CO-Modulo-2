import pygame
import random
from game.utils.constants import CONVEYOR, SCREEN_WIDTH, SCREEN_HEIGHT, CONVEYOR_MOV, FPS, FONT_2, ROUND_1_PATH
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
        self.enemies = []
        self.rou = 0
        self.num_enemies = 0
        
    def move_conveyor(self):
        if self.rect.y >= 0 - self.conv_height:
            if not self.disem:
                self.rect.y -= CONVEYOR_MOV 
                 
            if self.rect.y == 383:
                self.time += 1
                self.disem = True
                
        else:
            self.should_draw = False
            
    def show_counter_round(self):
        self.round = FONT_2.render(f'ROUND: {self.rou}', False, (255, 255, 255))
        self.round_rect = self.round.get_rect()
        self.round_rect.x, self.round_rect.y = SCREEN_WIDTH - 170, 20
        
    def dispose_enemy(self):
        if len(self.spaceship.bullets) != 0:
            for b in self.spaceship.bullets:
                for e in self.enemies:
                    if b.rect.colliderect(e):
                        self.enemies.remove(e)

    def create_enemies(self):
        if self.num_enemies < 3:
            if random.randint(0, 1) == 1:
                enemy = en("EN1", 4, 0)
            else:
                enemy = en("EN1", 4, 1)
            enemy.rect_enemy.x = random.randint(20, SCREEN_HEIGHT-20)
            self.num_enemies += 1
            self.enemies.append(enemy)
            
    def manage_bullet_enemy_colision(self):
        if len(self.spaceship.bullets) != 0:
            for b in self.spaceship.bullets:
                for e in self.enemies:
                    if b.rect.colliderect(e.rect_enemy):
                        self.spaceship.buller_counter +=1
                        self.enemies.remove(e)
                        self.num_enemies -=1
                
    def update(self):
        self.manage_bullet_enemy_colision()     
        self.create_enemies()
        self.manage_borders()
        
    def manage_borders(self):
        for e in self.enemies:
            if e.rect_enemy.y > SCREEN_HEIGHT:
                self.enemies.remove(e)
                self.num_enemies -=1

    def draw(self, screen, keys):
        if self.time >= (FPS * 2):
            self.spaceship.draw(screen)
            self.spaceship.update(keys)
            self.disem = False
            
        if self.should_draw:
            self.move_conveyor()           
            screen.blit(self.image, (self.rect.x, self.rect.y))
            
        else:
            if self.time < (FPS * 5):
                self.time += 1
                if self.time == (FPS * 2.5):
                    pygame.mixer.music.load(ROUND_1_PATH)
                    pygame.mixer.music.play(1, 1.3)
            if self.time >= (FPS * 2.5):
                self.show_counter_round()
                screen.blit(self.round, (self.round_rect.x, self.round_rect.y))
                if self.time >= (FPS * 3):
                    self.rou = 1
                    self.show_counter_round()
                    if self.time >= (FPS * 5) and self.num_enemies <= 3:
                        self.update()

                        for e in self.enemies:
                            e.draw(screen)