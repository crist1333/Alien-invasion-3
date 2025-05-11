
import pygame
import random

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, tipo):
        super().__init__()
        self.tipo = tipo
        self.image = pygame.image.load(f"imagenes/enemigo{tipo}.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 750)
        self.rect.y = random.randint(-150, -40)
        self.velocidad = random.randint(1, 3 + tipo)

    def update(self):
        self.rect.y += self.velocidad
        if self.rect.top > 600:
            self.rect.y = random.randint(-150, -40)
            self.rect.x = random.randint(0, 750)
