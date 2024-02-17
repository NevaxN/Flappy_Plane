import pygame
from settings.settings import *


class Background(pygame.sprite.Sprite):
    def __init__(self, groups, scale_factor):
        super().__init__(groups) #type: ignore
        bg = pygame.image.load("./game_assets/graphics/background/background.png").convert()

        full_height = bg.get_height() * scale_factor
        full_width = bg.get_width() * scale_factor
        full_sized_image = pygame.transform.scale(bg, (full_width, full_height))

        self.image = pygame.Surface((full_width * 2, full_height))
        self.image.blit(full_sized_image, (0, 0))
        self.image.blit(full_sized_image, (full_width, 0))

        self.rect = self.image.get_rect(topleft=(0, 0))
        self.pos = pygame.math.Vector2(self.rect.topleft)

    def update(self, dt):
        self.pos.x -= 300 * dt
        if self.rect.centerx <= 0:
            self.pos.x = 0
        self.rect.x = round(self.pos.x)
