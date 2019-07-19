import pygame
from pygame.math import Vector2
from source.entities.Attack import Attack


class Entity:
    def __init__(self):
        self.image = None
        self.speed = None
        self.health = None
        self.damage = None
        self.width = None
        self.height = None
        self.range = None
        self.knockback_force = None
        self.hit_stun = None
        self.attack_speed = None
        self.attack_delay = None
        self.knockback_time = 200
        self.time_pushed = 0.
        self.position = Vector2()
        self.velocity = Vector2()
        self.velocity.x = 0
        self.velocity.y = 0
        self.received_attack = None

    def move(self):
        self.position += self.velocity

    def draw(self, display):
        display.blit(self.image, self.position)

    def spawn(self, x, y):
        self.position.x = x
        self.position.y = y

    def attack(self, target: 'Entity', time: int):
        distance = self.position.distance_to(target.position)
        if distance <= self.range:
            direction = target.position - self.position
            direction = direction.normalize()
            attack_obj = Attack(damage=self.damage, force=self.knockback_force, direction=direction,
                                time=time, knockback_time=self.knockback_time)
            target.take_damage(attack_obj)
            target.received_attack = attack_obj

    def take_damage(self, attack: Attack):
        self.health -= attack.damage
        if self.health <= 0:
            self.die()

    def die(self):
        del self

    def update(self, player, time):
        pass
