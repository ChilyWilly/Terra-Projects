import os
import time
import random


playerhealth = (500)
enemyhealth = (500)
playermana = (100)
manacap = (100)
healthcap = (500)
hitchance = None
randendmg = None
randplaydmg = None


playerattack = False
playerdefend = False
stagger = False


# the function to clear the terminal
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def enemy_atk():
    global playerhealth, playerdefend
    if playerhealth > healthcap:
        playerhealth = healthcap
    if not playerdefend:
        randendmg = random.randint(50, 70)
    elif playerdefend:
        randendmg = random.randint(20, 40)
        playerdefend = False
    print(f'Your opponent did {randendmg} damage!')
    playerhealth -= randendmg
    time.sleep(2)


def boss_atk():
    global playerhealth, playerdefend, randendmg
    if playerhealth > healthcap:
        playerhealth = healthcap
    if not playerdefend:
        randendmg = random.randint(50, 70)
    elif playerdefend:
        randendmg = random.randint(20, 40)
        playerdefend = False
    print(f'Your opponent did {randendmg} damage!')
    time.sleep(2)
    playerhealth -= randendmg


def item():
    global playerhealth
    clear_terminal()
    print('Items:\n[1] Health potion')
    print('[2] Atk Boost')
    print('[3] Shield Boost')
    print('[4] Back')
    itemuse = input('What item would you like to use?\n')
    if itemuse == '1':
        if playerhealth < 500:
            playerhealth += 40
            print('You healed 40 health!')
            if enemyhealth > 0:
                enemy_atk()
        else:
            print('Your health is already full!')
    elif itemuse == '2':
        global playerattack
        playerattack = True
        print('Your next attack will do 20 more damage!')
        time.sleep(2)
        if enemyhealth > 0:
            enemy_atk()
    elif itemuse == '3':
        global playerdefend
        playerdefend = True
        print('You will take 30 less damage!')
        time.sleep(2)
        if enemyhealth > 0:
            enemy_atk()
    elif itemuse == '4':
        print('')
    else:
        print('Invalid action, try again')
        time.sleep(2)


def secretspell():
    clear_terminal()
    global playermana, stagger, playerhealth
    print('Spells:\n[1] Heal: Heals 60 HP (60 mana)')
    print('[2 Stagger: Gives a higher chance to hit the enemy (40 mana)]')
    print('[3] Back')
    spell = input('What spell would you like to cast?')
    if spell == '1':
        if playermana >= 60 and playerhealth < 500:
            playerhealth += 60
            playermana -= 60
            print('You healed 60 hp!')
            time.sleep(2)
            if enemyhealth > 0:
                boss_atk()
        else:
            print('Not enough mana! You need 60 mana!')
    elif spell == '2':
        if playermana >= 60:
            stagger = True
            print('Your next attack will have a higher chance to hit!')
            time.sleep(2)
            boss_atk()
    elif spell == '3':
        None
    else:
        print('Invalid action, try again')


def spell():
    clear_terminal()
    global enemyhealth, playerhealth, playermana
    print('Spells:\n[1] Earthquake: Does damage to both fighters (40 mana)')
    print('[2] Thunder: Does 100 damage (100 mana)')
    print('[3] Heal: Heals 60 health (60 mana)')
    print('[4] Back')
    spelluse = input('What spell would you like to cast?\n')
    if spelluse == '1':
        if playermana >= 40:
            playerhealth -= 20
            enemyhealth -= 60
            playermana -= 40
            print('You did 20 damage to yourself & 60 to your opponent!')
            time.sleep(2)
            if enemyhealth > 0:
                enemy_atk()
        else:
            print('Not enough mana! You need 60 mana!')
            time.sleep(2)
    elif spelluse == '2':
        if playermana >= 100:
            enemyhealth -= 100
            playermana -= 100
            print('You did 100 damage to your opponent!')
            time.sleep(2)
            if enemyhealth > 0:
                enemy_atk()
        else:
            print('not enough mana! You need 100 mana!')
            time.sleep(2)
    elif spelluse == '3':
        if playermana >= 40 and playerhealth < 500:
            playerhealth += 60
            playermana -= 60
            print('You healed 60 hp!')
            time.sleep(2)
            if enemyhealth > 0:
                enemy_atk()
        elif playerhealth >= 500:
            print('Your health is already full!')
            time.sleep(2)
        else:
            print('Not enough mana! You need 60 mana!')
            time.sleep(2)
    elif spelluse == '4':
        print('')
    else:
        print('Invalid action, try again')
        time.sleep(2)


def player_atk():
    global enemyhealth, playerattack
    if not playerattack:
        randplaydmg = random.randint(30, 50)
    if playerattack:
        randplaydmg = random.randint(50, 70)
        playerattack = False
    print(f'{playername} did {randplaydmg} damage!')
    enemyhealth -= randplaydmg
    if enemyhealth > 0:
        enemy_atk()


def atk_boss():
    global hitchance, enemyhealth, stagger
    if not stagger:
        hitchance = random.randint(1, 50)
    if stagger:
        hitchance = random.randint(1, 25)
        stagger = False
    if hitchance == 13:
        print('You hit and did 1 damage!')
        time.sleep(2)
        enemyhealth -= 1
    else:
        print('You missed!')
        time.sleep(2)
        boss_atk()


# this is the beginning of the game
def intro():
    clear_terminal()
    playername = input('What is your name?\n')
    print(f'Hello {playername}!')
    time.sleep(2)  # makes the text stay on screen for two seconds
    return playername


playername = intro()
while (
    playername.upper() == 'SECRETBOSS'
    and playerhealth > 0
    and enemyhealth > 0
):
    enemyhealth = 1
    clear_terminal()
    playermana += 20
    print(f'Player Health: {playerhealth} HP   \
    SHADOW OF GUSS: {enemyhealth} HP')
    print(f'Mana {playermana}')
    bossact = input('\nActions:\n[1] Attack\n[2] Spells\n[3] Run\n')
    if bossact == '1':
        atk_boss()
    elif bossact == '2':
        secretspell()
    elif bossact == '3':
        print('You Lost! :(')
        break
    else:
        print('Invalid input, try again')


while (
    not playername.upper() == 'SECRETBOSS'
    and playerhealth > 0
    and enemyhealth > 0
):
    clear_terminal()
    playermana += 20
    if playermana > manacap:
        playermana = manacap
    print(f'Player Health: {playerhealth}   Enemy Health: {enemyhealth}')
    print(f'Mana {playermana}\n')
    action = input('Actions:\n[1] Attack\n[2] Items\n[3] Spells\n[4] Run\n')
    if action == '1':
        player_atk()
    elif action == '2':
        item()
    elif action == '3':
        spell()
    elif action == '4':
        print('You gave up :(\n You Lost!')
        time.sleep(2)
        break
    else:
        print('Invalid action, try again')
        time.sleep(2)


while enemyhealth <= 0:
    print('You Won!')
    break


while playerhealth <= 0:
    print('You Lost :(')
    break
