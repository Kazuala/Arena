import random
from replit import db
username = 'holder'
def createAccount():
  global username
  newusername = input('What should your username be? ')
  while newusername in db.keys(): 
    print('Chosen name has already been used.')
    newusername = input('What should your username be? ')
  if newusername not in db.keys():
    newpassword = input('What will your password be? ')
    db[newusername] = newpassword
    print('Thank you for creating an account to play my game! ')
    print()
    db[newusername+'power'] = 1
    db[newusername+'winReward'] = 3
    db[newusername+'gold'] = 0
    db[newusername+'eChance'] = 50
    db[newusername+'health'] = 10
    username = newusername
    return username
def login():
  global username
  username = input('What is your username? ')
  while username not in db.keys():
    if username not in db.keys():
      print('That username does not exist, please try again. ')
    username = input('What is your username? ')
  print('Username confirmation complete, enter password. ')
  password = db[username]
  passGuess = 'N/A'
  while passGuess != password:
    passGuess = input('What is your password? ') 
    if passGuess == password:
      print('Password correct, login successful. ')
      print()
    if passGuess != password:
      print('Password incorrect, please try again. ')
  return username
CreateOrPlay = input('Do you have an account already (Yes/No)? ').lower()
if CreateOrPlay == 'no':
  createAccount()
elif CreateOrPlay == 'yes':
  login()
userpower = db[username+'power']
power2=1
userwinReward = db[username+'winReward']
oppwinReward = 3
gold1 = db[username+'gold']
gold2=0
userhealth = db[username+'health']
health2=10
skipTurn1=False
skipTurn2=False
block1=False
block2=False
eChance1=50
eChance2=50
def pvp():
  endable = False
  global userpower
  global power2
  global userwinReward
  global gold1
  global gold2
  global userhealth
  global health2
  userhealth = db[username+'health']
  health2 = 10
  global block1
  global block2
  block1 = False
  block2 = False
  global skipTurn1
  global skipTurn2
  def attack(block1,block2,power,player):
    global userhealth
    global health2
    if player == 1:
      if block2 == False:
        health2-=power
      elif block2 == True:
        health2-=power*0.5
    elif player == 2:
      if block1 == False:
        userhealth-=power
      elif block1 == True:
        userhealth-=power*0.5
  def barrel(block1,block2,power,player):
    global skipTurn1
    global skipTurn2
    global userhealth
    global health2
    if player == 1:
      if block2 == False:
        health2 -= power*1.5
        skipTurn1 = True
      elif block2 == True:
        health2 -= power*0.75
        skipTurn1 = True
    elif player == 2:
      if block1 == False:
        userhealth -= power*1.5
        skipTurn2 = True
      elif block1 == True:
        userhealth -= power*0.75
        skipTurn2 = True
  def block(player):
    global block1
    global block2
    if player == 1:
      block1 = True
    elif player == 2:
      block2 = True
  def escape(player):
    global endable
    global eChance1
    global eChance2
    end = random.randint(1,20)
    if player==1:
      if end == eChance1/5 or end<eChance1/5:
        endable = True
      else:
        print('')
        print("Failed to escape!")
        endable = False
    if player==2:
      if end == eChance2/5 or end<eChance2/5:
        endable = True
      else:
        print('')
        print("Failed to escape!")
        endable = False
    return endable
  print('Begin the fight')
  while endable == False:
    if skipTurn1==False:
      print('')
      print('Player 1 turn')
      print('')
      style = input('Which will you use: Attack, Barrel, Block, Escape? ').lower()
      if style == 'attack':
        attack(block1,block2,userpower,1)
        print('')
        print('Player 1 health: ',userhealth)
        print('Player 2 health: ',health2)
      elif style == 'barrel':
        barrel(block1,block2,userpower,1)
        print('')
        print('Player 1 health: ',userhealth)
        print('Player 2 health: ',health2)
      elif style == 'block':
        block(1)
      elif style == 'escape':
        escape(1)
    elif skipTurn1==True:
      print('')
      print('Player 1 turn skipped')
      skipTurn1=False
    if block2 == True:
      block2 = False
    if endable == True:
      break
    if health2<0.1:
      win1 = True
      break
    if skipTurn2==False:
      print('')
      print('Player 2 turn')
      print('')
      style = input('Which will you use: Attack, Barrel, Block, Escape? ').lower()
      if style == 'attack':
        attack(block1,block2,power2,2)
        print('')
        print('Player 1 health: ',userhealth)
        print('Player 2 health: ',health2)
      elif style == 'barrel':
        barrel(block1,block2,power2,2)
        print('')
        print('Player 1 health: ',userhealth)
        print('Player 2 health: ',health2)
      elif style == 'block':
        block(2)
      elif style == 'escape':
        escape(2)
    elif skipTurn2==True:
      print('')
      print('Player 2 turn skipped')
      skipTurn2=False
    if block1 == True:
      block1 = False
    if endable == True:
      break
    if userhealth<0.01:
      win2 = True
      break
  if endable == True:
    print('')
    print('Match ended successfully!')
    print("")
  elif win1 == True:
    print('')
    print('Congratulations player 1!')
    gold1+=userwinReward
    print("")
    print("Player 1 gold is now",gold1)
    print("Player 2 gold is now",gold2)
    print("")
  elif win2 == True:
    print('')
    print('Congratulations player 2!')
    gold2+=userwinReward
    print("")
    print("Player 1 gold is now",gold1)
    print("Player 2 gold is now",gold2)
    print("")
def shop():
  global userpower
  global power2
  global gold1
  global gold2
  global eChance1
  global eChance2
  shopUser=1
  print("Welcome to the shop, feel free to buy whatever you want")
  print("")
  print("Here are the options: Weapon Upgrade [5 Gold] , Escape Chance Up [7 Gold]")
  print("")
  if shopUser==1:
    choice=input("Which do you choose? ").lower()
    if choice=='weapon upgrade':
      gold1-=5
      if gold1>-1:
        userpower+=2
      elif gold1<0:
        gold1+=5
        print("")
        print("Insufficient funds")
      print("")
      print("Gold remaining:",gold1)
      print("")
      print("Weapon power:",userpower)
      print("")
    elif choice=='escape chance up':
      gold1-=7
      if gold1>-1:
        if eChance1==100:
          print("")
          print("Sorry, you are already at max ecu")
          gold1+=7
        elif eChance1<100:
          eChance1+=5
      elif gold1<0:
        print("Insufficient funds")
      print("")
      print("Gold remaining:",gold1)
      print("")
      print("Weapon power:",eChance1)
      print("")
def garden():
  print('something')
print('Hi and welcome to the Arena!')
print('')
print('Here you fight to the death against others to earn currency for the shop.')
print('')
print("To begin you will fight in your first battle.")
pvp()
while True:
  # currentTime=datetime.now()
  # print (datetime(lastTimeWateredPlants) != currentTime)
  modeChoice=input("What would you like to do? (Shop,Fight) ").lower()
  print("")
  if modeChoice=='fight':
    pvp()
  elif modeChoice=='shop':
    shop()
  elif modeChoice=='garden':
    garden()