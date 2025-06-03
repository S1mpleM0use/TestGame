#test = [['E' for i in range(2)] for _ in range(5)]
#print(test)
import random


class Room:
    def __init__(self):
        self.height = random.randint(4,16)
        self.width = random.randint(4,16)

    def generateRoom(self):

        room = [[0 for _ in range(self.width)] for _ in range(self.height)]

        for y in range(self.height):
            for x in range(self.width):
                if x == 0 or y == 0 or x == self.width-1 or y == self.height-1:
                    room[y][x] = 1
                else:
                    room[y][x] = 0

        return room

    def visualizeRoom(self):
        #print(f'Width = {self.width}; Height = {self.height}')
        for i in range(len(Room.generateRoom(self))):
            print(Room.generateRoom(self)[i])




# for y in range(height):
#     for x in range(width):
#         if x == 0 or y == 0 or x == width-1 or y == height-1:
#             dungeon[y][x] == 1
#         else:
#             dungeon[y][x] == 0


# for i in range(len(dungeon)):
#     print(dungeon[i])

test_room = Room()
test_room.visualizeRoom()