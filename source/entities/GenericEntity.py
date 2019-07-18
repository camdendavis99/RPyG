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
        self.knockback = None
        self.hit_stun = None
        self.position = Vector2()
        self.velocity = Vector2()
        self.velocity.x = 0
        self.velocity.y = 0

    def move(self):
        self.position += self.velocity

    def draw(self, display):
        display.blit(self.image, self.position)

    def spawn(self, x, y):
        self.position.x = x
        self.position.y = y

    def attack(self, target: 'Entity'):
        distance = self.position.distance_to(target.position)
        if distance <= self.range:
            attack_obj = Attack(damage=self.damage, knockback=self.knockback, src_loc=self.position)
            target.take_damage(attack_obj)

    def take_damage(self, attack: Attack):
        self.health -= attack.damage
        if self.health <= 0:
            self.die()

    def die(self):
        del self
