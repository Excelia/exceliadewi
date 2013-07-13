#Author's Name: Excelia Dewi
#Last Modified By: Excelia Dewi
#Date Last Modified: 13 July 2013
""" 
  Program Description: this is a side scroller mini games, the main character is the famous nyan cat. 
                       user has control of nyan cat up and down by using mouse. nyan cat purpose is to 
                       save nyan baloon, every nyan baloon that nyan cat save will gain the score 
                       incremental 100. 
                       tac nayn is the number one enemy of nyan cat and has to be avoided in all cost 
                       because it can decrease nyan cat life and can end up game over for the user.
                       the game has sound effect of nyan cat famous song, everytime the nyan cat hit 
                       tac nayn or save the nyan baloon there will be sound effect.
  
  Version 3.0 - * adding new sprites, tac nyan the enemy and nyan baloon.
                  both sprites scrolles in same direction with background and has different speed.
                  and adding the music background that loops through the game
    """
    
import pygame, random
pygame.init()

screen = pygame.display.set_mode((600, 280))

class NyanCat(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("nyan-rainbow.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        
        if not pygame.mixer:
            print("Problem with sound")
        else:
            pygame.mixer.init()

            self.sndNyan = pygame.mixer.Sound("nyan_sound.ogg")
            self.sndNyan.play(-1)
        
    def update(self):
        mousex, mousey = pygame.mouse.get_pos()
        if mousey > 265:
            mousey = 265   
        if mousey < 15:
            mousey = 15
        self.rect.center = (38, mousey)

class Space(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("space.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.dx = 20
        self.reset()
        
    def update(self):
        self.rect.right -= self.dx
        if self.rect.right == screen.get_width():
            self.reset() 
    
    def reset(self):
        self.rect.left = 0
        
class TacNyan(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("tac-nyan.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
        


    def update(self):
        self.rect.centerx -= self.dx
        self.rect.centery -= self.dy
        if self.rect.right < -1:
            self.reset()
    
    def reset(self):
        self.rect.left = 600
        self.rect.centery = random.randrange(0, screen.get_width())
        self.dy = random.randrange(1, 2)
        self.dx = random.randrange(10, 12)
        
class NyanBaloon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("nyan-baloon.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
        
        self.dx = 10
        
    def update(self):
        self.rect.right -= self.dx;
        if self.rect.right < -1:
            self.reset()
            
    def reset(self):
        self.rect.left = 600
        self.rect.centery = random.randrange(0, screen.get_height())
        
        
def main():
    screen = pygame.display.set_mode((600 , 280))
    pygame.display.set_caption("Nyan Cat!")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    nyan = NyanCat()
    baloon = NyanBaloon()
    space = Space()
    tac1 = TacNyan()
    tac2 = TacNyan()
    tac3 = TacNyan()
    tac4 = TacNyan()
    
    friendSprites = pygame.sprite.OrderedUpdates(space, baloon, nyan)
    tacSprites = pygame.sprite.Group(tac1,tac2,tac3,tac4)
    
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
        friendSprites.update()
        friendSprites.draw(screen)

        tacSprites.update()
        tacSprites.draw(screen)
            
            
        
        
        pygame.display.flip()
    
    #return mouse cursor
    pygame.mouse.set_visible(True) 
if __name__ == "__main__":
    main()