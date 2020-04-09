import kivy, sys
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.switch import Switch
from kivy.uix.button import ButtonBehavior
from kivy.clock import Clock
from ast import literal_eval
from game import Game

class GUI(Screen) :
    
    def __init__(self):
        self.sm = ScreenManager()
        self.sm.add_widget(self.menu())

    def render(self):
        return self.sm

    def menu(self):
        screen = Screen(name='Home')
        menu_background=Image(source="main_background.jpg", allow_stretch=True, keep_ratio=False)
        layout = FloatLayout(size=(500, 500))
        layout.add_widget(menu_background)
        btn_play = Button(text='Play', size_hint=(.15, .08), pos_hint={'x':.025, 'y':.875}) 
        btn_play.bind(on_press=self.play)
        btn_quit = Button (text='Quit', size_hint=(.15, .08), pos_hint={'x':.825, 'y':.025})
        btn_quit.bind(on_press=self.quit)
        layout.add_widget(btn_play)
        layout.add_widget(btn_quit)
        screen.add_widget(layout)
        return screen

    def play (self, source):
        self.settingsview = self.settings()
        self.sm.add_widget(self.settingsview)
        self.sm.current = 'Settings'
        self.random_generation_setting = False
    
    def quit(self, source):
        sys.exit(0)

    def settings(self):
        screen = Screen (name='Settings')
        settings_background=Image(source='settings_background.jpg', allow_stretch=True, keep_ratio=False)
        layout = FloatLayout(size=(500, 500))
        layout.add_widget(settings_background)
        btn_singleplayer = Button(text='Single Player', size_hint=(.15, .08), pos_hint={'x':.65, 'y':.45}) 
        btn_singleplayer.bind(on_press=self.singleplayer)
        btn_multiplayer = Button (text='Multiplayer', size_hint=(.15, .08), pos_hint={'x':.825, 'y':.45})
        btn_multiplayer.bind(on_press=self.multiplayer)
        label_switch = Label(text='Random Map Generator', size_hint=(.15, .08), pos_hint={'x':.5, 'y':.1})
        switch = Switch(active=False, size_hint=(.15, .08), pos_hint={'x':.7, 'y':.1})
        switch.bind(active = self.map_setting) 
        layout.add_widget(btn_multiplayer)
        layout.add_widget(btn_singleplayer)
        layout.add_widget(label_switch)
        layout.add_widget(switch)
        screen.add_widget(layout)
        return screen

    def map_setting(self, source, isActive): 
        if isActive: 
            self.random_generation_setting = True
        else: 
            self.random_generation_setting = False
            
    def singleplayer(self, source):
        self.multiplayer_status = False
        self.widget=[]
        self.game = Game(mode=self.random_generation_setting)
        self.gridview = self.grid(name='Game')
        self.sm.add_widget(self.gridview)
        self.sm.current = 'Game'
    
    def multiplayer(self, source):
        self.multiplayer_status = True
        self.widget=[]
        self.game_1 = Game(mode=self.random_generation_setting)
        self.game_2 = Game(mode=self.random_generation_setting)
        self.gridview_1 = self.grid(name='Player_1')
        self.gridview_2 = self.grid(name='Player_2')
        self.sm.add_widget(self.gridview_1)
        self.sm.add_widget(self.gridview_2)
        self.sm.current = 'Player_1'
        self.turn = 1

    def grid(self, name):
        screen = Screen(name=name)
        main_layout = GridLayout(cols=2)
        layout = GridLayout(cols=11, rows=11, width=700, size_hint=(None, 1))
        border = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        for y in range (11):
            for x in range (11):
                if (x == 0 and y == 0):
                    layout.add_widget(Label(text=''))
                elif (y == 0 and x != 0):
                    layout.add_widget(Label(text=str(x)))
                elif (x == 0 and y != 0):
                    layout.add_widget(Label(text=border[y-1]))
                else :
                    btn = Button(id= str((x,y)))
                    btn.bind(on_press=self.game_call)
                    layout.add_widget(btn)
        main_layout.add_widget(layout)
        self.game_label = Label(text='Start playing by clicking on the grid')
        if self.multiplayer_status == True :
            self.widget.append(self.game_label)
        print(self.widget)    
        main_layout.add_widget(self.game_label)
        screen.add_widget(main_layout)
        return screen

    def current_game(self):
        if self.turn == 2 :
            game = self.game_2
        else :
            game = self.game_1
        return game

    def game_call(self, btn):
        a = literal_eval(btn.id)
        
        
        if self.multiplayer_status == True: #multiplayer
            btn.background_disabled_normal = ''
            _, status,  btn.background_color, message = self.current_game().update_map(a)
            
            if status == 0 :
                self.sm.current='Home'
                self.score_popup()
                self.sm.remove_widget(self.gridview_1)
                self.sm.remove_widget(self.gridview_2)
            else :
                if self.turn == 2 :
                    self.widget[1].text=message
                    self.turn = 1
                    self.sm.transition.direction = 'right'
                else :
                    self.widget[0].text=message
                    self.turn = 2
                    self.sm.transition.direction = 'left'
                self.sm.current = 'Player_'+str(self.turn)
                self.turn_popup()

        else : #singleplayer
            btn.background_disabled_normal = ''
            _, status,  btn.background_color, self.game_label.text = self.game.update_map(a)
            if status == 0 :
                self.sm.current='Home'
                self.score_popup()
                self.sm.remove_widget(self.gridview)
        btn.disabled = True
    
    def score_popup(self):
        if self.multiplayer_status == True:
            score_label = Label(text="You scored a ratio of "+str(self.current_game().show_score())+" %")
            self.player_name_input = TextInput(text="Enter your name")
            popup_title="Player "+str(self.turn)
        else:
            score_label = Label(text="You scored a ratio of "+str(self.game.show_score())+" %")
            self.player_name_input = TextInput(text="Enter your name")
            popup_title = "Game Over"
        print("after if statement")
        score_layout = GridLayout (rows=2)
        score_layout.add_widget(score_label)
        save_layout = GridLayout (cols=2)
        save_layout.add_widget(self.player_name_input)
        save_btn = Button(text="Save")
        save_btn.bind(on_press=self.save)
        save_layout.add_widget(save_btn)
        score_layout.add_widget(save_layout)
        
        self.popup=Popup(title=popup_title, content=score_layout, size_hint=(None, None), size=(400, 400), auto_dismiss=False)
        self.popup.open()

    def save(self, src):
        if self.multiplayer_status == True:
            self.current_game().save(self.player_name_input.text)
            self.popup.dismiss()
        else:
            self.game.save(self.player_name_input.text)
            self.popup.dismiss()

    def turn_popup(self):
        popup = Popup(title='Player '+ str(self.turn)+ ' turn', 
        size_hint=(None, None), size=(120, 80), auto_dismiss=True)
        popup.open()
        Clock.schedule_once(popup.dismiss, 0.5)