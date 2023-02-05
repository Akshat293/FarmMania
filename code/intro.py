import pygame
import sys
from button import Button
from main import Game
from settings import *
pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        # sricity
        sricity_surf = pygame.image.load('sricity_logo.png').convert_alpha()
        sricity_rect = sricity_surf.get_rect(
            topleft=(100,100))
        SCREEN.blit(sricity_surf, sricity_rect)


        # lava_logo
        lava_surf = pygame.image.load('lavaza.png').convert_alpha()
        lava_rect = lava_surf.get_rect(topleft=(400,150))
        SCREEN.blit(lava_surf, lava_rect)

        # pepsico_logo
        pepsico_surf = pygame.image.load('pepsico.png').convert_alpha()
        pepsico_rect = pepsico_surf.get_rect(
            topleft=(800,70))
        SCREEN.blit(pepsico_surf, pepsico_rect)

        # tata_logo
        tata_surf = pygame.image.load('tata.png').convert_alpha()
        tata_rect = tata_surf.get_rect(topleft=OVERLAY_POSITIONS['tata'])
        SCREEN.blit(tata_surf, tata_rect)

        # jam_logo
        jam_surf = pygame.image.load('jam.png').convert_alpha()
        jam_rect = jam_surf.get_rect(topleft=OVERLAY_POSITIONS['jam'])
        SCREEN.blit(jam_surf, jam_rect)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                                text_input="PARTNERS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    game = Game()
                    game.run()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
