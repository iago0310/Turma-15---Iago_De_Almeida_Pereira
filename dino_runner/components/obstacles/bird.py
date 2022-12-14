import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class bird(Obstacle): ##criação da classe passaros
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250 ##altura do passaro
        self.index = 0 
    
    def draw(self, screen): ##faz o passaro bater as assas
        if self.index >= 9: ##reseta a função
            self.index = 0
        screen.blit (self.image[self.index//5], self.rect) ##de 0 ate 4 uma imagem, de 5 até 9 outra imagem
        self.index += 1