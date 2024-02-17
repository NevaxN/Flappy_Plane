import pygame
from settings.settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, groups, scale_factor):
        super().__init__(groups)#type: ignore

        self.import_frames(scale_factor)
        self.frame_index = 0
        self.image = self.frames[self.frame_index]

        self.rect = self.image.get_rect(midleft=(WINDOW_WIDTH / 20, WINDOW_HEIGHT/2))
        self.pos = pygame.math.Vector2(self.rect.topleft)

        self.gravity = 600
        self.direction = 0

        self.mask = pygame.mask.from_surface(self.image)

    def import_frames(self, scale_factor):
        self.frames = []

        for i in range(1, 4):
            img = pygame.image.load(f'./game_assets/graphics/plane/planeRed{i}.png').convert_alpha()
            img = pygame.transform.scale(img, pygame.math.Vector2(img.get_size()) * scale_factor)
            self.frames.append(img)

        return self.frames

    def apply_gravity(self, dt):
        self.direction += self.gravity * dt
        self.pos.y += self.direction * dt
        self.rect.y = round(self.pos.y)

    def player_jump(self):
        self.direction = -400

    def player_animation(self, dt):
        self.frame_index += 30 * dt
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def rotate_player(self):
        rotated_plane = pygame.transform.rotozoom(self.image, -self.direction * 0.06, 1)
        self.image = rotated_plane
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dt):
        self.apply_gravity(dt)
        self.player_animation(dt)
        self.rotate_player()

