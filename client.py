import pygame
from button import Button
from game import Game
from network import Network

width = 750
height = 750

window = pygame.display.set_mode((width,height))
pygame.display.set_caption('Client')

def redrawWindow(window,game,player):
    game = Game()
    window.fill((255,255,255))
    if not (game.isConnected()):
        font = pygame.font.SysFont("comicsans",80)
        text = font.render("Waiting for player...",1,(255,0,0))
        window.blit(text,(round(width/2) - text.get_width()//2),(height//2 - text.get_height()//2))
    else:
        font = pygame.font.SysFont("comicsans",60)
        text = font.render("Your Move",1,(0,255,0))
        window.blit(text,(80,200))

        text = font.render("Opponent's Move",1,(0,255,0))
        window.blit(text,(380,200))

        move1 = game.getPlayerMove(0)
        move2 = game.getPlayerMove(1)

        if game.bothWent():
            text1 = font.render(move1,1,(10,10,10))
            text2 = font.render(move2,1,(10,10,10))
        else:
            if game.player1Went and player == 0:
                text1 = font.render(move1,1,(10,10,10))
            elif game.player1Went:
                text1 = font.render("Locked in...",1,(10,10,10))
            else:
                text1 = font.render("Waiting...",1,(10,10,10))   

                
            if game.player2Went and player == 1:
                text1 = font.render(move2,1,(10,10,10))
            elif game.player2Went:
                text2 = font.render("Locked in...",1,(10,10,10))
            else:
                text2 = font.render("Waiting...",1,(10,10,10))    

        if player == 1:
            window.blit(text2, (100, 350))
            window.blit(text1, (400, 350))
        else:
            window.blit(text1, (100, 350))
            window.blit(text2, (400, 350))

        for btn in btns:
            btn.draw(window)

    pygame.display.update()






def main():
    run = True
    clock = pygame.time.Clock() 
    n = Network() 
   
    #player2 = Player()
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                # if player.rock.is_clicked(pos):
                #     n.send("Rock button clicked")
                #     #redrawWindow(window,player)
                    

                # if player.paper.is_clicked(pos): 
                #     n.send("Paper button clicked")
                #     #redrawWindow(window,player)  

                # if player.scissor.is_clicked(pos):
                #     n.send("Scissors button clicked")
                    #redrawWindow(window,player)
        # serverResponse = n.receive()
        # if serverResponse:
        #     print("Server Response: ",serverResponse)        
        # redrawWindow(window,player)    
                #run = False        

        redrawWindow(window,)
main()                



