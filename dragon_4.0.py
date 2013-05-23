#name: Excelia Dewi
#source name: The Dragon Warrior Text Based Game
#Version: 4.0
#Last Modified Date: 22 May 2013
#last Modified By: Excelia Dewi
#Revision History: All the functionality works properly, adding some of the intro lines,
#                  Add elapse time in every text
#Program Description: Text Based Game, the user act as dragon warrior that has to save his dragon
#                     from the evil witch that wants to destroy earth. The dragon warrior has the obligation
#                     to guard earth from the hand of darkness evil and he cannot do his duty without his dragon.
#                     The game will make the user to choose decision in each stage of the game and each decision
#                     will lead user to 8 death or 1 victory.

import random
import time

def displayIntro():
    print ('You are the dragon warrior, the guardian of earth')
    time.sleep(1)
    print ('Earth had been attack by evil witch that want to conquer the earth')
    time.sleep(1)
    print ('The witch know that you will not defeat him if he separate you with your dragon')
    time.sleep(1)
    print ('So he kidnapped your dragon')
    time.sleep(1)
    print ('In order to save earth you need to get back your dragon')
    time.sleep(1)
    print ('Therefore you will have a journey to release your dragon')
    time.sleep(1)
    print ('In order to kill that evil witch and save the earth!')
    time.sleep(2)
    print ('you are going to start your journey to get back your dragon')
    time.sleep(1)
    print ('you are walking...')
    time.sleep(1)
    print ('you are stopping because there are two branch road and you have to choose')
    
def chooseRoad():
    road = ''
    while road != '1' and road != '2':
        time.sleep(1)
        print ('Which road you will choose 1=rocky road or 2=sandy road? (1 or 2)')
        road = raw_input()
    return road

def checkRoad(chosenRoad): 
    print ('You are walking towards the road')
    time.sleep(1)
    print ('Then all of the sudden...')
    time.sleep(2)
    
    if chosenRoad == "1":
        print('you are at the big spacious area')
        time.sleep(1)
        print ('you face jungle and mountain')
        time.sleep(2)
        print ('the jungle is full of gigantic spider and the mountain is full of rattlesnake')
        jungleAndMountain()
        
    elif chosenRoad == "2": 
        print('you will face the lake and the river')
        time.sleep(2)
        print ('the lake is full of flying electric eel and the river is full of piranha')
        time.sleep(1)
        lakeAndRiver()
    return chosenRoad

def lakeAndRiver():
    print('the witch know that you want to save your dragon')
    time.sleep(1)
    print('so he send his zombie army to eat your brain')
    time.sleep(1)
    print('in order to escape from the zombie you have to choose your way between river and lake')
    time.sleep(1)
    print('there a huge piece of wood that you can use to cross both lake and river')
    time.sleep(2)
    pick_path =''
    
    while pick_path !='1' and pick_path != '2':
            print('make your way 1=river and 2=lake')
            time.sleep(1)
            break
    pick_path = raw_input('')
    
    if pick_path == "1":
        print('you grab the wood and right away and start cross the river')
        time.sleep(1)
        lakePath()
    elif pick_path == "2":
        print('you grab the wood and right away and start cross the lake')
        time.sleep(1)
        riverPath()
        return pick_path


def jungleAndMountain():
    print('the witch know that you want to save your dragon')
    time.sleep(1)
    print('so he send his zombie army to eat your brain')
    time.sleep(1)
    print('in order to escape from the zombie you have to choose your way between jungle and mountain')
    time.sleep(1)
    pick_path =''
    
    while pick_path !='1' and pick_path != '2':
            print('make your way 1=jungle and 2=mountain')
            time.sleep(1)
            break
    pick_path = raw_input('')
    
    if pick_path == "1":
        print('you run toward the deadliest jungle')
        time.sleep(1)
        junglePath()
    elif pick_path == "2":
        mountainPath()
        return pick_path

def riverPath():
    print('youre crossing the lake now')
    time.sleep(1)
    print('you can see through the water that group of piranha try to attack you')
    time.sleep(1)
    print('you can a lot of snakes want to attack you from the branches at the tree along the river')
    time.sleep(1)
    print('you have to make quick decision!')
    time.sleep(1)
    choose_action = ''
    while choose_action != '1' and choose_action != '2':
        print ('What would you do? 1=jump to the water or 2=keep stand still on top of the wood?')
        time.sleep(1)
        break
    choose_action = raw_input('')
    
    if choose_action == '1':
            print ('you jump into water')
            time.sleep(1)
            print('you try to swim as fast as you can')
            time.sleep(1)
            print('but its too late the piranha already eat you, you die')
    elif choose_action == '2':
            print('you just stand still and try to kill the snake')
            time.sleep(1)
            print('you kill some of snakes but there are too many of them that you get bitten')
            time.sleep(1)
            print('you fall over into the water and get eaten by piranhas')   
            time.sleep(1)
    return choose_action  

def lakePath():
    print('youre crossing the lake now')
    time.sleep(1)
    print('you can see from the distance that a group of electric eel are flying towards you')
    time.sleep(1)
    print('you have to make quick decision!')
    time.sleep(1)
    choose_action = ''
    while choose_action != '1' and choose_action != '2':
        print ('What would you do? 1=jump to the water or 2=keep stand still on top of the wood?')
        time.sleep(1)
        break
    choose_action = raw_input('')
    
    if choose_action == '1':
            print ('you jump into water')
            time.sleep(1)
            print('the electric eel kill you and eat your corps')
    elif choose_action == '2':
            print('you just stand still and prepare to attack back')
            time.sleep(1)
            print('you kill some of the electric eel but there are so many of them')
            time.sleep(1)
            print('you get electrocuted and you die')   
            time.sleep(1)
    return choose_action   
    

def junglePath():
    print('youre at the deadliest jungle in the world')
    time.sleep(1)
    print('you feel that something following you')
    time.sleep(1)
    choose_action = ''
    while choose_action != '1' and choose_action != '2':
        print ('What would you do? 1=swing by the vines or 2=keep walking on the ground?')
        time.sleep(1)
        break
    choose_action = raw_input('')
    
    if choose_action == '1':
            print ('you trapped at the gigantic spider web, you cannot move')
            time.sleep(1)
            print('you get eaten by the giant spider')
    elif choose_action == '2':
            print('you realized there is a giant spider chasing you, the giant spider want to eat you')
            time.sleep(1)
            print('you can escape from the giant spider by hiding at the bushes')
            time.sleep(1)
            print('but you trapped at the quicksand and you die because nobody can help you')   
            time.sleep(1)
    return choose_action

def mountainPath():
    print('youre at the mountain that full of rattlesnake')
    time.sleep(1)
    print('you can see the snake are coming out behind the rock')
    time.sleep(1)
    print('you have two options to escape from the snake')
    time.sleep(1)
    choose_action = ''
    while choose_action != '1' and choose_action != '2':
        print ('What would you do? 1=Go climb the mountain or 2=Go down the mountain?')
        time.sleep(1)
        break
    choose_action = raw_input('')
    
    if choose_action == '1':
            print ('You climbed the rocky mountain')
            time.sleep(2)
            print ('Behind the huge rock you can see your dragon trapped in the rock prison')
            time.sleep(2)
            print ('so you decide to go to your dragon and release it with your special power')
            time.sleep(2)
            print('your dragon get release and burn down all the snakes')
            time.sleep(1)
            print('you and your dragon are flying to evil witch castle and kill him without mercy!')
            time.sleep(3)
            print('congratulations you save the world, dragon warrior!')
    elif choose_action == '2':
            print('you go down the mountain and try to escape from the snake')   
            time.sleep(1)
            print('but there are too much snake and you get bitten by them')   
            time.sleep(1)
            print('your body become paralyzed and you get eaten by the snake')   
            time.sleep(1)
    return choose_action


def main():
    
    
    playAgain = 'yes'
    while playAgain == 'yes' or playAgain == 'y':
        displayIntro()
        roadNumber = chooseRoad()
        checkRoad(roadNumber)
    
        print ('Do you want to play again? (yes or no)')
        playAgain = raw_input()


if __name__ == "__main__": main()
