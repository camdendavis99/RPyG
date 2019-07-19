import pygame


class Attack:
    def __init__(self, damage=0, force=0, direction=None, time=None, knockback_time=250):
        self.damage = damage
        self.force = force
        self.direction = direction
        self.time = time
        self.knockback_time = knockback_time
