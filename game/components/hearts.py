import pygame
from game.utils.constants import HEARTS, SCREEN_WIDTH, SCREEN_HEIGHT

heart_width, hearth_height = 30, 30

class Hearts:
    def __init__(self, hearts):
        self.hearts = HEARTS
        self.hearts_list = []
        self.hearts_counter = hearts
        self.max_hearts = 10
        
    def clip_heart(self, clip, screen):
        heart_clips = [pygame.Rect(3, 314, 261, 224), pygame.Rect(290, 320, 260, 225), pygame.Rect(578, 320, 260, 225)]
        heart = HEARTS.subsurface(heart_clips[clip])
        heart = pygame.transform.scale(heart, (heart_width, hearth_height))
        heart_rect = heart.get_rect()
        heart_rect.x, heart_rect.y = (SCREEN_WIDTH), (SCREEN_HEIGHT - hearth_height)
        screen.blit(heart, (heart_rect.x - heart_width, heart_rect.y))
        
    def update(self):
        if self.hearts_counter < self.max_hearts:
            self.hearts_counter += 2
            self.hearts_list.append(2)
        else:
            if self.hearts_counter % 2 == 1 and self.hearts_counter < self.max_hearts:
                self.hearts_counter += 1
                self.hearts_list.append(1)
            else:
                if len(self.hearts_list) < 5:
                    self.hearts_list.append(0)
    
    def draw(self, screen):
        self.update()
        if len(self.hearts_list) != 0:
            for heart in reversed(self.hearts_list):
                self.clip_heart(heart, screen)
