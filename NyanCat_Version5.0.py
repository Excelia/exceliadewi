#Author's Name: Excelia Dewi
#Last Modified By: Excelia Dewi
#Date Last Modified: 13 July 2013
""" 
  Program Description: this is a side scroller mini games, the main character is the famous nyan cat. 
                       user has control of nyan cat up and down by using mouse. nyan cat purpose is to 
                       save nyan baloon, every nyan baloon that nyan cat save will gain the score 
                       incremental 100. 
                       tac nayn(the original name but for in this game i will call it tac nyan for 
                       the purpose it is easier for me to call and type it as tac nyan) 
                       is the number one enemy of nyan cat and has to be avoided in all cost 
                       because it can decrease nyan cat life and can end up game over for the user.
                       the game has sound effect of nyan cat famous song, everytime the nyan cat hit 
                       tac nyan or save the nyan baloon there will be sound effect.
  
  Version 5.0 - *     Adding score and lives function. The lives is five and it will decrease everytime 
                      nyan cat hits tac nyan. The score will gain 100 each time nyan cat hit nyan baloon.
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
            self.sndBaloon = pygame.mixer.Sound("Nyan-baloon.ogg")
            self.sndTac = pygame.mixer.Sound("tac-nyan.ogg")
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
        
        
class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lives = 5
        self.score = 0
        self.font = pygame.font.SysFont("Lucida Console", 20)
        
    def update(self):
        self.text = "Nyan: %d | Score: %d" % (self.lives, self.score)
        self.image = self.font.render(self.text, 1, (255, 177, 0))
        self.rect = self.image.get_rect()
        self.rect.right = 600
        
def main():
    screen = pygame.display.set_mode((600 , 280))
    pygame.display.set_caption("Nyan Cat - Saving Nyan Baloon")

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
    scoreboard = Scoreboard()
    
    friendSprites = pygame.sprite.OrderedUpdates(space, baloon, nyan)
    tacSprites = pygame.sprite.Group(tac1,tac2,tac3,tac4)
    scoreSprites = pygame.sprite.Group(scoreboard)
    
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
        #check collisions
        if nyan.rect.colliderect(baloon.rect):
            nyan.sndBaloon.play()
            baloon.reset()
            scoreboard.score += 100


        hitTacs = pygame.sprite.spritecollide(nyan, tacSprites, False)
        if hitTacs:
            nyan.sndTac.play()
            scoreboard.lives -= 1
            if scoreboard.lives <= 0:
                print("Game over!")
                scoreboard.lives = 5
                scoreboard.score = 0
            for theTac in hitTacs:
                theTac.reset()
                
                
                
                
        friendSprites.update()
        tacSprites.update()
        scoreSprites.update()
        
        friendSprites.draw(screen)
        tacSprites.draw(screen)
        scoreSprites.draw(screen)
            
            
        
        
        pygame.display.flip()
    
    #return mouse cursor
    pygame.mouse.set_visible(True) 
if __name__ == "__main__":
    main()