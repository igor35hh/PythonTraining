import random
import time

nums = [x for x in range(16)]
secret_list = (
    'picture', 'box', 'cup', 'carpet', 
    'fireplace', 'flower', 'fridge', 'basket', 
    'table', 'vase', 'book', 'lamp', 
    'bed', 'shoe', 'suitcase', 'hole', 
    )
help_list = {
    
    'picture':'what leonardo da vinci liked to draw', 
    'box':'it uses for store things', 
    'cup':'it can contain inside coffee or tea or water', 
    'carpet':'what is lying on the floor', 
    
    'fireplace':'near what sherlock holmes liked to smoke pipe', 
    'flower':'it brings happy for women', 
    'fridge':'it helps to store food', 
    'basket':'think for garbage', 
    
    'table':'where people eating', 
    'vase':'where flowers are staying', 
    'book':'what people read', 
    'lamp':'what to light a room', 
    
    'bed':'where people are sleping', 
    'shoe':'what legs are wearing', 
    'suitcase':'every traveling you take it with you', 
    'hole':'where mouse is hide'
    }

class Room():
    def __init__(self, number_room, door_list, secr_list):
        self.number_room = number_room
        self.door_list = door_list
        self.secret_list = secr_list
    def checkKey(self, key):
        return secret_list[self.secret_list[0]] == key
    def checkDoor(self, door):
        pass
    def showWelcome(self):
        pass
    def showHelp(self):
        print(help_list.get(secret_list[self.secret_list[0]]))
    def showPlace(self):
        for place in self.secret_list:
            print(secret_list[place])
    def showDoor(self):
        for door in self.door_list:
            print(door) 

class Room1(Room):
    def __init__(self, number_room, door_list, secret_list):
        super().__init__(number_room, door_list, secret_list)
    def checkDoor(self, door):
        if self.door_list[0] == door:
            return 1
        else:
            return 0
    def showWelcome(self):
        print("************************************************")
        print("Welcome in the first room!")
        print("you have to find a key, key can be in or over: ")
        self.showPlace()
        print() 
            
class Room2(Room):
    def __init__(self, number_room, door_list, secret_list):
        super().__init__(number_room, door_list, secret_list)
    def checkDoor(self, door):
        if self.door_list[1] == door:
            return 2
        else:
            return 0
    def showWelcome(self):
        print("************************************************")
        print("Welcome in the second room!")
        print("you have to find a key, key can be in or over: ")
        self.showPlace()
        print() 
            
class Room3(Room):
    def __init__(self, number_room, door_list, secret_list):
        super().__init__(number_room, door_list, secret_list)
    def checkDoor(self, door):
        if self.door_list[3] == door:
            return 3
        elif self.door_list[1] == door:
            return 2
        else:
            return 0 
    def showWelcome(self):
        print("************************************************")
        print("Welcome in the third room!")
        print("you have to find a key, key can be in or over: ")
        self.showPlace()
        print()
    def showDoor(self):
        for door in self.door_list:
            print(door)
        print("The promt...")
        print("What were finding Christopher Columbus, and where it is located?")
        print("don't hurry, think diligently")   
            
class Room4(Room):
    def __init__(self, number_room, door_list, secret_list):
        super().__init__(number_room, door_list, secret_list)
    def checkDoor(self, door):
            return 3
    def showWelcome(self):
        print("************************************************")
        print("Welcome in the fourth room!")
        print("it is end of your way... ")
        self.showPlace()
        print() 

def createRooms():
    random.shuffle(nums)
    global rooms
    rooms = []
   
    room = Room1(1, ['north'], nums[0:4])
    rooms.append(room)
    
    room = Room2(2, ['north', 'east'], nums[4:8])
    rooms.append(room)
    
    room = Room3(3, ['north', 'east', 'west', 'south'], nums[8:12])
    rooms.append(room)
    
    room = Room4(4, ['no doors'], nums[12:16])
    rooms.append(room)
      
    global current_room
    current_room = rooms[0]
    current_room.showWelcome()

def checkPath(chosenPath):
    
    global current_room
    
    if chosenPath == str('exit'):
        return chosenPath
    
    if chosenPath == str('traffic light'):
        return 'exit'
    
    if current_room.checkKey(chosenPath):
        print("You are smart...")
        time.sleep(2)
        print("But let's check the door:)")
        time.sleep(1)
        current_room.showDoor()
        door = input("Which door will you choose?: ")
        if door == str('exit'):
            return door 
        answ = current_room.checkDoor(door)
        time.sleep(1)
        
        if answ == 0:
            print("You are failure!")
            time.sleep(2)
            print("Let's go to the room one...")
            time.sleep(1)
            return 'again'
        else:
            if current_room.number_room == rooms[answ].number_room:
                print("You are failure!")
                time.sleep(2)
                print("Let's go to the previous room...")
            current_room = rooms[answ]
            current_room.showWelcome()
            return ''
    
    if chosenPath == str('help'):
        print("You head down the path")
        time.sleep(1)
        print("it is going to be rainy here...")
        time.sleep(1)
        print("But your skin begins to be wet...")
        print()
        time.sleep(1)
        current_room.showHelp()
        return ''
        

createRooms()
playAgain = "yes"

while playAgain == "yes":
    
    path = ''
    while path != "exit" and path != "help" and path not in secret_list:
        path = input("Which path will you choose? (help or your choice or exit): ")
    
    path = checkPath(path)
    
    if path == "again":
        createRooms()
        
    if path == "exit":
        playAgain = input("Do you want to play again? (yes or no to continue playing): ")
        if playAgain != "no":
            createRooms()
    