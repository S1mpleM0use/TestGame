import pygame
import Constants
import Blocks


class Player:
    def __init__(self, x, y, name, base_damage, health):
        self.x = x
        self.y = y
        self.name = name
        self.health = health
        self.base_damage = base_damage
        self.color = (255, 150, 150)
        self.rect = pygame.Rect(x * Constants.TILE_SIZE, y * Constants.TILE_SIZE, Constants.TILE_SIZE, Constants.TILE_SIZE)

    def get_near_blocks(self, side):
        check_rect = self.rect.copy()
        blocks = [Blocks.Floor, Blocks.Door, Blocks.Chest, Blocks.Wall]

        match side:
            case 'north':
                check_rect.height = 1
                check_rect.y -= 1
            case 'south':
                check_rect.height = 1
                check_rect.y += self.rect.height
            case 'west':
                check_rect.width = 1
                check_rect.x -= 1
            case 'east':
                check_rect.width = 1
                check_rect.x += self.rect.width

        for obj in blocks:
            if hasattr(obj, 'rect') and check_rect.colliderect(obj.rect):
                return obj

        return None

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)