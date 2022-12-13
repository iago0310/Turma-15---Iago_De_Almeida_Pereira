import pygame
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING ##importações das constantes


X_POS = 80
Y_POS = 310
JUMP_VEL = 8.5
Y_POS_DUCK = 340 ##atualização de posição quando se abaixar, alteração da hitbox abaixado

class Dinosaur:
    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.jump_vel = JUMP_VEL
        self.dino_duck = False

    def update(self, user_input):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()      
        elif self.dino_duck: ##função ducking para abaixar
            self.duck()

        if self.step_index >= 10:
            self.step_index = 0

        if user_input[pygame.K_UP] and not self.dino_jump: ##presionando botão seta pra cima, pula
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
        elif user_input[pygame.K_DOWN] and not self.dino_jump: ##presionando botão seta pra baixo, abaixa
            self.dino_jump = False
            self.dino_run = False
            self.dino_duck = True   
        elif not (self.dino_jump or user_input[pygame.K_DOWN]): ##quando não acontece nada, corre
            self.dino_jump = False
            self.dino_run = True
            self.dino_duck = False

    def jump(self): ##função pulo
        self.image = JUMPING
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4 ##altura do pulo
            self.jump_vel -= 0.8 ##velocidade do pulo
        
        if self.jump_vel < -JUMP_VEL:
            self.dino_rect.y = Y_POS
            self.dino_jump = False
            self.jump_vel = JUMP_VEL

    def run(self): ##função correr
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1] ##troca das imagens correndo
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index += 1
    
    def duck(self): ##função abaixar
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1] ##troca das imagens abaixado
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS_DUCK
        self.step_index += 1

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))