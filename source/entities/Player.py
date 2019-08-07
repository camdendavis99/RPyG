import os
import pygame
from source.entities.GenericEntity import Entity


class Player(Entity):
    PLAYER_IMG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets', 'Player')

    def __init__(self):
        Entity.__init__(self)
        self.image_dir = self.PLAYER_IMG_DIR
        self.speed = 5
        self.health = 100
        self.damage = 10
        self.width = 50
        self.height = 75
        self.hit_stun = 1
        self.knockback_force = 10
        self.range = 50
        self.attack_speed = 100
        self.attack_delay = 1000 * self.attack_speed / 60

    def change_velocity(self, player=None):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.velocity.x = -self.speed
        elif keys[pygame.K_RIGHT]:
            self.velocity.x = self.speed
        else:
            self.velocity.x = 0

        if keys[pygame.K_UP]:
            self.velocity.y = -self.speed
        elif keys[pygame.K_DOWN]:
            self.velocity.y = self.speed
        else:
            self.velocity.y = 0

    def update(self, player, time):
        if self.received_attack:
            self.knockback(time)
        else:
            self.change_velocity()
            self.change_direction()
        self.move()
