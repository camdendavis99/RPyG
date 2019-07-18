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

    def change_velocity(self, player_position):
        path_to_player = player_position - self.position
        self.velocity = self.speed * path_to_player.normalize()
