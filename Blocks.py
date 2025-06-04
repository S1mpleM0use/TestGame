import pygame
import random
import Constants


class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x * Constants.TILE_SIZE, y * Constants.TILE_SIZE, Constants.TILE_SIZE, Constants.TILE_SIZE)

    def draw(self, surface):
        pass


class Floor(Block):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.color = (100, 100, 100)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

class Wall(Block):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.color = (180, 180, 180)
        self.solid = True

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

class Chest(Block):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.color = (90, 60, 0)
        self.solid = True
        self.opened = False
        #self.loot = self.generate_loot()

    def generate_loot(self):
        pass
        #loot_types = [СЮДА ИМПОРТНИ ИЗ ДРУГОГО МОДУЛЯ ВЕСЬ ЛУТ]
        #return random.choice(loot_types)

    def open(self):
        self.opened = True
        #return self.loot

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

class Door(Block):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.color = (200, 135, 0)
        self.solid = True
        self.opened = False

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def open(self):
        self.opened = True
        self.solid = False
