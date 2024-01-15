import pygame, sys
import os, pathlib
from settings import *
from level import Level

class Game:
	def __init__(self):

		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('Zelda')
		self.clock = pygame.time.Clock()

		self.level = Level()

		# sound 
		main_sound = pygame.mixer.Sound(os.path.join(pathlib.Path(__file__).parent.parent.absolute(),'audio/main.ogg'))
		main_sound.set_volume(0.5)
		main_sound.play(loops = -1)

	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_m & self.level.gamemenu.is_toggled==False:
						self.level.upgrade.is_toggled = not self.level.upgrade.is_toggled
						self.level.toggle_menu()
					if event.key==pygame.K_ESCAPE & self.level.upgrade.is_toggled==False:
						self.level.gamemenu.is_toggled = not self.level.gamemenu.is_toggled
						self.level.toggle_menu()
			self.screen.fill(WATER_COLOR)
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)

if __name__ == '__main__':
	game = Game()
	game.run()