#Author's Name: Excelia Dewi
#Last Modified By: Excelia Dewi
#Date Last Modified: 7 July 2013
""" 
  Program Description: this is a side scroller mini games, the main character is the famous nyan cat. 
                       user has control of nyan cat up and down by using mouse. nyan cat purpose is to 
                       save nyan baloon, every nyan baloon that nyan cat save will gain the score 
                       incremental 100. 
                       tac nayn is the number one enemy of nyan cat and has to be avoided in all cost 
                       because it can decrease nyan cat life and can end up game over for the user.
                       the game has sound effect of nyan cat famous song, everytime the nyan cat hit 
                       tac nayn or save the nyan baloon there will be sound effect.
  
  Version 1.0 - * show nyan cat sprite that can move up and down according to the mouse movemement
                  the limit of the nyan cat motion is based on the height screen of game,
                  so the character cannot go further than the game screen.
                  set the background to 600x280(widthxheight)
    """
    
import pygame
pygame.init()

class NyanCat(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("nyan-rainbow.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        
    def update(self):
        mousex, mousey = pygame.mouse.get_pos()
        if mousey > 265:
            mousey = 265   
        if mousey < 15:
            mousey = 15
        self.rect.center = (40, mousey)

        
def main():
    screen = pygame.display.set_mode((600 , 280))
    pygame.display.set_caption("Nyan Cat!")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 255))
    screen.blit(background, (0, 0))
    nyan = NyanCat()
    
    allSprites = pygame.sprite.Group(nyan)
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        
        pygame.display.flip()
    
    #return mouse cursor
    pygame.mouse.set_visible(True) 
if __name__ == "__main__":
    main()