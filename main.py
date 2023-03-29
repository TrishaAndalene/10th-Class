#------------- System resource -----------
from os import system

from kivymd.app import MDApp

from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, SwapTransition, FallOutTransition, CardTransition

from kivy.core.audio import SoundLoader
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.config import Config

from kivy.clock import Clock
from kivy.utils import get_color_from_hex
from kivy.lang import Builder

#------------- Private resource -----------
from machine.login import Status, Interface
from machine.dialog import Dialog
from machine.main_menu import MenuScreen
from machine.lobby import Lobby

LabelBase.register(name="Playfair", fn_regular='assets/font/PlayfairDisplay-Regular.ttf', fn_bold='assets/font/PlayfairDisplay-Medium.ttf')

WIDTH = 14*60
HEIGHT = 9*60

Config.set('graphics', 'width', f'{WIDTH}')
Config.set('graphics', 'height', f'{HEIGHT}')
Config.write()

Window.clearcolor = get_color_from_hex('#101216')

class MyApp(MDApp):

	def __init__(self):
		super().__init__()
		self.title = "Celestral Ground: Zero I"
		self.data = Status(self)
		self.lobby = Lobby(self)
		self.first_teleport = False
		self.enter_floor = True
		self.awal_data = []

		#---------------- Counter ------------------
		self.number = 0
		self.dialog_next = 0
		self.num = 0
		self.code = 1
		self.login_stats = 1
		self.current_floor = 0
		self.stats_city = -1
		self.transition = FadeTransition()

		self.screen_manager = ScreenManager(transition= self.transition)
		self.screen_manager.add_widget(Builder.load_file("pages/splash.kv")) #0
		self.screen_manager.add_widget(Builder.load_file("pages/login.kv")) #1
		self.screen_manager.add_widget(Builder.load_file("pages/register.kv")) #2
		self.screen_manager.add_widget(Builder.load_file("pages/dashboard.kv")) #3
		self.screen_manager.add_widget(Builder.load_file("pages/guildcard.kv")) #4
		self.screen_manager.add_widget(Builder.load_file("pages/menu.kv")) #5
		self.screen_manager.add_widget(Builder.load_file("pages/black.kv")) #6
		self.screen_manager.add_widget(Builder.load_file("pages/splash_2.kv")) #7
		self.screen_manager.add_widget(Builder.load_file("pages/lobby.kv")) #8
		self.screen_manager.add_widget(Builder.load_file("pages/warning.kv")) #9
		self.screen_manager.add_widget(Builder.load_file("pages/complete.kv")) #10
		self.screen_manager.add_widget(Builder.load_file("pages/exit_confirm.kv")) #11
		self.screen_manager.add_widget(Builder.load_file("pages/more_detail.kv")) #12

		#--------------- Import machine -----------
		self.login_machine = Interface(self)
		self.menu_machine = MenuScreen(self)
		self.dialog_box = Dialog()

	def build(self):
		self.start_music()
		self.screen_manager.current = 'black_screen'
		return self.screen_manager

	def black_screen(self, *args):
		self.screen_manager.current = 'black_screen'
		self.screen_manager.transition = FadeTransition()
		if self.number == 1:
			Clock.schedule_once(self.splash_2, 6)
		elif self.number == 2:
			Clock.schedule_once(self.warning, 4)
		elif self.number == 3:
			Clock.schedule_once(self.loading_schedule, 4)
		elif self.number == 4:
			Clock.schedule_once(self.main_menu, 4)
			self.number = 5
		elif self.number == 5:
			self.screen_manager.screens[6].ids['text'].text = "Teleporting ."
			if self.num == 1:
				self.screen_manager.screens[6].ids['text'].text = "Teleporting . ."
			elif self.num == 2:
				self.screen_manager.screens[6].ids['text'].text = "Teleporting . . ."
				Clock.schedule_once(self.change_lobby, 3)
			if self.num < 2:
				self.num += 1
				Clock.schedule_once(self.black_screen, 2)
		elif self.number == 6:
			self.title = "Tour complete :D"
			Clock.schedule_once(self.complete_introduction, 4)

		elif self.number == 7:
			Clock.schedule_once(self.main_menu, 4)

	def complete_introduction(self, *args):
		self.screen_manager.current = 'complete'
		self.data.level_up(self.login_machine.name)
		self.number = 7
		Clock.schedule_once(self.black_screen, 6)

	def warning(self, *args):
		self.number += 1
		self.screen_manager.current = 'warning'
		Clock.schedule_once(self.black_screen, 3)

	def start_music(self):
		self.music = SoundLoader.load('assets/music/Inazuma.mp3')
		self.music.loop = False
		self.music.volume = 0.85
		self.music.play()

	def on_start(self):
		self.number += 1
		Clock.schedule_once(self.black_screen, 3)

	def exit_screen(self):
		self.screen_manager.current = "exit"
		self.title = "Exit?"

	def backstory(self):
		self.screen_manager.current = "detail"
		self.title = "Backstory time"

	def exit(self):
		exit()

	def dialog(self):
		try:
			self.current_dialog = self.dialog_box.dialog_beginner
			#print(self.login_machine.level)
			if self.login_machine.level == 0:
				self.current_dialog = self.dialog_box.dialog_beginner
				if self.dialog_next < 41:
					dial_now = self.current_dialog[self.dialog_next]
					if self.first_teleport == False:
						self.screen_manager.screens[8].ids['dialog'].text = dial_now
						if self.dialog_next == 1:
							self.screen_manager.screens[8].ids['character_guide'].source = "assets/img/alisa_hi.png"
						if self.dialog_next == 2:
							self.screen_manager.screens[8].ids['character_guide'].source = "assets/img/alisa_trans.png"
						if self.dialog_next == 9 or self.dialog_next == 14 or self.dialog_next == 31:
							self.first_teleport = True
						if self.dialog_next == 18 or self.dialog_next == 22:
							self.enter_floor = False
						if self.dialog_next == 40:
							self.number = 6
							self.login_machine.level = 1
							self.black_screen()
						self.dialog_next += 1
					elif self.first_teleport == True:
						if self.dialog_next == 10:
							dial_now = self.current_dialog[41]
							self.screen_manager.screens[8].ids['dialog'].text = dial_now
						else:
							pass
					if self.enter_floor == False:
						self.first_teleport = True
			elif self.login_machine.level == 1:
				self.number = 6
				self.black_screen()

		except:
			self.title = "Login to continue"
			self.login_stats = 0
			self.to_login_page()

	def down_stairs(self):
		if self.lobby.number == 2 and self.current_floor == 0:
			self.current_floor = 1

		elif self.current_floor == 1:
			self.current_floor = 2

		print(self.current_floor)

		self.first_teleport = False
		self.enter_floor = True
		self.lobby.change_floor()
		self.into_the_dungeon()

	def up_stairs(self):
		if self.current_floor == 2:
			self.current_floor = 1

		elif self.current_floor == 1:
			self.current_floor = 0

		self.lobby.change_floor()
		self.into_the_dungeon()

	def into_the_dungeon(self):
		if self.current_floor == 1:
			self.screen_manager.screens[8].ids['town'].source = self.lobby.current_lobby
			self.screen_manager.screens[8].ids['dungeon_floor_up'].text = "Surface"
			self.screen_manager.screens[8].ids['dungeon_floor_up'].background_color = '#6666FF'
			self.screen_manager.screens[8].ids['dungeon_floor_down'].text = "2nd Floor"
			self.screen_manager.screens[8].ids['dungeon_floor_down'].background_color = '#6666FF'
			if self.dialog_next == 19:
				self.check_continue_dialog()
		elif self.current_floor == 2:
			self.screen_manager.screens[8].ids['town'].source = self.lobby.current_lobby
			self.screen_manager.screens[8].ids['dungeon_floor_up'].text = "1st Floor"
			self.screen_manager.screens[8].ids['dungeon_floor_up'].background_color = '#6666FF'
			self.screen_manager.screens[8].ids['dungeon_floor_down'].text = ""
			self.screen_manager.screens[8].ids['dungeon_floor_down'].background_color = 0,0,0,0
			if self.dialog_next == 23:
				self.check_continue_dialog()
		elif self.current_floor == 0:
			self.screen_manager.screens[8].ids['dungeon_floor_up'].text = ""
			self.screen_manager.screens[8].ids['dungeon_floor_up'].background_color = 0,0,0,0
			self.title = "Dungeon Gate"
			self.screen_manager.screens[8].ids['town_name'].text = "{ - Dungeon Gate - }"
			self.screen_manager.screens[8].ids['town'].source = self.lobby.current_lobby
			self.screen_manager.screens[8].ids['dungeon_floor_down'].text = "1st Floor"
			self.screen_manager.screens[8].ids['dungeon_floor_down'].background_color = '#6666FF'
			#self.lobby.change_lobby()

		#if self.dialog_next == 19 or self.dialog_next == 23:
		#	self.check_continue_dialog()

	def change_lobby(self, *args):
		if self.code == 0: #current di Dwarven
			self.lobby.number = 2
			self.code = 2
			self.stats_city = 2
			self.screen_manager.screens[8].ids['teleport_available_town'].text = "Elvish Wood"
			#self.screen_manager.screens[8].ids['teleport_available_town_2'].text = "Dungeon Gate"
			#self.screen_manager.screens[8].ids['teleport_available_town_3'].text = "Elvish Wood"
		elif self.code == 1: #current di Festval
			self.lobby.number = 1
			self.code = 0
			self.stats_city = 1
			self.screen_manager.screens[8].ids['teleport_available_town'].text = "Dungeon Gate"
			#self.screen_manager.screens[8].ids['teleport_available_town_2'].text = "Dungeon Gate"
			#self.screen_manager.screens[8].ids['teleport_available_town_3'].text = "Elvish Wood"
		elif self.code == 2: #current dungeon
			self.lobby.number = 3
			self.code = 3
			self.stats_city = 3
			self.screen_manager.screens[8].ids['teleport_available_town'].text = "Festval Town"
			#self.screen_manager.screens[8].ids['teleport_available_town'].text = "Festval Town"
			#self.screen_manager.screens[8].ids['teleport_available_town_3'].text = "Elvish Wood"
		elif self.code == 3: #current elvish
			self.lobby.number = 0
			self.code = 1
			self.stats_city = 0
			self.screen_manager.screens[8].ids['teleport_available_town'].text = "Dwarven Cave"
			#self.screen_manager.screens[8].ids['teleport_available_town_2'].text = "Dwarven Cave"
			#self.screen_manager.screens[8].ids['teleport_available_town_3'].text = "Dungeon Gate"

		print(self.code)
		self.stats_lobby = 0
		self.num = 0
		self.lobby.change_lobby()
		self.screen_manager.screens[8].ids['nav_drawer'].set_state('close')

		#self.black_screen()


	def loading_schedule(self, *args):
		self.number += 1
		self.screen_manager.current = 'splash'
		Clock.schedule_once(self.black_screen, 3)

	def splash_2(self, *args):
		self.number += 1
		self.screen_manager.current = 'splash_2'
		Clock.schedule_once(self.black_screen, 3)

	def main_menu(self, *args):
		self.title = "Celestral Ground"
		self.screen_manager.current = 'menu_screen'

	def backstories(self):
		self.title = "Background Stories"
		self.screen_manager.current = 'detail'

	def check_continue_dialog(self):
		if self.login_machine.level == 0:
			self.dialog()

	#def secret_item(self):
	#	if self.lobby.number == 0:
	#		self.screen_manager.screens[8].ids['secret_item'].source = "assets/secret_item/baloon_trans.png"
	#		self.screen_manager.screens[8].ids['secret_item'].pos_hint =  {"center_x" : .9, "center_y": .85}
	#	elif self.lobby.number == 1:
	#		self.screen_manager.screens[8].ids['secret_item'].source = "assets/secret_item/coal_trans.png"
	#		self.screen_manager.screens[8].ids['secret_item'].pos_hint = {"center_x":.2, "center_y":.5}

	def to_lobby(self, *args):
		if self.stats_city == self.lobby.number:
			self.first_teleport = False
			self.stats_city = -1
		self.screen_manager.transition = FadeTransition()
		#self.secret_item()
		if self.lobby.number == 0:
			self.title = "Festval Town"
			self.screen_manager.screens[8].ids['town'].source = self.lobby.current_lobby
			self.screen_manager.screens[8].ids['town_name'].text = "{ - Festval Town - }"
		elif self.lobby.number == 1:
			self.title = "Dwarven Cave"
			self.screen_manager.screens[8].ids['town_name'].text = "{ - Dwarven Cave - }"
			self.screen_manager.screens[8].ids['town'].source = self.lobby.current_lobby
		elif self.lobby.number == 2:
			self.title = "Dungeon Gate"
			self.screen_manager.screens[8].ids['town_name'].text = "{ - Dungeon Gate - }"
			self.screen_manager.screens[8].ids['town'].source = self.lobby.current_lobby
			self.screen_manager.screens[8].ids['dungeon_floor_down'].text = "1st Floor"
			self.screen_manager.screens[8].ids['dungeon_floor_down'].background_color = '#6666FF'#85/255, 0/255, 255/255, 255/255
		elif self.lobby.number == 3:
			self.title = "Elvish Wood"
			self.screen_manager.screens[8].ids['town_name'].text = "{ - Elvish Wood - }"
			self.screen_manager.screens[8].ids['town'].source = self.lobby.current_lobby
			self.screen_manager.screens[8].ids['dungeon_floor_down'].text = ""
			self.screen_manager.screens[8].ids['dungeon_floor_up'].text = ""
			self.screen_manager.screens[8].ids['dungeon_floor_up'].background_color = 0,0,0,0
			self.screen_manager.screens[8].ids['dungeon_floor_down'].background_color = 0,0,0,0
		self.screen_manager.current = 'lobby'
		if self.dialog_next == 10 or self.dialog_next == 15 or self.dialog_next == 32 or self.dialog_next == 41:
			self.check_continue_dialog()

	def checking_status(self, number, screen_number):
		self.login_machine.checking_status(number, screen_number)

	def show_status(self, *args):
		self.screen_manager.transition = CardTransition()
		self.title = "Traveler's Guildcard"
		self.screen_manager.current = "guildcard"
		self.data.read_data()
		for name, password, code, rank, status, class_, level in self.data.read_datas:
			if self.login_machine.name == name:
				self.screen_manager.screens[4].ids['name'].text = name
				self.screen_manager.screens[4].ids['code'].text = code	
				self.screen_manager.screens[4].ids['class'].text = class_
				self.screen_manager.screens[4].ids['status'].text = status
				self.screen_manager.screens[4].ids['rank'].text	= rank
				break
		else:
			self.screen_manager.screens[4].ids['name'].text = "Player 1"
			self.code = "unknown"
			self.class_ = "not chosen"
			self.status = "none"
			self.rank = "no rank"

	def save_data(self):
		print(self.screen_manager.screens[4].ids['name'].text)
		self.data.update_data(self.screen_manager.screens[3], self.screen_manager.screens[4].ids['name'].text)
		self.screen_manager.screens[4].ids['status'].text = self.screen_manager.screens[3].ids['status'].text
		self.checking_status(3, 1)

	def to_login_page(self, *args):
		self.screen_manager.transition = SwapTransition()
		if self.login_stats == 1:
			self.title = "Player sign in"
		self.screen_manager.current = "login"

	def to_dashboard(self):
		for name, password, code, rank, status, class_, level in self.data.read_datas:
			if self.login_machine.name == name:
				self.screen_manager.screens[3].ids['username'].text = name
				self.screen_manager.screens[3].ids['code'].text = code	
				self.screen_manager.screens[3].ids['class'].text = class_
				self.screen_manager.screens[3].ids['status'].text = status
				self.screen_manager.screens[3].ids['rank'].text	= rank
				break

		else:
			self.screen_manager.screens[3].ids['username'].text = "Player 1"
			self.code = "unknown"
			self.class_ = "not chosen"
			self.status = "none"
			self.rank = "no rank"
		self.screen_manager.current = "dashboard"

if __name__ == '__main__':
	app = MyApp()
	app.run()

'''
MDLabel:
			text: "-------------------------------------------------"
			color: (1, 1, 1, 1)
			size_hint: 1, .5
			font_size: "30sp"
			font_name: "Playfair"
			pos_hint: {"center_x":.56, "center_y":.85}
'''