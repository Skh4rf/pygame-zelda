import pygame
import os, pathlib
from settings import *


class MenuItem:
    def __init__(self, name, options, default_index=0):
        self.name = name
        self.options = options
        self.index = default_index

    def get_current_valuename(self):
        if len(self.options) < 1:
            return ""
        return self.options[self.index][0]

    def get_current_value(self):
        if len(self.options) < 1:
            return ""
        return self.options[self.index][1]

class Quit(MenuItem):
    def __init__(self, player):
        super().__init__('Quit', {})
        self.player = player
    
    def next_option(self):
        self.index = (self.index + 1) % len(self.options)

    def prev_option(self):
        self.index = (self.index - 1) % len(self.options)

    def apply_selection(self):
        pygame.quit()

class Difficulty(MenuItem):
    def __init__(self, player, settings):
        super().__init__('Difficulty:', list([["Immortal", 0], ["Easy",0.25], ["Medium",0.5], ["Normal",1], ["Hard",1.5], ["Extreme",2]]))
        self.player = player
        self.settings = settings
        for index, option in enumerate(self.options):
            if INITIAL_DIFFICULTY in option:
                self.index = index

    def next_option(self):
        if self.index < len(self.options)-1:
            self.index = (self.index + 1)
            self.settings.game_difficulty = self.get_current_value()

    def prev_option(self):
        if self.index > 0:
            self.index = (self.index - 1)
            self.settings.game_difficulty = self.get_current_value()

    def apply_selection(self):
        print(f"Difficulty: {self.get_current_value()}")

class Volume(MenuItem):
    def __init__(self, player, settings):
        self.settings = settings
        super().__init__('Volume:', list([[0,0],[1,0.1],[2,0.2],[3,0.3],[4,0.4],[5,0.5],[6,0.6],[7,0.7],[8,0.8],[9,0.9],[10,1]]))
        self.player = player
        self.index = int(INITIAL_VOLUME * 10)

    def next_option(self):
        if self.index < len(self.options)-1:
            self.index = (self.index + 1)
            self.settings.game_volume = self.get_current_value()

    def prev_option(self):
        if self.index > 0:
            self.index = (self.index - 1)
            self.settings.game_volume = self.get_current_value()

    def apply_selection(self):
        #implement code here
        print(f"Volume: {self.get_current_value()}")

class MainMenu:
    def __init__(self, player, settings):
        self.settings = settings
        self.menu_items = [
            Volume(player, settings),
            Difficulty(player, settings),
            Quit(player)
        ]
        # General
        self.display_surface = pygame.display.get_surface()
        self.player = player
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE+10)
        self.is_toggled = False

        # Selection
        self.current_item = 0  # index of the selected entry
        self.selection_time = None
        self.can_move = True

    def handle_input(self):
        keys = pygame.key.get_pressed()

        if self.can_move:
            if keys[pygame.K_LEFT]:
                self.can_move = False
                self.menu_items[self.current_item].prev_option()
                self.selection_time = pygame.time.get_ticks()
            elif keys[pygame.K_RIGHT]:
                self.can_move = False
                self.menu_items[self.current_item].next_option()
                self.selection_time = pygame.time.get_ticks()
            elif keys[pygame.K_SPACE]:
                self.can_move = False
                self.menu_items[self.current_item].apply_selection()
                self.selection_time = pygame.time.get_ticks()
            elif keys[pygame.K_UP]:
                self.can_move = False
                self.current_item = (self.current_item - 1) % len(self.menu_items)
                self.selection_time = pygame.time.get_ticks()
            elif keys[pygame.K_DOWN]:
                self.can_move = False
                self.current_item = (self.current_item + 1) % len(self.menu_items)
                self.selection_time = pygame.time.get_ticks()

    def selection_cooldown(self):
        if not self.can_move:
            current_time = pygame.time.get_ticks()
            if current_time - self.selection_time >= 150:
                self.can_move = True

    def display(self):
        self.handle_input()
        self.selection_cooldown()

        # Darken the Background
        background_overlay = pygame.Surface((WIDTH, HEIGTH), pygame.SRCALPHA)
        background_overlay.fill((0, 0, 0, 160)) 
        self.display_surface.blit(background_overlay, (0, 0))

        titleimg = pygame.image.load(os.path.join(pathlib.Path(__file__).parent.parent.absolute(),'graphics/ui/title.png'))
        titleimg_rect = titleimg.get_rect(midtop=pygame.math.Vector2(WIDTH// 2, 20))
        self.display_surface.blit(titleimg, titleimg_rect)

        y_offset = 30 + titleimg_rect.bottom  # vertical distance from top to first entry
        for i, item in enumerate(self.menu_items):
            color = TEXT_COLOR if i == self.current_item else TEXT_COLOR_SELECTED # invert for this ui 

            # Draw Rectangular Outline
            entryimg = pygame.image.load(os.path.join(pathlib.Path(__file__).parent.parent.absolute(),'graphics/ui/entry.png'))
            entryimg_rect = entryimg.get_rect(midtop=pygame.math.Vector2(WIDTH//2, y_offset))
            self.display_surface.blit(entryimg, entryimg_rect)
            text_surf = self.font.render(f"{item.name} {item.get_current_valuename()}", False, color)
            text_rect = text_surf.get_rect(center=entryimg_rect.center)
            y_offset = 30 + entryimg_rect.bottom # distance between entries
            self.display_surface.blit(text_surf, text_rect)

        pygame.display.flip()