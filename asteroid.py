import pygame
from constants import LINE_WIDTH
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__():
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.x, self.y), self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position = pygame.Vector2(self.x + self.velocity, self.y + self.velocity)
