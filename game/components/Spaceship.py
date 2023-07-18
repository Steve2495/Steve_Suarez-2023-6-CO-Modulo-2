import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, SPACESHIP_MOV, FONT, BULLET
from game.components.bullets import Bullet

pygame.init()
pygame.font.init()

class Spaceship(Sprite):
    scale_x, scale_y = 40, 60
    
    def __init__(self, label):
        super(Spaceship, self).__init__()
        self.type = 'player'
        self.asset = SPACESHIP #call a asset location
        self.asset = pygame.transform.scale(self.asset, (self.scale_x, self.scale_y)) #scale the asset
        self.asset_rect = self.asset.get_rect() #take the rectangle of the asset
        self.asset_rect.x, self.asset_rect.y = SCREEN_WIDTH // 2, SCREEN_HEIGHT - 80 #create a tuple so that the ship is printed in the bottom half of the screen
        self.label = FONT.render(f'PLAYER: {label}', True, (12, 159, 254))
        self.bullet = Bullet(self.type, self.asset_rect.x, self.asset_rect.y)
        
    def move_left(self):
        if self.asset_rect.left > 0: #determine the limit of the screen
            self.asset_rect.left -= SPACESHIP_MOV #subtract from the x axis
        else:
            self.asset_rect.left = (SCREEN_WIDTH - self.scale_x)
            
    def move_right(self):
        if self.asset_rect.right < SCREEN_WIDTH: #determine the limit of the screen
            self.asset_rect.left += SPACESHIP_MOV  #add from the x axis
        else:
            self.asset_rect.left = 0
            
    def move_up(self):
        if self.asset_rect.top > 0: #determine the limit of the screen
            self.asset_rect.top -= SPACESHIP_MOV #subtract from the y axis
            
    def move_down(self):
        if self.asset_rect.bottom < SCREEN_HEIGHT: #determine the limit of the screen
            self.asset_rect.bottom += SPACESHIP_MOV #add from the y axis
            
    def shoot(self):
        self.bullet.is_showable = True
        self.bullet.add_bullet()
        self.bullet.counter += 1
        #screen.blit(self.bullet, (self.bullet_rect.x, self.bullet_rect.y)) THIS
    
    def update(self, user_input): #determinate a key event, to call the respective method
        if user_input[pygame.K_LEFT]:
            self.move_left()
        if user_input[pygame.K_RIGHT]:
            self.move_right()
        if user_input[pygame.K_UP]:
            self.move_up()
        if user_input[pygame.K_DOWN]:
            self.move_down()
        if user_input[pygame.K_SPACE]:
            self.shoot()
    
    def draw(self, screen):
        screen.blit(self.label, (self.asset_rect.x - (self.scale_x //2), self.asset_rect.y - (self.scale_y //5)))
        screen.blit(self.asset, (self.asset_rect.x, self.asset_rect.y)) #draw the spaceship in the screen
        self.bullet.draw(screen)

    