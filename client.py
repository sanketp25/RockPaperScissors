import pygame
from player import Player

width = 750
height = 750

window = pygame.display.set_mode((width,height))
pygame.display.set_caption('Client')

def redrawWindow(window,player,player2):
    window.fill((255,255,255))
    player.draw(window)
    player2.draw(window)
    pygame.display.flip()    

def main():
    run = True
    player = Player()
    player2 = Player()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if player.rock.is_clicked(pos):
                    print("Rock button clicked")

                if player.paper.is_clicked(pos): 
                    print("Paper button clicked")  

                if player.scissor.is_clicked(pos):
                    print("Scissors button clicked")

        redrawWindow(window,player,player2)
main()                



