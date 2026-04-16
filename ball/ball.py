import pygame

WIDTH, HEIGHT = 600, 400

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 25

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy

        if 0 + self.radius <= new_x <= WIDTH - self.radius:
            self.x = new_x
        if 0 + self.radius <= new_y <= HEIGHT - self.radius:
            self.y = new_y

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)