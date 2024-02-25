class Game:
    def __init__(self,id) -> None:
        self.id = id
        self.player1Went = False
        self.player2Went = False
        self.ready = False
        self.moves = [None,None]
        self.wins = [0,0]
        self.ties = 0
    def getPlayerMove(self,p):
        """
        There are two players. p => [0,1]
        """
        return self.moves[p]  
     
    def play(self,p,move):

        # This function:
        # 1. Assigns move to the the respective player.
        # 2. Returns which player played

        self.moves[p] = move 
        if p == 0:
            self.player1Went = True
        else:
            self.player2Went = True  

    def isConnected(self):
        return self.ready          

    def bothWent(self):
        return self.player1Went and self.player2Went
    
    def winner(self):
        """
        Get the initials of the moves of the players and run against various conditions
        """
        print("moves: ",self.moves
              
              )
        p0,p1 = self.moves[0].upper()[0],self.moves[1].upper()[0] #get the initials: R-> ROCK
        winner = -1
        if p0 == 'R' and p1 == 'S':
            winner = 0
        elif p0 == 'S' and p1 == 'R':   
            winner = 1
        elif p0 == 'S' and p1 == 'P':
            winner = 0
        elif p0 == 'P' and p1 == 'S': 
            winner = 1
        elif p0 == 'P' and p1 == 'R':
            winner = 0
        elif p0 == 'R' and p1 == 'P':
            winner = 1
        return winner
    def resetWent(self):
        self.player1Went = False
        self.player2Went = False                    


