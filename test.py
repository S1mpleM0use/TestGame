import Enemies
import Constants
import Map
import Blocks
import Player


r_floor = Blocks.Floor(1, 3)
player = Player.Player(1,2,'Nick',10, 100)

print(player.get_near_blocks('top'))