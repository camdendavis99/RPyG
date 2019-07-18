from source.entities.GenericEntity import Entity


class Enemy(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.image = None
        self.speed = None
        self.health = None
        self.damage = None
        self.width = None
        self.height = None
        self.range = None

    def change_velocity(self, player):
        buffer = 5
        vector_to_player = player.position - self.position
        if vector_to_player.magnitude() < self.range + buffer:
            self.velocity.x = 0
            self.velocity.y = 0
        else:
            self.velocity = self.speed * vector_to_player.normalize()

    def update(self, player):
        self.change_velocity(player)
        self.move()
        if self.position.distance_to(player.position) <= self.range:
            self.attack(player)
