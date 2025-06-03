import pygame
import Constants

class Player:
    def __init__(self, x, y, name, base_damage, health):
        self.x = x
        self.y = y
        self.name = name
        self.health = health
        self.base_damage = base_damage
        self.color = (255, 150, 150)
        self.rect = pygame.Rect(x * Constants.TILE_SIZE, y * Constants.TILE_SIZE, Constants.TILE_SIZE, Constants.TILE_SIZE)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)