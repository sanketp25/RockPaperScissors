import pygame

width = 750
height = 750

window = pygame.display.set_mode((width,height))
pygame.display.set_caption('Client')

def redrawWindow(window,player):
    window.fill((255,255,255))
    player.draw(window)
    pygame.display.flip()

# class RPS_Game:
#     def __init__(self) -> None:
#         button_surface = pygame.Surface((100,100))
#         # self.rock = (100,350)
#         # self.paper = (310,350)
#         # self.scissor = (520,350)
#     def draw(self,window):
#         pygame.draw.rect(window,(255,0,0),self.rock)
#         pygame.draw.rect(window,(0,255,0),self.paper)
#         pygame.draw.rect(window,(0,0,255),self.scissor)
#     # def click(self)        
       
def main():
    run = True
    p = RPS_Game()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        redrawWindow(window,p)
main()                



