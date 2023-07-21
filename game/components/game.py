import pygame
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, BACKGROUND_MUSIC
from game.components.conveyor import Conveyor as cn

class Game:
    def __init__(self):
        pygame.init() 
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.conveyor = cn() #create a conveyor object
        self.background_sound = pygame.mixer.Sound(BACKGROUND_MUSIC)

    def run(self):
        self.playing = True
        while self.playing:
            self.handle_events()
            self.update()
            self.draw()
        else:
            pygame.display.quit()
            pygame.quit()

    def handle_events(self):
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.keys = pygame.key.get_pressed() #get the keys pressed
        if self.keys[pygame.K_r] and self.conveyor.spaceship.hearts == 0:
            self.conveyor.spaceship.hearts = 10
        
    def should_draw(self):
        if self.conveyor.spaceship.hearts > 0:
            self.draw_background()
            self.conveyor.draw(self.screen, self.keys) # call the draw method of the class to render the spaceship 

    def draw(self):
        self.clock.tick(FPS)
        self.background_sound.set_volume(0.1)
        self.background_sound.play()
        self.should_draw()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        """pygame.mixer.music.load(BACKGROUND_MUSIC)
        pygame.mixer.music.play()"""
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed
