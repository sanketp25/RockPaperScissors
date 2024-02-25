import pygame
#font = pygame.font.SysFont('Arial', 40)
class Button:
    def __init__(self,x,y,width,height,color,text) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.rect = (self.x,self.y,self.width,self.height)
        
       
    def draw(self,win):
        pygame.draw.rect(win,self.color,self.rect)
        font = pygame.font.SysFont("comicsans",40)
        text = font.render(self.text,1,(255,255,255))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False    


