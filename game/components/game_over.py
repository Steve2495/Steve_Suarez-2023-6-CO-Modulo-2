import pygame
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FONT_3, FONT_2, BACKGROUND

class Game_over:
    def __init__(self, nick, target_count, death_count):
        self.text = 'GAME OVER\n\nPRESS THE R KEY TO RESTART THE GAME'
        self.report = f'PLAYER:{nick}\nTARGET COUNT:{target_count}\nDEATH COUNT:{death_count}'
        self.background = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Create a gradient
        self.overlay_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.overlay_surface.set_alpha(128)
        self.overlay_surface.fill((0, 0, 0))   

    def draw(self, screen):
        screen.blit(self.background, (0, 0))

        # Draw the semi-transparent surface over the background image
        screen.blit(self.overlay_surface, (0, 0))

        # Render and draw the text "GAME OVER"
        game_over_surfaces = self.render_multiline_text(self.text, FONT_3, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
        for surface, rect in game_over_surfaces:
            screen.blit(surface, rect)

        # Render and draw the player report
        report_surfaces = self.render_multiline_text(self.report, FONT_2, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5))
        for surface, rect in report_surfaces:
            screen.blit(surface, rect)

    def render_multiline_text(self, text, font, center_pos):
        lines = text.split('\n')
        surfaces = [font.render(line, False, (255, 255, 255)) for line in lines]
        total_height = sum(surface.get_height() for surface in surfaces)
        y_offset = center_pos[1] - total_height // 2

        surfaces_with_positions = []
        for surface in surfaces:
            rect = surface.get_rect(centerx=center_pos[0], y=y_offset)
            surfaces_with_positions.append((surface, rect))
            y_offset += surface.get_height()

        return surfaces_with_positions
