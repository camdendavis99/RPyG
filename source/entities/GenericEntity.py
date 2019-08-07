import os
import math
import enum
import pygame
from pygame.math import Vector2
from source.entities.Attack import Attack


class Entity:
    def __init__(self):
        self.image_dir = None
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
        self.direction = Directions.Down

    def move(self):
        self.position += self.velocity

    def draw(self, display):
        image_name = self.__class__.__name__ + '_' + self.direction.value + '.png'
        image_path = os.path.join(self.image_dir, image_name)
        image = pygame.image.load(image_path)
        display.blit(image, self.position)

    def spawn(self, x, y):
        self.position.x = x
        self.position.y = y

    def change_direction(self):
        x = self.velocity.x
        y = self.velocity.y
        if abs(y) > abs(x):
            if y < 0:
                self.direction = Directions.Up
                print(self.direction)
            else:
                self.direction = Directions.Down
                print(self.direction)
        elif abs(x) > abs(y):
            if x < 0:
                self.direction = Directions.Left
                print(self.direction)
            else:
                self.direction = Directions.Right
                print(self.direction)

    def attack(self, target: 'Entity', time: int):
        distance = self.position.distance_to(target.position)
        if distance <= self.range:
            direction = target.position - self.position
            direction = direction.normalize()
            attack_obj = Attack(damage=self.damage, force=self.knockback_force, direction=direction,
                                time=time, knockback_time=self.knockback_time)
            target.take_damage(attack_obj)
            target.received_attack = attack_obj

    def knockback(self, time):
        print(self.received_attack.direction, self.received_attack.force)
        if time - self.received_attack.time < self.received_attack.knockback_time:
            self.velocity = self.received_attack.direction * self.received_attack.force
        else:
            self.change_velocity()
            self.received_attack = None

    def take_damage(self, attack: Attack):
        self.health -= attack.damage
        if self.health <= 0:
            self.die()

    def die(self):
        del self

    def update(self, player, time):
        pass

    def change_velocity(self, player=None):
        pass


class Directions(enum.Enum):
    Up = 'Up'
    Down = 'Down'
    Left = 'Left'
    Right = 'Right'
