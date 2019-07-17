from pygame.math import Vector2


class Entity:
    def __init__(self):
        self.image = None
        self.speed = None
        self.health = None
        self.damage = None
        self.width = None
        self.height = None
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
