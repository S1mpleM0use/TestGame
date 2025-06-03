import pygame
import random
import Constants


class Monster:
    def __init__(self, x, y, enemy_type, health, damage, loot):
        self.x = x
        self.y = y
        self.enemy_type = enemy_type
        self.health = health
        self.damage = damage
        self.loot = loot
        self.solid = True
        self.color = self.get_color_by_type()
        self.rect = pygame.Rect(x * Constants.TILE_SIZE, y * Constants.TILE_SIZE, Constants.TILE_SIZE, Constants.TILE_SIZE)

    def get_color_by_type(self):
        colors = {
            "zombie": (200, 20, 0),
            "skeleton": (225,225,225),
            "slime": (0, 247, 255),
            "mimic": (90, 60, 0),
            "lizard": (255, 0, 0)
        }

        return colors.get(self.enemy_type)

    def draw(self, surface):
        pass


class Zombie(Monster):
    def __init__(self, x, y, enemy_type, health, damage, loot):
        super().__init__(x,y, enemy_type, health, damage, loot)
        self.enemy_type = "zombie"
        self.health = 75
        self.damage = 10
        #self.loot = loot
        self.color = self.get_color_by_type()


    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

class Skeleton(Monster):
    def __init__(self, x, y, enemy_type, health, damage, loot):
        super().__init__(x,y, enemy_type, health, damage, loot)
        self.enemy_type = "skeleton"
        self.health = 50
        self.damage = 20
        #self.loot = loot
        self.color = self.get_color_by_type()


    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

class Slime(Monster):
    def __init__(self, x, y, enemy_type, health, damage, loot):
        super().__init__(x,y, enemy_type, health, damage, loot)
        self.enemy_type = "slime"
        self.health = 25
        self.damage = 5
        #self.loot = loot
        self.color = self.get_color_by_type()


    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

class Mimic(Monster):
    def __init__(self, x, y, enemy_type, health, damage, loot):
        super().__init__(x,y, enemy_type, health, damage, loot)
        self.enemy_type = "mimic"
        self.health = 50
        self.damage = 25
        #self.loot = loot
        self.color = self.get_color_by_type()


    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

class Lizard(Monster):
    def __init__(self, x, y, enemy_type, health, damage, loot):
        super().__init__(x,y, enemy_type, health, damage, loot)
        self.enemy_type = "lizard"
        self.health = 50
        self.damage = 10
        #self.loot = loot
        self.color = self.get_color_by_type()


    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)