from map import Map
import random, json
from player import Player


class Game():

    def __init__ (self, mode):
        self.ship_remaining = 5
        if (mode):
            self.available_pos = []
            self.positions = self.random_map()
            print("random map")
        else:
            self.positions = Map().open_map()
        self.player = Player()
        print("GAME INITIALIZED")
        print(self.positions)

    def check_position(self, p):
        for i in self.positions.keys():
            if p in self.positions[i]:
                a = len(self.positions[i]) #ship health
                for j in range(a):
                    if ( p == self.positions[i][j]):
                        self.message = self.update_score(a-1, i) #i = ship ID a-1 because hp not updated yet
                        return (True,i,j)
        return(False,'/','/')

    def update_map(self, p):
        self.player.set_score(0, 1)
        self.message = " "
        a,b,c = self.check_position(p)
        if ( a == True):
            del(self.positions[b][c])
            color = (1, 0, 0, 1) #R, G, B, Intensity = color RED
            #texture = 'exploded_tile.jpg'
        else:
            color = (0, 0, 1, 1) #color blue
            #texture = 'water_missed_tile.jpg'
            self.message = "Nothing there, just the sea"
        
        return(self.positions, self.ship_remaining, color, self.message) #make sure to put back color in return !
    
    def show(self):
        print(self.positions)

    def update_score(self, hp, id):
        self.player.set_score(1, 0)
        if hp == 0 :
            self.ship_remaining -= 1
            self.message = "SHIP DOWN you sink a "+ str(id)
            if self.ship_remaining == 0 :
                self.message = "YOU WON !!!"
        else :
            self.message = "SHIP TOUCHED you hit a "+ str(id)
        return self.message

    def show_score(self):
        return str(self.player.get_score())

    def vertical_ship(self, ship_length):
        update_list = [] 
        position_list = []
        a = self.available_pos[random.randint(0, len(self.available_pos)-1)]
        status = 0
        count=0
        #print("VERTICAL TEST of : ", a)
        while (status != ship_length) :          #by convention drawing from top to bottom
            #print("this is the available position left : ", self.available_pos)
            if (a[1] + ship_length - 1) <= 10:
                for i in range (ship_length):
                    if [a[0],a[1]+i] in self.available_pos:
                        #print("TESTING n° ", i)
                        status+=1
                    else:
                        #print("TESTING HAS STOPPED")
                        status=0
                        break
                #print("Status = ", status)
                
                if status == ship_length:
                    #print("IT WORKED with : ", a)
                    break

            status = 0    
            count+=1
            if count >100:
                #print("OUT OF RANGE ERROR")
                break
            a = self.available_pos[random.randint(0, len(self.available_pos)-1)]
            #print("Failed, try again with : ", a)

        for i in range(ship_length):                    #add space around the ship in the list
            update_list.append([a[0], a[1]+i])
            position_list.append(tuple([a[0], a[1]+i]))
            if a[0]+1 <= 10 :
                update_list.append([a[0]+1,a[1]+i])    
            if a[0]-1 >= 1 :
                update_list.append([a[0]-1,a[1]+i])
            if i == 0 and a[1]-1 >= 1 :
                update_list.append([a[0], a[1]-1])
                if a[0]-1 >= 1 :
                    update_list.append([a[0]-1, a[1]-1])
                if a[0]+1 <= 10 :
                    update_list.append([a[0]+1, a[1]-1])
            if i == ship_length-1 and a[1]+ship_length <= 10 : 
                update_list.append([a[0], a[1]+ship_length])
                if a[0]-1 >= 1 :
                    update_list.append([a[0]-1, a[1]+ship_length])
                if a[0]+1 <= 10 :
                    update_list.append([a[0]+1, a[1]+ship_length])
        #print("Final VERTICAL position is : ", position_list)
        return update_list, position_list

    def horizontal_ship(self, ship_length):
        update_list = [] 
        position_list = []
        a = self.available_pos[random.randint(0, len(self.available_pos)-1)]
        status = 0
        count=0
        #print("HORIZONTAL TEST of : ", a)
        while (status != ship_length):          #by convention drawing left to right
            #print("this is the available position left : ", self.available_pos)
            if (a[0] + ship_length - 1) <= 10:
                for i in range (ship_length):
                    if [a[0]+i,a[1]] in self.available_pos:
                        #print("TESTING n° ", i)
                        status+=1
                    else:
                        #print("TESTING HAS STOPPED")
                        status=0
                        break
                #print("Status = ", status)
                
                if status == ship_length:
                    #print("IT WORKED with : ", a)
                    break

            status = 0    
            count+=1
            if count > 100:
                #print("OUT OF RANGE ERROR")
                break
            a = self.available_pos[random.randint(0, len(self.available_pos)-1)]
            #print("Failed, try again with : ", a)
            

        for i in range(ship_length):                    #add space around the ship in the list
            update_list.append([a[0]+i, a[1]])
            position_list.append(tuple([a[0]+i, a[1]])) 
            if a[1]+1 >= 1 :
                update_list.append([a[0]+i,a[1]+1])
            if a[1]-1 <= 10 :
                update_list.append([a[0]+i,a[1]-1])
            if i == 0 and a[0]-1 >= 1 :
                update_list.append([a[0]-1, a[1]])
                if a[1]-1 >= 1 :
                    update_list.append([a[0]-1, a[1]-1])
                if a[1]+1 <= 10 :
                    update_list.append([a[0]-1, a[1]+1])
            if i == ship_length-1 and a[0]+ship_length <= 10 :
                update_list.append([a[0]+ship_length, a[1]])
                if a[1]-1 >= 1 :
                    update_list.append([a[0]+ship_length, a[1]-1])
                if a[1]+1 <= 10 :
                    update_list.append([a[0]+ship_length, a[1]+1])
        #print("Final HORIZONTAL position is : ", position_list)
        return update_list, position_list

    def add_ship(self, ship):
        orientation = random.randint(0, 1)

        if orientation == 0:
            a, ship_coordinate = self.vertical_ship (ship)
        if orientation == 1 :
            a, ship_coordinate = self.horizontal_ship(ship)

        for elem_to_remove in a : #a = list contains places to delete
            for elem_available in self.available_pos:
                if elem_to_remove == elem_available:
                    self.available_pos.remove(elem_to_remove)

        return ship_coordinate

    def random_map(self):
        dico = {}
        for i in range(1, 11):
            for j in range (1, 11):
                self.available_pos.append([i, j])
        AC = 5
        C = 4
        SM1 = 3
        SM2 = SM1
        D = 2

        dico['Aicraft Carrier'] = self.add_ship(AC)
        dico['Cruiser'] = self.add_ship(C)
        dico['Submarine n°1'] = self.add_ship(SM1)
        dico['Submarine n°2'] = self.add_ship(SM2)
        dico['Destroyer'] = self.add_ship(D)
        return dico
    
    def save (self, name) :
        path='BattleShip Project\score.json'
        with open(path) as json_data:
            data_dict = json.load(json_data)
            print(data_dict)
        data_dict[name] = self.player.get_score()
        print(data_dict)
        with open(path, 'w') as outfile:
            json.dump(data_dict, outfile, indent=2)