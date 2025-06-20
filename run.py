import pygame
import Constants
import Map
import Player



def run():
    pygame.init()
    screen = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    dungeon = Map.DungeonMap(Constants.SCREEN_WIDTH // Constants.TILE_SIZE, Constants.SCREEN_HEIGHT // Constants.TILE_SIZE)
    #dungeon = Map.DungeonMap()
    dungeon.generate_room()




    player = Player.Player(5, 5, "Test", 10, 100, dungeon)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


            #movement
            delta_x = 0
            delta_y = 0
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_UP:
                        delta_y -= 1
                    case pygame.K_DOWN:
                        delta_y += 1
                    case pygame.K_LEFT:
                        delta_x -= 1
                    case pygame.K_RIGHT:
                        delta_x += 1
                if dungeon.tiles[player.y+delta_y][player.x+delta_x] is None:
                    player.y += delta_y
                    player.x += delta_x
                elif not dungeon.tiles[player.y+delta_y][player.x+delta_x].is_solid():
                    player.y += delta_y
                    player.x += delta_x
                player.rect.topleft = (player.x * Constants.TILE_SIZE, player.y * Constants.TILE_SIZE)

        screen.fill((0,0,0))
        dungeon.draw(screen)
        player.draw(screen)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

run()