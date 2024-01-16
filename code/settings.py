import pygame
import os, pathlib

class Settings:
	def __init__(self, game):
		self.game = game
		self._game_volume = INITIAL_VOLUME
		self._game_difficulty = INITIAL_DIFFICULTY

	@property
	def game_volume(self):
		return self._game_volume
	
	@game_volume.setter
	def game_volume(self, value):
		self._game_volume = value
		self.on_game_volume_change()

	def on_game_volume_change(self):
		self.game.main_sound.set_volume(self._game_volume)
		self.game.level.player.update_volume(self._game_volume)
		self.game.level.magic_player.update_volume(self.game_volume)
		for enemy in self.game.level.enemies:
			enemy.update_volume(self.game_volume)

	@property
	def game_difficulty(self):
		return self._game_difficulty
	
	@game_difficulty.setter
	def game_difficulty(self, value):
		self._game_difficulty = value
		self.on_game_difficulty_change()

	def on_game_difficulty_change(self):
		for enemy in self.game.level.enemies:
			enemy.update_difficulty(self.game_difficulty)

INITIAL_VOLUME = 0.1 # 0...1 only change in 1/10 steps
INITIAL_DIFFICULTY = 1 # ["Easy",0.25], ["Medium",0.5], ["Hard",1], ["Extreme",2]

# game setup
WIDTH    = 1280	
HEIGTH   = 720
FPS      = 60
TILESIZE = 64
HITBOX_OFFSET = {
	'player': -26,
	'object': -40,
	'grass': -10,
	'invisible': 0}

# ui 
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = os.path.join(pathlib.Path(__file__).parent.parent.absolute(),'graphics/font/joystix.ttf')
UI_FONT_SIZE = 18

# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

# menu colors
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
RECT_COLOR = '#EEEEEE'
RECT_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

# weapons 
weapon_data = {
	'sword': {'cooldown': 100, 'damage': 15,'graphic':os.path.join(pathlib.Path(__file__).parent.parent.absolute(),'graphics/weapons/sword/full.png')},
	'lance': {'cooldown': 400, 'damage': 30,'graphic':os.path.join(pathlib.Path(__file__).parent.parent.absolute(),'graphics/weapons/lance/full.png')},
	'axe': {'cooldown': 300, 'damage': 20, 'graphic':os.path.join(pathlib.Path(__file__).parent.parent.absolute(),'graphics/weapons/axe/full.png')},
	'rapier':{'cooldown': 50, 'damage': 8, 'graphic':os.path.join(pathlib.Path(__file__).parent.parent.absolute(),'graphics/weapons/rapier/full.png')},
	'sai':{'cooldown': 80, 'damage': 10, 'graphic':os.path.join(pathlib.Path(__file__).parent.parent.absolute(),'graphics/weapons/sai/full.png')}}

# magic
magic_data = {
	'flame': {'strength': 5,'cost': 20,'graphic':os.path.join(pathlib.Path(__file__).parent.parent.absolute(),'graphics/particles/flame/fire.png')},
	'heal' : {'strength': 20,'cost': 10,'graphic':os.path.join(pathlib.Path(__file__).parent.parent.absolute(),'graphics/particles/heal/heal.png')}}

# enemy
monster_data = {
	'squid': {'health': 100,'exp':100,'damage':20,'attack_type': 'slash', 'attack_sound':os.path.join(pathlib.Path(__file__).parent.parent.absolute(),'audio/attack/slash.wav'), 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
	'raccoon': {'health': 300,'exp':250,'damage':40,'attack_type': 'claw',  'attack_sound':os.path.join(pathlib.Path(__file__).parent.parent.absolute(),'audio/attack/claw.wav'),'speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
	'spirit': {'health': 100,'exp':110,'damage':8,'attack_type': 'thunder', 'attack_sound':os.path.join(pathlib.Path(__file__).parent.parent.absolute(),'audio/attack/fireball.wav'), 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
	'bamboo': {'health': 70,'exp':120,'damage':6,'attack_type': 'leaf_attack', 'attack_sound':os.path.join(pathlib.Path(__file__).parent.parent.absolute(),'audio/attack/slash.wav'), 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}}
