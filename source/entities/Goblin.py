from source.entities.Enemy import Enemy
import pygame
import os


class Goblin(Enemy):
    GOBLIN_IMG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets', 'Goblin')

    def __init__(self):
        Enemy.__init__(self)
        self.image_dir = self.GOBLIN_IMG_DIR
        self.health = 25
        self.speed = 2
        self.damage = 1
        self.width = 40
        self.height = 60
        self.range = 60
        self.knockback_force = 4
        self.hit_stun = 0.25
        self.attack_speed = 30
        self.attack_delay = 1000 * self.attack_speed / 60
