import kivy, json, os, sys
sys.path.insert(1, '/home/shayan/Desktop/json_base_app')
#from Model import make_password_to_save, json_singin, get_user_to
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

def check_the_inputs(input_data):
	for parts in input_data:
		if input_data[parts] == '':
			return "ERROR"
		elif parts == 'timeline':
			if len(input_data[parts].split('/')) != 3:
				return "ERROR"
		elif input_data[parts] == ' ':
			return "ERROR"

class singin(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.cols = 1
		
		self.add_widget(Label(text='Name: '))
		self.name = TextInput(multiline=False)
		self.add_widget(self.name)

		self.add_widget(Label(text='Username: '))
		self.username = TextInput(multiline=False)
		self.add_widget(self.username)

		self.add_widget(Label(text='Password: '))
		self.password = TextInput(password=True, multiline=False)
		self.add_widget(self.password)

		self.add_widget(Label(text='Work: '))
		self.work = TextInput(multiline=False)
		self.add_widget(self.work)

		self.add_widget(Label(text='Timeline: '))
		self.timeline = TextInput(multiline=False)
		self.add_widget(self.timeline)

		self.add_widget(Label(text='Location: '))
		self.location = TextInput(multiline=False)
		self.add_widget(self.location)

		self.Sing_in = Button(text="singin")
		self.Sing_in.bind(on_press=self.sing_in)
		self.add_widget(Label())
		self.add_widget(self.Sing_in)

	def sing_in(self, instance):
		self.return_data={'name': self.name.text, 'username': self.username.text, 'password': make_password_to_save(self.password.text), 'work': self.work.text, 'timeline': self.timeline.text, 'location': self.location.text}
		push_data=self.return_data
		if check_the_inputs(push_data) == None:
			json_singin(push_data)
		else: print(check_the_inputs(push_data))

class login(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.cols=1
		
		self.add_widget(Label(text="username: "))
		self.username = TextInput(multiline=False)
		self.add_widget(self.username)

		self.add_widget(Label(text="password"))
		self.password = TextInput(multiline=False, password=True)
		self.add_widget(self.password)

		self.logiN = Button(text="Login")
		self.logiN.bind(on_press=self.Login)
		self.add_widget(self.logiN)

	def Login(self, instance):
		self.push_data={'username': self.username.text, 'password': self.password.text}
		if check_the_inputs(self.push_data) == None:
			self.push_data={'username': self.username.text, 'password': make_password_to_save(self.password.text)}
			print(self.push_data)
		else:
			print(check_the_inputs(self.push_data))
			Main.screen_manager.current = 'main'

class mainPage(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

class Main(App):
	def build(self):
		self.screen_manager = ScreenManager()
		self.login_page = login()
		self.singin_page = singin()
		screen = Screen(name='Login')
		screen.add_widget(self.login_page)
		self.screen_manager.add_widget(screen)

		screen = Screen(name='main')
		screen.add_widget(self.singin_page)
		self.screen_manager.add_widget(screen)
		return self.screen_manager

if __name__ == '__main__':
	Main().run()
