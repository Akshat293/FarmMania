import pygame
from settings import *

class Overlay:
	def __init__(self,player):

		# general setup
		self.display_surface = pygame.display.get_surface()
		self.player = player

		# imports 
		overlay_path = '../graphics/overlay/'
		self.tools_surf = {tool: pygame.image.load(f'{overlay_path}{tool}.png').convert_alpha() for tool in player.tools}
		self.seeds_surf = {seed: pygame.image.load(f'{overlay_path}{seed}.png').convert_alpha() for seed in player.seeds}

	def display(self):

		# tool
		tool_surf = self.tools_surf[self.player.selected_tool]
		tool_rect = tool_surf.get_rect(midbottom = OVERLAY_POSITIONS['tool'])
		self.display_surface.blit(tool_surf,tool_rect)

		# seeds
		seed_surf = self.seeds_surf[self.player.selected_seed]
		seed_rect = seed_surf.get_rect(midbottom = OVERLAY_POSITIONS['seed'])
		self.display_surface.blit(seed_surf,seed_rect)

		# sricity
		sricity_surf = pygame.image.load('college.png').convert_alpha()
		sricity_rect = sricity_surf.get_rect(topleft = OVERLAY_POSITIONS['sricity'])
		self.display_surface.blit(sricity_surf,sricity_rect)

		#iota_logo
		iota_surf = pygame.image.load('iota_logo.png').convert_alpha()
		iota_rect = iota_surf.get_rect(topleft = OVERLAY_POSITIONS['iota'])
		self.display_surface.blit(iota_surf,iota_rect)

		#lava_logo
		lava_surf = pygame.image.load('lava.png').convert_alpha()
		lava_rect = lava_surf.get_rect(topleft = OVERLAY_POSITIONS['lava'])
		self.display_surface.blit(lava_surf,lava_rect)

		# pepsico_logo
		pepsico_surf = pygame.image.load('Pepsi.png').convert_alpha()
		pepsico_rect = pepsico_surf.get_rect(topleft = OVERLAY_POSITIONS['pepsi'])
		self.display_surface.blit(pepsico_surf,pepsico_rect)

		# tata_logo
		tata_surf = pygame.image.load('tata.png').convert_alpha()
		tata_rect = tata_surf.get_rect(topleft = OVERLAY_POSITIONS['tata'])
		self.display_surface.blit(tata_surf,tata_rect)

		# jam_logo
		jam_surf = pygame.image.load('jam.png').convert_alpha()
		jam_rect = jam_surf.get_rect(topleft = OVERLAY_POSITIONS['jam'])
		self.display_surface.blit(jam_surf,jam_rect)