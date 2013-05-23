#name: Excelia Dewi
#Version: 3.0
#Date: 22 May 2013    
#Program Description: Text Based Game, the user act as dragon warrior that has to save his dragon
#                     from the evil witch that wants to destroy earth. The dragon warrior has the obligation
#                     to guard earth from the hand of darkness evil and he cannot do his duty without his dragon.
#                     The game will make the user to choose decision in each stage of the game and each decision
#                     will lead user to 8 death and 1 victory.

import random
import time

def displayIntro():
    print ('You are the dragon warrior, the guardian of earth')
    print ('Earth had been attack by evil witch that want to conquer the earth')
    print ('The witch know that you will not defeat him if he separate you with your dragon')
    print ('So he kidnapped your dragon')
    print ('In order to save earth you need to get back your dragon')
    print ('Therefore you will have a journey to release your dragon')
    print ('In order to kill that evil witch and save the earth!')
    print
    
def chooseRoad():
    road = ''
    while road != '1' and road != '2':
        print ('Which road you will choose 1=rocky road or 2=sandy road? (1 or 2)')
        road = raw_input()
    return road

def checkRoad(chosenRoad): 
    print ('You are walking towards the road')
    time.sleep(2)
    print ('Then all of the sudden...')
    time.sleep(2)
    
    if chosenRoad == "1":
        print('you are at the big spacios area')
        print ('you face jungle and mountain')
        time.sleep(2)
        print ('the jungle is full of gigantic spider and the mountain is full of rattlesnake')
        jungleAndMountain()
        
    elif chosenCave == "2": 
        print('you will face the lake and the river')
        time.sleep(2)
        print ('the lake is full of electric eel and the river is full of piranha')
        lakeAndRiver()
    return chosenRoad

def jungleAndMountain():
    print('the witch know that you want to save your dragonn')
    print('so he send his zombie army to eat your brain')
    print('in order to escape from the zombie you have to choose your way between jungle and mountain')
    pick_path =''
    
    while pick_path !='3' and pick_path != '4':
            print('make your way 3=jungle and 4=mountain')
            break
    pick_path = raw_input('')
    
    if pick_path == "3":
        print('you run toward the deadliest jungle')
        junglePath()
    elif pick_path == "4":
    
        return pick_path
 
    
    

def junglePath():
    print('youre at the deadliest jungle in the world')
    time.sleep(1)
    print('you feel that something following you')
    
    choose_action = ''
    while choose_action != '5' and choose_action != '6':
        print ('What would you do? 5=swing by the vines or 6=keep walking on the roads?')
        break
    choose_action = raw_input('')
    
    if choose_action == '5':
            print ('you trapped at the gigantic spider web and its the end of your life')
    elif choose_action == '6':
            print('you trapped at the quicksand and you will die!')   
    
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
