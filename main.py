import pygame
import time


pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('RPyG')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARK_RED = (200, 0, 0)
DARK_GREEN = (0, 200, 0)
PLAYER_SPEED = 10
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 75
OUT_OF_BOUNDS_MESSAGE = 'That path is too dangerous for now'

clock = pygame.time.Clock()
player_img = pygame.image.load('assets/player.png')

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


def get_text_objects(text, font_size=14, font_color=WHITE, font='freesansbold.ttf'):
    font_object = pygame.font.Font(font, font_size)
    text_surf = font_object.render(text, True, font_color)
    text_rect = text_surf.get_rect()
    return text_surf, text_rect


def display_message(text):
    text_surf, text_rect = get_text_objects(text, font_size=24)
    text_rect.center = ((DISPLAY_WIDTH/2), (DISPLAY_HEIGHT - (DISPLAY_HEIGHT/10)))
    game_display.blit(text_surf, text_rect)

    pygame.display.update()
    time.sleep(2)


def exit_button_click():
    pygame.quit()
    quit()


def game_over():
    text_surf, text_rect = get_text_objects("GAME OVER", font_size=100, font_color=RED)
    text_rect.center = ((DISPLAY_WIDTH / 2), (DISPLAY_HEIGHT / 2))
    game_display.blit(text_surf, text_rect)
    pygame.display.update()
    time.sleep(3)
    main()


def intro():
    intro_screen = True

    while intro_screen:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        game_display.fill(BLACK)
        text_surf, text_rect = get_text_objects("RPyG", font_size=100)
        text_rect.center = ((DISPLAY_WIDTH / 2), (DISPLAY_HEIGHT / 2))
        game_display.blit(text_surf, text_rect)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]

        start_button = pygame.Rect(150, 450, 100, 50)
        exit_button = pygame.Rect(550, 450, 100, 50)

        # Darkens the buttons if the mouse scrolls over them
        if start_button.collidepoint(mouse_x, mouse_y):
            pygame.draw.rect(game_display, DARK_GREEN, start_button)
            if click:
                intro_screen = False
        else:
            pygame.draw.rect(game_display, GREEN, start_button)
        if exit_button.collidepoint(mouse_x, mouse_y):
            pygame.draw.rect(game_display, DARK_RED, exit_button)
            if click:
                exit_button_click()
        else:
            pygame.draw.rect(game_display, RED, exit_button)

        start_text_surf, start_text_rect = get_text_objects('START', font_size=20, font_color=BLACK)
        exit_text_surf, exit_text_rect = get_text_objects('EXIT', font_size=20, font_color=BLACK)
        start_text_rect.center = start_button.center
        exit_text_rect.center = exit_button.center
        game_display.blit(start_text_surf, start_text_rect)
        game_display.blit(exit_text_surf, exit_text_rect)

        pygame.display.update()
        clock.tick(15)


def game_loop():
    x = 0.5 * DISPLAY_WIDTH
    y = 0.5 * DISPLAY_HEIGHT
    global v_x
    global v_y
    v_x = 0
    v_y = 0
    dead = False

    while not dead:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            move_player(event)
            print(event)

        x += v_x
        y += v_y

        if x == 0:
            dead = True

        if x > DISPLAY_WIDTH - PLAYER_WIDTH:
            display_message(OUT_OF_BOUNDS_MESSAGE)
            x = DISPLAY_WIDTH - PLAYER_WIDTH
        elif x < 0:
            display_message(OUT_OF_BOUNDS_MESSAGE)
            x = 0
        if y > DISPLAY_HEIGHT - PLAYER_HEIGHT:
            display_message(OUT_OF_BOUNDS_MESSAGE)
            y = DISPLAY_HEIGHT - PLAYER_HEIGHT
        elif y < 0:
            display_message(OUT_OF_BOUNDS_MESSAGE)
            y = 0

        game_display.fill(BLACK)
        player(x, y)
        pygame.display.update()
        clock.tick(60)

    game_over()


def main():
    intro()
    game_loop()


if __name__ == '__main__':
    main()
