import random
import Blocks
import Enemies
import Constants

class DungeonMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = [[None for _ in range(width)] for _ in range(height)]
        self.entities = []

    def generate_room(self):
        for y in range(self.height):
            for x in range(self.width):
                self.tiles[y][x] = Blocks.Wall(x, y)


        room_width = random.randint(4, 16)
        room_height = random.randint(4, 16)
        room = [[Blocks.Floor for _ in range(room_width)] for _ in range(room_height)]

        for i in range(len(room)):
            print(i)
...
test_room = DungeonMap
test_room.generate_room()
