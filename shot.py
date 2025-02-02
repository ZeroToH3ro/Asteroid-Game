import pygame.draw

from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.position, 2)


    def update(self, dt):
        self.position += self.velocity * dt