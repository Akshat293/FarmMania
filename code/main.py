import pygame, sys
from settings import *
from level import Level

class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
		pygame.display.set_caption('FarmMania by Team DnR')
		self.clock = pygame.time.Clock()
		self.level = Level()
		self.font = pygame.font.SysFont
		font1 = self.font('Arial', 15)
		self.text = font1.render('Akshat', True, 'black')

	
		

	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
  
			dt = self.clock.tick() / 1000
			self.level.run(dt)
			self.screen.blit(self.text, (SCREEN_WIDTH/2 - 23, SCREEN_HEIGHT/2-40))
			pygame.display.update()

if __name__ == '__main__':
	game = Game()
	game.run()



