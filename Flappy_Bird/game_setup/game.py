import sys, pygame, time
from sprite.background import *
from sprite.ground import *
from sprite.player import *
from sprite.obstacle import *


class Game:
    def __init__(self):
        #setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Flappy Plane')
        self.clock = pygame.time.Clock()

        #sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        #scale_factor
        bg_height = pygame.image.load("./game_assets/graphics/background/background.png").get_height()
        self.scale_factor = WINDOW_HEIGHT/bg_height

        #sprite setup
        Background(self.all_sprites, self.scale_factor) #type: ignore
        Ground([self.all_sprites, self.collision_sprites], self.scale_factor) #type: ignore
        self.plane = Player(self.all_sprites, self.scale_factor/1.5) #type: ignore

        #timer
        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, 1400)

    def collisions(self):
        if pygame.sprite.spritecollide(self.plane, self.collision_sprites, False, pygame.sprite.collide_mask)\
                or self.plane.rect.top <= 0:
            pygame.quit()
            sys.exit()

    def run(self):
        last_time = time.time()
        while True:

            #delta time
            dt = time.time() - last_time
            last_time = time.time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.plane.player_jump()
                if event.type == self.obstacle_timer:
                    Obstacle([self.all_sprites, self.collision_sprites], self.scale_factor)#type: ignore

            self.all_sprites.update(dt)
            self.collisions()
            self.all_sprites.draw(self.display_surface)

            pygame.display.update()
            self.clock.tick(FRAMERATE)
