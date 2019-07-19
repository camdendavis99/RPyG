import pygame
from typing import List, Tuple
from pygame.math import Vector2
from source.entities.GenericEntity import Entity
from source.entities.Player import Player
from source.entities.Enemy import Enemy
from source.entities.Goblin import Goblin
import random
import time


pygame.init()

WIN_WIDTH = 800
WIN_HEIGHT = 600
game_display = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('RPyG')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARK_RED = (200, 0, 0)
DARK_GREEN = (0, 200, 0)
GRAY = (150, 150, 150)
OUT_OF_BOUNDS_MESSAGE = 'That path is too dangerous for now'

clock = pygame.time.Clock()


def get_text_objects(text: str, font_size=14, font_color=WHITE, font='freesansbold.ttf') -> Tuple:
    font_object = pygame.font.Font(font, font_size)
    text_surf = font_object.render(text, True, font_color)
    text_rect = text_surf.get_rect()
    return text_surf, text_rect


def display_message(text: str, font_size=24, location=(WIN_WIDTH/2, WIN_HEIGHT - WIN_HEIGHT/10)) -> None:
    text_surf, text_rect = get_text_objects(text, font_size=font_size)
    text_rect.center = location
    game_display.blit(text_surf, text_rect)
    pygame.display.update()
    time.sleep(2)


def exit_button_click():
    pygame.quit()
    quit()


def game_over():
    text_surf, text_rect = get_text_objects("GAME OVER", font_size=100, font_color=RED)
    text_rect.center = ((WIN_WIDTH / 2), (WIN_HEIGHT / 2))
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
        text_rect.center = ((WIN_WIDTH / 2), (WIN_HEIGHT / 2))
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


def update_entities(entity_list: List[Entity], player, cur_time):
    for entity in entity_list:
        entity.update(player, cur_time)


def draw_entities(entity_list: List[Entity]):
    for entity in entity_list:
        entity.draw(game_display)


def display_health_bar(health):
    bar_left_x = WIN_WIDTH // 6
    bar_right_x = WIN_WIDTH - bar_left_x
    bar_max_length = bar_right_x - bar_left_x
    bar_cur_length = int(health / 100 * bar_max_length)
    gray_bar = pygame.Rect(bar_left_x, 16, bar_max_length, 30)
    red_bar = pygame.Rect(bar_left_x, 16, bar_cur_length, 30)
    pygame.draw.rect(game_display, GRAY, gray_bar)
    pygame.draw.rect(game_display, RED, red_bar)


def game_loop():
    player = Player()
    entities: List[Entity] = [player]
    player.spawn(WIN_WIDTH / 2, WIN_HEIGHT / 2)
    dead = False

    while not dead:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
                goblin = Goblin()
                entities.append(goblin)
                spawn_x = random.randint(goblin.width/2, WIN_WIDTH - goblin.height/2)
                spawn_y = random.randint(goblin.height/2, WIN_HEIGHT - goblin.height/2)
                goblin.spawn(spawn_x, spawn_y)
            player.change_velocity(event)

        update_entities(entities, player, pygame.time.get_ticks())

        if player.position.x == 0 or player.health <= 0:
            dead = True

        if player.position.x > WIN_WIDTH - player.width:
            display_message(OUT_OF_BOUNDS_MESSAGE)
            player.position.x = WIN_WIDTH - player.width
        elif player.position.x < 0:
            display_message(OUT_OF_BOUNDS_MESSAGE)
            player.position.x = 0
        if player.position.y > WIN_HEIGHT - player.height:
            display_message(OUT_OF_BOUNDS_MESSAGE)
            player.position.y = WIN_HEIGHT - player.height
        elif player.position.y < 0:
            display_message(OUT_OF_BOUNDS_MESSAGE)
            player.position.y = 0

        game_display.fill(BLACK)
        draw_entities(entities)
        display_health_bar(player.health)
        pygame.display.update()
        clock.tick(60)

    game_over()


def main():
    intro()
    game_loop()


if __name__ == '__main__':
    main()
