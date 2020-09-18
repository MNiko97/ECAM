import kivy
from kivy.app import App
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
from gui import GUI

class BattleShip(App):
    
    def build (self):
        self.gui = GUI()
        return self.gui.render()

if __name__ == "__main__":
    Config.set('graphics', 'width', 1000)
    Config.set('graphics', 'height', 700)
    Config.set('graphics', 'resizable', '0')
    BattleShip().run()