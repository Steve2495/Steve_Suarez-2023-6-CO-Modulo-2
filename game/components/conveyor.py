import pygame
import random
from game.utils.constants import CONVEYOR, SCREEN_WIDTH, SCREEN_HEIGHT, CONVEYOR_MOV, FPS, FONT_2, ROUND_1_PATH
from game.components.spaceship import Spaceship as sp
from game.components.enemies.enemy import Enemy as en
from game.components.game_over import Game_over as Go
from game.components.hearts import Hearts

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
        self.should_run = True
        
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

        if len(self.enemies) !=0:
            for e in self.enemies:
                if e.rect_enemy.colliderect(self.spaceship.asset_rect):
                    self.enemies.remove(e)
                    self.spaceship.buller_counter +=1
                    self.spaceship.hearts -=1
                        
        for e in self.enemies:
            if len(e.enemy_bullets) != 0:
                for b in e.enemy_bullets:
                    if b.rect.colliderect(self.spaceship.asset_rect):
                        e.enemy_bullets.remove(b)
                        self.spaceship.hearts -=1
                                  
    def update(self):
        self.hearts = Hearts(self.spaceship.hearts)
        self.manage_bullet_enemy_colision()     
        self.create_enemies()
        self.manage_borders()
        
    def manage_borders(self):
        for e in self.enemies:
            if e.rect_enemy.y > SCREEN_HEIGHT:
                self.enemies.remove(e)
                self.num_enemies -=1
                
    def update_game_over(self, screen):
        self.game_over = Go(self.spaceship.label_1, self.spaceship.buller_counter, self.spaceship.deaths)
        self.game_over.draw(screen)

    # Update and draw the spaceship
    def update_spaceship(self, screen, keys):
        self.spaceship.draw(screen)
        self.spaceship.update(keys)

    # Handle time and load round 1 music
    def handle_time(self):
        self.time += 1
        if self.time == FPS * 2.5:
            pygame.mixer.music.load(ROUND_1_PATH)
            pygame.mixer.music.play(1, 1.3)

    # Display the round counter
    def show_round_counter(self, screen):
        self.show_counter_round()
        screen.blit(self.round, (self.round_rect.x, self.round_rect.y))

    # Manage the current round and enemies
    def handle_current_round(self, screen):
        self.rou = 1
        self.show_counter_round()
        self.num_enemies = len(self.enemies)

        if self.time >= FPS * 5 and self.num_enemies <= 3:
            self.update()
            self.draw_enemies(screen)
            if self.spaceship.hearts == 0:
                self.spaceship.deaths += 1
                self.update_game_over(screen)
                self.reset_enemies_position()
                self.reset_enemy_bullets()
                self.spaceship.bullets = []

    # Draw the enemies on the screen
    def draw_enemies(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    # Reset the enemies positions after the players defeat
    def reset_enemies_position(self):
        for enemy in self.enemies:
            enemy.update_position()

    # Reset the enemy bullets after the players defeat
    def reset_enemy_bullets(self):
        for enemy in self.enemies:
            enemy.enemy_bullets = []

    # Draw and update the spaceship if it needed
    def draw(self, screen, keys):
        if self.time >= FPS * 2 and self.spaceship.hearts > 0:
            self.update_spaceship(screen, keys)
            self.disem = False

        # Draw the conveyor or the image as required
        if self.should_draw:
            self.move_conveyor()
            screen.blit(self.image, (self.rect.x, self.rect.y))
        else:
            # Manage time and rounds
            if self.time < FPS * 5:
                self.handle_time()
            if self.time >= FPS * 2.5:
                self.show_round_counter(screen)
            if self.time >= FPS * 3:
                self.handle_current_round(screen)