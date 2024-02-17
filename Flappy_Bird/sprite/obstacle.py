import pygame.sprite
from random import choice, randint
from settings.settings import *


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, groups, scale_factor):
        super().__init__(groups)#type: ignore

        orientation = choice(('up', 'down'))

        x = WINDOW_WIDTH + randint(40, 100)

        if orientation == 'up':
            surf = pygame.image.load(f'./game_assets/graphics/rock/{0}.png').convert_alpha()
            self.image = pygame.transform.scale(surf, pygame.math.Vector2(surf.get_size()) * scale_factor)
            y = WINDOW_HEIGHT + randint(10, 50)
            self.rect = self.image.get_rect(midbottom=(x, y))
        else:
            surf = pygame.image.load(f'./game_assets/graphics/rock/{1}.png').convert_alpha()
            self.image = pygame.transform.scale(surf, pygame.math.Vector2(surf.get_size()) * scale_factor)
            y = randint(-50, -10)
            self.rect = self.image.get_rect(midtop=(x, y))

        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dt):
        self.pos.x -= 400 * dt
        self.rect.x = round(self.pos.x)
        if self.rect.right <= -100:
            self.kill()
