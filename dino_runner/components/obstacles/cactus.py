import random

from dino_runner.components.obstacles.obstacle import Obstacle

class small_cactus(Obstacle): ##classe cactos pequenos
    def __init__(self, image):
        self.type = random.randint(0, 2) ##randomiza as imagens
        super().__init__(image, self.type) ## sobrepoe um metodo
        self.rect.y = 325 ##tamanho menor do cacto


class large_cactus(Obstacle): ##classe cactos grandes
    def __init__(self, image):
        self.type = random.randint(0, 2) ##randomiza as imagens
        super().__init__(image, self.type) ## sobrepoe um metodo
        self.rect.y = 300 ##tamanho maior do cacto

