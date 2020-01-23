class tile:
    def __init__(self):
        self.display = " "

class tower:
    #Tower Displays
    # Neutral = White
    # Symbol is $

    def __init__(self):
        self.team = 0
        self.display = "$"
        self.money = 10
    def change_team(self,new_team):
        if new_team == 0:
            self.team = 0
            self.display = "$"
        elif new_team == 1:
            self.team = 1
            self.display = "#"
        elif new_team == 2:
            self.team = 1
            self.display = "@"

class flag:
    def __init(self,team):
        self.team = team
        self.health = 20

class unit:
    # Types of units
    # Tank  | T | t
    # Land  | L | l
    # Range | R | r

    def __init__(self,unit_type,team):
        #Tank
        if unit_type == "t":
            self.unit_health = 12
            self.unit_damage = 6
            self.unit_movement = 1
            self.attack_range = 1
            if team == 1:
                self.display = "T"
            elif team == 2:
                self.display = "t"
        #land
        elif unit_type == "l":
            self.unit_health = 10
            self.unit_damage = 3
            self.unit_movement = 2
            self.attack_range = 1
            if team == 1:
                self.display = "L"
            elif team == 2:
                self.display = "l"
        #range
        elif unit_type == "r":
            self.unit_health = 6
            self.unit_damage = 4
            self.unit_movement = 3
            self.attack_range = 3
            if team == 1:
                self.display = "R"
            elif team == 2:
                self.display = "r"
        self.temp_movement = self.unit_movement
        self.team = team
        self.attack = True
    def start_turn():
        self.temp_movement = self.unit_movement
        self.attack = True
        


def move_distance(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)
class _map:
    def __init__(self):
        self.player1_money = 0
        self.player2_money = 0
        self.map_data = []
        self.turn = 1
        for i in range(10):
            self.map_data.append([])
            for i2 in range(10):
                self.map_data[i].append(tile()) 
    
    def move(self,x1,y1,x2,y2):
        if x1 < 0 or x1 > 9 or y1 < 0 or y1 > 9 or x2 < 0 or x2 > 9 or y2 < 0 or y2 > 9:
            print("Out of map! Use cordinates from 0-9")
            return
        # Creates a temporary variable to make code more clean
        test_unit = self.map_data[y1][x1]
        #Test if first cords are a unit
        if isinstance(test_unit,unit):
            # Test if that unit is the correct team
            if test_unit.team == self.turn:
                # Test if there is enough movement left
                if test_unit.temp_movement >= move_distance(x1,y1,x2,y2):
                    # Test if the tile selected to move to is a blank tile()
                    if isinstance(self.map_data[y2][x2],tile):
                        test_unit.temp_movement -= move_distance(x1,y1,x2,y2)
                        self.map_data[y2][x2] = test_unit
                        self.map_data[y1][x1] = tile()

                    else:
                        print("You can't move there!")
                else:
                    print("Not enough movement left. Remaining movement: " + str(test_unit.temp_movement))
            else:
                print("Wrong Team.")
        else:
            print("You can't move that!")
    
    def attack(self,x1,y1,x2,y2):
        if x1 < 0 or x1 > 9 or y1 < 0 or y1 > 9 or x2 < 0 or x2 > 9 or y2 < 0 or y2 > 9:
            print("Out of map! Use cordinates from 0-9")
            return
        #Test if first cords are a unit
        if isinstance(test_unit,unit):
            # Test if that unit is the correct team
            if self.map_data[y1][x1].team == self.turn:
                # Test if the object is close enough
                if self.map_data[y1][x1].attack_range >= move_distance(x1,y1,x2,y2):
                    if isinstance(self.map_data[y2][x2], unit):
                        self.map_data[y2][x2].unit_health -= self.map_data[y1][x1].unit_damage
                        self.map_data[y1][x1].attack = False
                        if self.map_data[y2][x2].unit_health <= 0:
                            print("Unit was killed!")
                            self.map_data[y2][x2] = tile()
                            self.add_money(25)
                            print("You gained 25 gold")
                        else:
                            print("You did " + str(self.map_data[y1][x1].unit_damage) "! Remaining enemy unit health: " + str(self.map_data[y2][x2].unit_health))


                    elif isinstance(self.map_data[y2][x2],flag):
                        self.map_data[y2][x2].health -= self.map_data[y1][x1].unit_damage
                        print("You did " + str(self.map_data[y1][x1].unit_damage) + "! Remaining flag health:" + str(self.map_data[y2][x2]))
                    else:
                        print("You can't attack that!")
                else:
                    print("Attack too far.")
            else:
                print("Wrong Team.")
        else:
            print("You can't attack with that!")
    
    #adds money
    def add_money(self,money):
        if self.turn == 1:
            self.player1_money += money
        else:
            self.player2_money += money
    
    #calculates amount of money made from towers in a given turn
    def tower_money(self):
        money_total = 0
        for layer in self.map_data:
            for e in layer:
                if isinstance(e,tower):
                    if e.team == self.turn:
                        money_total += e.money
        if turn == 1:
            self.player1_money += money_total
        else:
            self.player2_money += money_total
        
        print("gained " + str(money_total) + "!")
    def check_tower_influence(self):
        for i in range(len(self.map_data)):
            for i2 in range(len(self.map_data)):
                if isinstance(self.map_data[i][i2],tower):
                    tower_influence = 0
                    tower_influence_1 = 0
                    tower_influence_2 = 0
                    #WORK ON THIS NEXT

    def change_turn(self):
        if self.turn == 1:
            self.turn = 2:
        else:
            self.turn = 1

    def new_turn(self):
        #Gives player money
        self.tower_money()
        self.check_tower_influence()
        #Resets moves and attacks for all units
        for layer in self.map_data:
            for e in layer:
                if isinstance(e,unit):
                    e.start_turn()
        #
    

    def end_turn(self):
        self.change_turn()


def draw(mapi):
    for layer in mapi.map_data:
        draw_layer = "|"
        for tile in layer:
            draw_layer += "[" + tile.display + "]"
        draw_layer += "|"
        print(draw_layer)
    print("-------------------------------")

def command(mapi):
    command = input("Command: ")
    
    if command == "help":
        print("List of commands:")
        print("move")
        print("info")
        print("attack")
    
    elif command == "move":
        x1 = int(input("x1: "))
        y1 = int(input("y1: "))
        x2 = int(input("x2: "))
        y2 = int(input("y2: "))
        mapi.move(x1,y1,x2,y2)
    
    elif command == "attack":
        x1 = int(input("x1: "))
        y1 = int(input("y1: "))
        x2 = int(input("x2: "))
        y2 = int(input("y2: "))
        mapi.attack(x1,y1,x2,y2)
    
    elif command == "info":
        x = int(input("x: "))
        y = int(input("y: "))
        if isinstance(mapi.map_data[y][x], unit):
            print("Unit health: " + str(mapi.map_data[y][x].unit_health))
            print("Unit remaining movement: " + str(mapi.map_data[y][x].temp_movement))
            print("Unit attack remaining: " + str(mapi.map_data[y][x].attack))
            print("Unit attack damage: " + str(mapi.map_data[y][x].unit_damage))
        elif isinstance(mapi.map_data[y][x], tower):
            print("Tower money per turn: " + str(mapi.map_data[y][x]))
        elif isinstance(mapi.map_data[y][x], flag):
            print("Flag health: "+ str(mapi.map_data[y][x]))



map1 = _map()
map1.map_data[0][0] = unit("r",1)
running = True


while running:
    running = False


