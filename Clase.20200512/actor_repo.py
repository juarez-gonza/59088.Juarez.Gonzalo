class ActorRepo:
    def __init__(self):
        self.actores = {}

    def agregar_actor(self, key, actor):
        self.actores[key] = actor
