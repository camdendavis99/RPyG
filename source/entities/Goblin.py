from source.entities.Enemy import Enemy
import pygame
import os


class Goblin(Enemy):
    GOBLIN_IMG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets', 'goblin.png')

    def __init__(self):
        Enemy.__init__(self)
        self.image = pygame.image.load(self.GOBLIN_IMG_PATH)
        self.health = 25
        self.speed = 2
        self.damage = 8
        self.width = 40
        self.height = 60
        self.range = 60
        self.knockback = 4
        self.hit_stun = 0.25
        self.attack_speed = 30
        self.attack_delay = 1000 * self.attack_speed / 60
