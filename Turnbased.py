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
            self.team = 2
            self.display = "@"

class flag:
    def __init__(self,team):
        self.team = team
        self.health = 20
        if self.team == 1:
            self.display = "F"
        else:
            self.display = "f"

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
            self.attack_range = 2
            self.cost = 35
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
            self.cost = 20
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
            self.cost = 30
            if team == 1:
                self.display = "R"
            elif team == 2:
                self.display = "r"
        self.temp_movement = self.unit_movement
        self.team = team
        self.attack = True
    def start_turn(self):
        self.temp_movement = self.unit_movement
        self.attack = True
        


def move_distance(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)
class _map:
    def __init__(self):
        self.flag = 0
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
        if isinstance(self.map_data[y1][x1],unit):
            # Test if that unit is the correct team
            if self.map_data[y1][x1].team == self.turn:
                # Test if the object is close enough
                if self.map_data[y1][x1].attack_range >= move_distance(x1,y1,x2,y2):
                    #Tests if the target is a unit
                    if isinstance(self.map_data[y2][x2], unit):
                        #Test if this unit has already been used to attack
                        if self.map_data[y1][x1].attack:
                            #Test if target unit is from opposing team
                            if self.map_data[y2][x2].team != self.turn:
                                self.map_data[y2][x2].unit_health -= self.map_data[y1][x1].unit_damage
                                self.map_data[y1][x1].attack = False
                                self.map_data[y1][x1].temp_movement = 0
                                if self.map_data[y2][x2].unit_health <= 0:
                                    print("Unit was killed!")
                                    self.map_data[y2][x2] = tile()
                                    self.add_money(25)
                                    print("You gained 25 gold")
                                else:
                                    print("You did " + str(self.map_data[y1][x1].unit_damage) + "damage! Remaining enemy unit health: " + str(self.map_data[y2][x2].unit_health))
                            else:
                                print("You can't attack your own units!")
                        else:
                            print("You already attacked with this unit!")
                    elif isinstance(self.map_data[y2][x2],flag):
                        if self.map_data[y2][x2].team != self.turn:
                            self.map_data[y2][x2].health -= self.map_data[y1][x1].unit_damage
                            if self.map_data[y2][x2].health > 0:
                                print("You did " + str(self.map_data[y1][x1].unit_damage) + "damage! Remaining flag health:" + str(self.map_data[y2][x2].health))
                            else:
                                print("You win!")
                                self.flag = "end"
                        else:
                            print("You can't attack your own flag!")
                    else:
                        print("You can't attack that!")
                else:
                    print("Attack too far.")
            else:
                print("Wrong Team.")
        else:
            print("You can't attack with that!")
    def shop(self):
        print("If you would like to exit the shop ever type 'exit' whenever you like")
        while True:
            
            if self.turn == 1:
                print("Player " + str(self.turn) + " balance: " + str(self.player1_money))
            elif self.turn == 2:
                print("Player " + str(self.turn) + " balance: " + str(self.player2_money))
            print("Tank cost: " + str(unit("t",1).cost))
            print("Land cost: " + str(unit("l",1).cost))
            print("Ranged cost: " + str(unit("r",1).cost))
            buy = input("What would you like to buy? (t, l, r): ")
            if buy == "t" or buy == "l" or buy == "r":
                if self.turn == 1:
                    if self.player1_money >= unit(buy,2).cost:
                        y = int(input("At which y cordinate would you like to place this unit at? "))
                        if isinstance(self.map_data[y][0],tile):
                            self.map_data[y][0] = unit(buy,self.turn)
                            self.player1_money -= unit(buy,1).cost
                            print("----------------")
                        elif y == "exit":
                            break
                        else:
                            print("That please choose an empty tile to place this at")
                    else:
                        ("You don't have enough money for this!")
                else:  
                    if self.player2_money >= unit(buy,2).cost:
                        y = int(input("At which y cordinate would you like to place this unit at?"))
                        if isinstance(self.map_data[y][9],tile):
                            self.map_data[y][9] = unit(buy,self.turn)
                            self.player2_money -= unit(buy,2).cost
                            print("----------------")
                        elif y == "exit":
                            break
                        else:
                            print("That please choose an empty tile to place this at")
                    else:
                        ("You don't have enough money for this!")
                            
            
            elif buy == "exit":
                break
            else:
                print("That is not a valid choice")


        
    #adds money
    def add_money(self,money):
        if self.turn == 1:
            self.player1_money += money
        else:
            self.player2_money += money
    
    #calculates amount of money made from towers in a given turn
    def tower_money(self):
        money_total = 5
        for layer in self.map_data:
            for e in layer:
                if isinstance(e,tower):
                    if e.team == self.turn:
                        money_total += e.money
        if self.turn == 1:
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
                    if isinstance(self.map_data[i+1][i2],unit):
                        if self.map_data[i+1][i2].team == 1:
                            tower_influence += 1
                        else:
                            tower_influence -= 1
                    if isinstance(self.map_data[i-1][i2],unit):
                        if self.map_data[i-1][i2].team == 1:
                            tower_influence += 1
                        else:
                            tower_influence -= 1
                    if isinstance(self.map_data[i][i2+1],unit):
                        if self.map_data[i][i2+1].team == 1:
                            tower_influence += 1
                        else:
                            tower_influence -= 1
                    if isinstance(self.map_data[i][i2-1],unit):
                        if self.map_data[i][i2-1].team == 1:
                            tower_influence += 1
                        else:
                            tower_influence -= 1
                        
                    if tower_influence == 0:
                        pass
                    elif tower_influence > 0:
                        if self.map_data[i][i2].team == 1:
                            pass
                        elif self.map_data[i][i2].team == 2:
                            self.map_data[i][i2].change_team(0)
                        else:
                            self.map_data[i][i2].change_team(1)

                    else:
                        if self.map_data[i][i2].team == 1:
                            self.map_data[i][i2].change_team(0)
                        elif self.map_data[i][i2].team == 2:
                            pass
                        else:
                            self.map_data[i][i2].change_team(2)
                        


    def change_turn(self):
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1
        

    def new_turn(self):
        self.change_turn()
        self.check_tower_influence()
        #Gives player money
        print("Player " + str(self.turn) + " turn!")
        self.tower_money()
        #Resets moves and attacks for all units
        for layer in self.map_data:
            for e in layer:
                if isinstance(e,unit):
                    e.start_turn()
        



def draw(mapi):
    print("  0  1  2  3  4  5  6  7  8  9 ")
    for layer in mapi.map_data:
        draw_layer = str(mapi.map_data.index(layer))
        for tile in layer:
            draw_layer += "[" + tile.display + "]"
        
        print(draw_layer)
    print("-------------------------------")

def command(mapi):
    command = input("Command: ")
    
    if command == "help":
        print("List of commands:")
        print("move")
        print("info")
        print("attack")
        print("end")
        
    elif command == "end":
        mapi.new_turn()

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
    elif command == "buy":
        mapi.shop()
    elif command == "info":
        x = int(input("x: "))
        y = int(input("y: "))
        if isinstance(mapi.map_data[y][x], unit):
            print("Unit health: " + str(mapi.map_data[y][x].unit_health))
            print("Unit remaining movement: " + str(mapi.map_data[y][x].temp_movement))
            print("Unit attack remaining: " + str(mapi.map_data[y][x].attack))
            print("Unit attack damage: " + str(mapi.map_data[y][x].unit_damage))
        elif isinstance(mapi.map_data[y][x], tower):
            print("Tower money per turn: " + str(mapi.map_data[y][x].money))
        elif isinstance(mapi.map_data[y][x], flag):
            print("Flag health: "+ str(mapi.map_data[y][x].health))



map1 = _map()

def fill_map_1(mapi):
    #Flags
    mapi.map_data[8][1] = flag(1)
    mapi.map_data[1][8] = flag(2)

    #Towers
    mapi.map_data[2][2] = tower()
    mapi.map_data[7][7] = tower()
    mapi.map_data[3][6] = tower()
    mapi.map_data[6][3] = tower()
    mapi.map_data[4][4] = tower()
    mapi.map_data[5][5] = tower()
    
    #Base units
    #Team 1
    mapi.map_data[7][0] = unit("t",1)
    mapi.map_data[9][2] = unit("t",1)
    mapi.map_data[8][0] = unit("l",1)
    mapi.map_data[9][1] = unit("l",1)
    mapi.map_data[9][0] = unit("r",1)
    #Team 2
    mapi.map_data[0][7] = unit("t",2)
    mapi.map_data[2][9] = unit("t",2)
    mapi.map_data[0][8] = unit("l",2)
    mapi.map_data[1][9] = unit("l",2)
    mapi.map_data[0][9] = unit("r",2)
    

fill_map_1(map1)

running = True


while running:
    draw(map1)
    command(map1)
    print(map1.turn)
    if map1.flag == "end":
        break




