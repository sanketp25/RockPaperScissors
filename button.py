import pygame
#font = pygame.font.SysFont('Arial', 40)
class Button:
    def __init__(self,x,y,width,height,color,buttonText) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.buttonText = buttonText
        self.rect = (self.x,self.y,self.width,self.height)
        
       
    def draw(self,win):
        pygame.draw.rect(win,self.color,self.rect)

    def is_clicked(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False    


