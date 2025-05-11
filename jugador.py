import pygame

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("imagenes/jugador.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.bottom = 580
        self.velocidad = 5

    def update(self, teclas):
        if teclas[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocidad
        if teclas[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.x += self.velocidad
