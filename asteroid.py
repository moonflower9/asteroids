import pygame
import random
from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        old_radius = self.radius
        self.kill()
        if old_radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        vector_pos = self.velocity.rotate(angle)
        vector_neg = self.velocity.rotate(-angle)
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        asteroid_pos = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_neg = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_pos.velocity = vector_pos * 1.2
        asteroid_neg.velocity = vector_neg * 1.2

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
