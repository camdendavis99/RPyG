import os
import pygame
from source.entities.GenericEntity import Entity


class Player(Entity):
    PLAYER_IMG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets', 'player.png')

    def __init__(self):
        Entity.__init__(self)
        self.image = pygame.image.load(self.PLAYER_IMG_PATH)
        self.speed = 10
        self.health = 100
        self.damage = 10
        self.width = 50
        self.height = 75

    def change_velocity(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.velocity.x = -self.speed
            elif event.key == pygame.K_RIGHT:
                self.velocity.x = self.speed

            elif event.key == pygame.K_UP:
                self.velocity.y = -self.speed
            elif event.key == pygame.K_DOWN:
                self.velocity.y = self.speed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.velocity.x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.velocity.y = 0
