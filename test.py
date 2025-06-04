import Enemies
import Constants
import Map

dungeon = Map.DungeonMap(Constants.SCREEN_WIDTH // Constants.TILE_SIZE, Constants.SCREEN_HEIGHT // Constants.TILE_SIZE)

lizard = Enemies.Lizard(1, 2)


print(len(dungeon.tiles))