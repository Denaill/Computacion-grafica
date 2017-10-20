import pygame
import random

ANCHO=420
ALTO=270
BLANCO=(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
AZUL=(0,0,255)
VERDE=(0,255,0)
GRIS=(64,64,64)
#-----------------------------------------------------------------------------------------------
class Plataform(pygame.sprite.Sprite):
	
	def __init__(self,ancho,alto):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([ancho,alto])
		self.image.fill(AZUL)
		self.rect = self.image.get_rect()
		self.rect.x = 150
		self.rect.y = 150

	def update(self):
		pass

#-----------------------------------------------------------------------------------------------
class Player(pygame.sprite.Sprite):

    def __init__(self,ancho,alto):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("mira.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.var_y = 0
        self.var_x = 0
        self.dir = 4
        self.sonido = pygame.mixer.Sound('scream.ogg')
        self.plataform_state = None
        self.plataform_colision = False

    def gravedad(self):
    	if self.var_y == 0:
    		self.var_y = 1
    	else: 
    		self.var_y += 0.35
    	if self.rect.y >= ALTO - self.rect.height:
    		self.rect.y = ALTO - self.rect.height

    def gritar(self):
    	self.sonido.play()

    def update(self):
    	#self.gravedad()
    	self.rect.x = self.rect.x + self.var_x
    	self.rect.y = self.rect.y + self.var_y
    	if self.rect.y >= ALTO - self.rect.height:
    		self.rect.y = ALTO - self.rect.height
#------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	pygame.init()
	pantalla=pygame.display.set_mode([ANCHO, ALTO])
	player_group = Player(30,30)
	plataform_group = Plataform(150,10) 
	plataformm = pygame.sprite.Group()
	general = pygame.sprite.Group()
	general.add(player_group)
	general.add(plataform_group)
	plataformm.add(plataform_group)
	player_group.plataform_state = plataformm
	clock = pygame.time.Clock()
	variacion_x = 0
	fondo = pygame.mixer.Sound('domenico.ogg')
	background = pygame.image.load('Fondos.jpg')
	background_x = 0
	fondo.play()
	end = False 
	while not end:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				end = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					player_group.var_y = -10
					player_group.gritar()

		mov_mouse = pygame.mouse.get_pos()
		player_group.rect.x = mov_mouse[0] - 50
		player_group.rect.y = mov_mouse[1] - 50
		if player_group.rect.x > 400 - player_group.rect.width:
			player_group.rect.x = 400 - player_group.rect.width
			variacion_x = -5
		elif player_group.rect.x < 20:
			player_group.rect.x = 20
			variacion_x = 5
		else:
			variacion_x = 0
		background_x = background_x + variacion_x
		player_group.update()
		pantalla.blit(background, [background_x,0])
		#pantalla.fill(NEGRO)
		general.draw(pantalla)
		clock.tick(60)
		pygame.display.flip()