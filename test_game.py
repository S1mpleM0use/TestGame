import pygame as p


p.init()


test_surface = p.Surface((100, 100))
test_rectangle = p.Rect(1, 1, 49, 49)
draw_test_rectangle = p.draw.rect(surface=test_surface, color=(255,255,255,128), rect=test_rectangle)


screen = p.display.set_mode((400,400))

running = True
while running:
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False

        screen.fill((0, 100, 200))
        screen.blit(test_surface, (50, 50))
        p.display.flip()


p.quit()