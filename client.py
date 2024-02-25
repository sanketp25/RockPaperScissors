import pygame
from button import Button

from network import Network
pygame.font.init()


width = 750
height = 750

win = pygame.display.set_mode((width,height))
pygame.display.set_caption('Client')

def redrawWindow(win,game,player):
    
    win.fill((255,255,255))
    if not (game.isConnected()):
        font = pygame.font.SysFont("comicsans",80)
        text = font.render("Waiting for player...",1,(255,0,0))
        win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
    else:
        font = pygame.font.SysFont("comicsans",60)
        text = font.render("Your Move",1,(0,255,0))
        win.blit(text,(80,200))

        text = font.render("Opponent's Move",1,(0,255,0))
        win.blit(text,(380,200))

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
                text2 = font.render(move2,1,(10,10,10))
            elif game.player2Went:
                text2 = font.render("Locked in...",1,(10,10,10))
            else:
                text2 = font.render("Waiting...",1,(10,10,10))    

        if player == 1:
            win.blit(text2, (100, 350))
            win.blit(text1, (400, 350))
        else:
            win.blit(text1, (100, 350))
            win.blit(text2, (400, 350))

        for btn in buttons:
            btn.draw(win)

    pygame.display.update()


buttons = [Button(50,500,150,100,(0,255,255),"Rock"),Button(250,500,150,100,(255,0,255),"Scissors"),Button(450,500,150,100,(255,255,0),"Paper")]



def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    player = int(n.get_P())
    print("You are player", player)

    while run:
        clock.tick(60)
        try:
            game = n.send("get")
        except:
            run = False
            print("Couldn't get game")
            break

        if game.bothWent():
            redrawWindow(win, game, player)
            pygame.time.delay(500)
            try:
                game = n.send("reset")
            except:
                run = False
                print("Couldn't get game")
                break

            font = pygame.font.SysFont("comicsans", 90)
            if (game.winner() == 1 and player == 1) or (game.winner() == 0 and player == 0):
                text = font.render("You Won!", 1, (255,0,0))
            elif game.winner() == -1:
                text = font.render("Tie Game!", 1, (255,0,0))
            else:
                text = font.render("You Lost...", 1, (255, 0, 0))

            win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(2000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in buttons:
                    if btn.click(pos) and game.isConnected():
                        if player == 0:
                            if not game.player1Went:
                                n.send(btn.text)
                        else:
                            if not game.player2Went:
                                n.send(btn.text)

        redrawWindow(win, game, player)

def menu_screen():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        win.fill((128, 128, 128))
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Click to Play!", 1, (255,0,0))
        win.blit(text, (100,200))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    main()

while True:
    menu_screen()              



