import pygame


pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('RPyG')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PLAYER_SPEED = 10

clock = pygame.time.Clock()
player_img = pygame.image.load('assets/player.png')
dead = False


def player(x, y):
    game_display.blit(player_img, (x, y))


while not dead:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True
            
        print(event)

    game_display.fill(BLACK)
    player(0.5 * DISPLAY_WIDTH, 0.5 * DISPLAY_HEIGHT)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
