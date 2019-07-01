import pygame

game_display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('RPyG')
clock = pygame.time.Clock()

pygame.init()

dead = False
while not dead:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

        print(event)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
