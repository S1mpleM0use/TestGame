import random
import Blocks
import math
import Enemies
import Constants

class DungeonMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = [[None for _ in range(width)] for _ in range(height)]
        self.entities = []

    def generate_room(self):
        room_height = int(random.randrange(5, 21, 2))
        room_width = int(random.randrange(5, 21, 2))
        start_x = random.randint(0, self.width - room_width-1)
        start_y = random.randint(0, self.height - room_height-1)
        #room = [[None for _ in range(self.width)] for _ in range(self.height)]
        for y in range(start_y, start_y + room_height):
            for x in range(start_x, start_x + room_width):
                # walls
                if x == start_x or y == start_y or y == start_y + room_height-1 or x == start_x + room_width-1:
                    #if self.tiles[y][x] is not None or Blocks.Wall or Blocks.Floor or Blocks.Door:
                    self.tiles[y][x] = Blocks.Wall(x,y)
                    #door
        #if x == math.ceil(((start_x + room_width) - start_x)/2) or y == math.ceil(((start_y + room_height) - start_y)/2):
        #    self.tiles[y][x] = Blocks.Door(x, y)
                #if y == math.ceil((start_y + room_height)/2) or x == math.ceil((start_x + room_width)/2):
                #    self.tiles[y][x] = Blocks.Door(x,y)
        for y in range(start_y+1, start_y + room_height-1):
            for x in range(start_x+1, start_x + room_width-1):
                self.tiles[y][x] = Blocks.Floor(x, y)

        y = math.floor(room_height/2 + start_y)
        x = math.floor(room_width/2 + start_x)
        self.tiles[y][x] = Blocks.Door(x, y)

        # for i in range(len(room)):
        #     print(room[i])

    def draw(self, surface):
        for y in range(self.height):
            for x in range(self.width):
                if self.tiles[y][x]:
                    self.tiles[y][x].draw(surface)


#random_room = DungeonMap()
#random_room.generate_room()
