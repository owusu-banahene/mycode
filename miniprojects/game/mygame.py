#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')


def printDirections():
    #get current north, south, east and west item
     if 'north' in rooms[currentRoom]:
         print(f"You have {rooms[currentRoom]['north']} to the north")
     if 'east' in rooms[currentRoom]:
         print(f"You have {rooms[currentRoom]['east']} to the east")
     if 'south' in rooms[currentRoom]:
         print(f"You have {rooms[currentRoom]['south']} to the south")
     if 'west' in rooms[currentRoom]:
         print(f"You have {rooms[currentRoom]['west']} to the west")


def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #get directions
  printDirections()
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if 'item' in rooms[currentRoom]:
      collection =''
      for items in rooms[currentRoom]['item']:
          collection +=items+','
      if len(collection.strip()) > 0:    
          print('You see a ' + collection[:-1])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'west':'Office',
                  'north':'Garage',
                  'item'  : ['key']
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : ['monster','sink','knife','fridge','water']
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : ['potion','table','chair','sette'],
                  'north' : 'Pantry',
                  'east':'Bedroom'
               },
            'Garden' : {
                  'north' : 'Dining Room',
                  'item':['garden fork']
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : ['cookie','pasta','dried fruit','cereal','mixed nuts']
            },
            'Office':{
                'east':'Hall',
                'item':['desk','chair','bookself']
                },
            'Garage':{
                'south':'Hall',
                'item':['cars']
                },
            'Bedroom':{
                'west':'Dining Room',
                'south':'Bathroom',
                'item':['bed','gun']
                },
            'Bathroom':{
                'north':'Bedroom',
                'item':['sink','toilet','tub']
                }

         }

#list of items you cannot carry with you
unmoveableItems =['table','chair','sette','fridge','sink','desk','bookself','toilet','tube','monster','bed']
#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      #inventory += [move[1]]
      #display a helpful message
      if move[1] in unmoveableItems:
          print(f"Sorry, you cannot carry {move[1]} with you")
      else:
          #add the item to their inventory
          inventory += [move[1]]
          print(move[1] + ' got!')
          #delete the item from the room
          #items = rooms[currentRoom]['item']
          if len(rooms[currentRoom]['item']) == 1:
              del rooms[currentRoom]['item']
          else:
              rooms[currentRoom]['item'].remove(move[1])
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    #if you have a knife or gun in your inventory you will survive
    if 'knife' in inventory or 'gun' in inventory:
        rooms[currentRoom]['item'].remove('monster')
        print('The monster in the kitchen is dead!!!')
    else:
        print('A monster has got you... GAME OVER!')
        break
