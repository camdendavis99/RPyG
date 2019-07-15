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


x = 0.5 * DISPLAY_WIDTH
y = 0.5 * DISPLAY_HEIGHT
v_x = 0
v_y = 0

while not dead:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                v_x = -PLAYER_SPEED
            elif event.key == pygame.K_RIGHT:
                v_x = PLAYER_SPEED

            elif event.key == pygame.K_UP:
                v_y = -PLAYER_SPEED
            elif event.key == pygame.K_DOWN:
                v_y = PLAYER_SPEED
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                v_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                v_y = 0

        print(event)

    x += v_x
    y += v_y

    game_display.fill(BLACK)
    player(x, y)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
