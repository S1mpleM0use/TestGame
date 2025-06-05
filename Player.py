import pygame
import Constants
import Blocks
import Map


class Player:
    def __init__(self, x, y, name, base_damage, health, dungeon):
        self.x = x
        self.y = y
        self.name = name
        self.health = health
        self.base_damage = base_damage
        self.color = (255, 150, 150)
        self.rect = pygame.Rect(x * Constants.TILE_SIZE, y * Constants.TILE_SIZE, Constants.TILE_SIZE, Constants.TILE_SIZE)
        self.dungeon = dungeon

    def get_blocks(self):
        return [self.dungeon.tiles[self.y-1][self.x], self.dungeon.tiles[self.y+1][self.x],
                self.dungeon.tiles[self.y][self.x-1], self.dungeon.tiles[self.y][self.x+1]]

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)