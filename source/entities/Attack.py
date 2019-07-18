import pygame


class Attack:
    def __init__(self, damage=0, knockback=0, src_loc=(0, 0)):
        self.damage = damage
        self.knockback = knockback
        self.src_loc = src_loc
