import os
import pygame
from source.entities.GenericEntity import Entity


class Player(Entity):
    PLAYER_IMG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets', 'player.png')

    def __init__(self):
        Entity.__init__(self)
        self.image = pygame.image.load(self.PLAYER_IMG_PATH)
        self.speed = 5
        self.health = 100
        self.damage = 10
        self.width = 50
        self.height = 75
        self.hit_stun = 1
        self.knockback_force = 10
        self.range = 50
        self.attack_speed = 100
        self.received_attack = None
        self.attack_delay = 1000 * self.attack_speed / 60

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

    def knockback(self, time):
        print(self.received_attack.direction, self.received_attack.force)
        if time - self.received_attack.time < self.received_attack.knockback_time:
            self.velocity = self.received_attack.direction * self.received_attack.force
        else:
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

            self.received_attack = None

    def update(self, player, time):
        if self.received_attack:
            self.knockback(time)
        self.move()
