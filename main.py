import pygame
import sys
from jugador import Jugador
from enemigo import Enemigo

# Inicializa PyGame
pygame.init()
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Alien Invasion")
fondo = pygame.image.load("imagenes/fondo.jpg").convert()

# Colores y fuente
BLANCO = (255, 255, 255)
fuente = pygame.font.SysFont(None, 36)

# Grupos de sprites
jugador = Jugador()
grupo_jugador = pygame.sprite.Group(jugador)

enemigos = pygame.sprite.Group()
tipos_naves = 3
for i in range(5):
    enemigo = Enemigo(tipo=(i % tipos_naves) + 1)
    enemigos.add(enemigo)

# Grupo para disparos
balas = pygame.sprite.Group()

# Variables del juego
jugando = False
puntos = 0
balas_disparadas = 0
naves_destruidas = 0

# Clase para proyectiles
class Bala(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("imagenes/bala.png").convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.y -= 7
        if self.rect.bottom < 0:
            self.kill()

# Función para dibujar puntajes y stats
def mostrar_puntaje():
    texto = fuente.render(f"Score: {puntos} | Disparos: {balas_disparadas} | Naves: {naves_destruidas}", True, BLANCO)
    pantalla.blit(texto, (10, 10))

# Función del menú de pausa
def menu_pausa():
    pantalla.fill((0, 0, 0))
    texto1 = fuente.render("PAUSA", True, BLANCO)
    texto2 = fuente.render("Presiona ESC para continuar o Q para salir", True, BLANCO)
    texto3 = fuente.render(f"Score: {puntos} | Disparos: {balas_disparadas} | Naves: {naves_destruidas}", True, BLANCO)
    pantalla.blit(texto1, (330, 200))
    pantalla.blit(texto2, (160, 250))
    pantalla.blit(texto3, (180, 300))
    pygame.display.flip()

    en_pausa = True
    while en_pausa:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    en_pausa = False
                elif evento.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

# Menú principal con instrucciones
def mostrar_menu_inicio():
    pantalla.fill((0, 0, 0))
    titulo = fuente.render("Alien Invasion", True, BLANCO)
    instrucciones1 = fuente.render("Flechas ← → para mover", True, BLANCO)
    instrucciones2 = fuente.render("ESPACIO para disparar", True, BLANCO)
    instrucciones3 = fuente.render("ESC para pausar el juego", True, BLANCO)
    iniciar = fuente.render("Presiona ESPACIO para comenzar", True, BLANCO)
    pantalla.blit(titulo, (300, 100))
    pantalla.blit(instrucciones1, (250, 200))
    pantalla.blit(instrucciones2, (250, 240))
    pantalla.blit(instrucciones3, (250, 280))
    pantalla.blit(iniciar, (220, 340))
    pygame.display.flip()

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    esperando = False

# Inicia el juego
mostrar_menu_inicio()

# Bucle principal del juego
reloj = pygame.time.Clock()
jugando = True
while jugando:
    reloj.tick(60)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                bala = Bala(jugador.rect.centerx, jugador.rect.top)
                balas.add(bala)
                balas_disparadas += 1
            elif evento.key == pygame.K_ESCAPE:
                menu_pausa()

    teclas = pygame.key.get_pressed()
    jugador.update(teclas)
    enemigos.update()
    balas.update()

    # Colisiones entre balas y enemigos
    colisiones = pygame.sprite.groupcollide(balas, enemigos, True, True)
    for colision in colisiones:
        puntos += 10
        naves_destruidas += 1
        nuevo = Enemigo(tipo=(naves_destruidas % tipos_naves) + 1)
        enemigos.add(nuevo)

    # Dibujar todo
    pantalla.blit(fondo, (0, 0))
    grupo_jugador.draw(pantalla)
    enemigos.draw(pantalla)
    balas.draw(pantalla)
    mostrar_puntaje()

    pygame.display.flip()

pygame.quit()
