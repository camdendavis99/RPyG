import pygame


pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('RPyG')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PLAYER_SPEED = 10
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 75

clock = pygame.time.Clock()
player_img = pygame.image.load('assets/player.png')
dead = False

x = 0.5 * DISPLAY_WIDTH
y = 0.5 * DISPLAY_HEIGHT
v_x = 0
v_y = 0


def player(x, y):
    game_display.blit(player_img, (x, y))


def move_player(event):
    global v_x
    global v_y

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

    return v_x, v_y


while not dead:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True
        move_player(event)
        print(event)

    x += v_x
    y += v_y

    if x > DISPLAY_WIDTH - PLAYER_WIDTH:
        x = DISPLAY_WIDTH - PLAYER_WIDTH
    elif x < 0:
        x = 0
    if y > DISPLAY_HEIGHT - PLAYER_HEIGHT:
        y = DISPLAY_HEIGHT - PLAYER_HEIGHT
    elif y < 0:
        y = 0

    game_display.fill(BLACK)
    player(x, y)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
