import sys
# Make a tictac game
'''
Rules and specs:

Set up:
1. 2 players(command line input the coordinate of the move)
2. 1 board(3x3 matrix using "x" and "o" to indicate a move)

Rules:
1. 1 user can only make 1 move. ALTERNATE
2. winner: 3 same char in a row (vertial/horizontal/diagonal) or a player quits
3. no winner: winner = FALSE
4. player 1 uses "x", player 2 uses "o"

'''

# Helper functions here:
def parse_move(move, gm):
    
    while True:
        if move == "QUIT":
            break
        else:
            try:
                move = move.split(",")
                if len(move) == 2:
                    move = (int(move[0]), int(move[1]))
                    if (move[0] in [0,1,2] and move[1] in [0,1,2] 
                        and gm._board[move[0]][move[1]] == 0):
                        break

                print("The move you entered in invalid, please do enter your move:")
                move = input()
            except:
                print("The move you entered in invalid, please do enter your move:")
                move = input()
        
    return move

class Player:
    '''
    A Player is instantiated with name, which is passed in in the argument
    '''
    name = ""

    def __init__(self,name):
        self.name = name

    def make_move(self, move):
        return move

class GameManager:


    players = [None,None]
    winner = None
    
    def __init__(self):
        self.winner = None
        self._board = [[0 for _ in range(3)] for _ in range(3)]

    def set_players(self, players):     
        self.players = players
    
    def update_board(self, move, player):
        if move == "QUIT":
            if player == self.players[0]:
                self.winner = self.players[1]
            else:
                self.winner = self.players[0]
            print("The winner is {}".format(self.winner.name))
            print("Thank you for playing")
            sys.exit(0)

        else:
            if player == self.players[0]:
                self._board[move[0]][move[1]] = "x"
            else:
                self._board[move[0]][move[1]] = "o"
        print(self._board)

    def check_winner(self):
        # check horizontal
        for row in self._board:
            if row[0] == row[1] and row[1] == row[2] and row[0] != 0:
                if row[0] == "x":
                    self.winner = self.players[0].name
                else:
                    self.winner = self.players[1].name
                return True
        
        # check vertical
        for col in range(3):
            if self._board[0][col] == self._board[1][col] and self._board[1][col] == self._board[2][col] and self._board[0][col] != 0:
                if self._board[0][col] == "x":
                    self.winner = self.players[0].name
                else:
                    self.winner = self.players[1].name
                return True
        
        # check diagnol
        if self._board[0][0] == self._board[1][1] and self._board[1][1] == self._board[2][2] and self._board[0][0] != 0:
            if self._board[0][0] == "x":
                self.winner = self.players[0].name
            else:
                self.winner = self.players[1].name
            return True

        # check tie
        while True:
            for row in self._board:
                if row[0] == 0 or row[1] == 0 or row[2] ==0:
                    return False
            self.winner = "{} and {}".format(self.players[0].name,self.players[1].name)
            return True
                    
        return False

# Program code
def play_game():

    # initialize the game 
    print("Tictactoe game is starting!")
    gm = GameManager()
    print("Player 1, please enter your name:")
    name1 = input()
    p1 = Player(name1)
    print("Player 2, please enter your name:")
    name2 = input()
    p2 = Player(name2)
    gm.set_players([p1,p2])
    print("We have players: {} and {}. Have fun!".format(p1.name,p2.name))

    # check game status
    print(gm._board)
    while True:
        print("{}, please enter your move or QUIT to quit the game".format(p1.name))
        coord = parse_move(input(),gm)
        print("{}, your move is {}".format(p1.name,coord))
        move = p1.make_move(coord)
        gm.update_board(move,p1)
        
        if gm.check_winner():
            print("The winner is {}".format(gm.winner))
            break
        else:
            print("{}, please enter your move or QUIT to quit the game".format(p2.name))
            coord = parse_move(input(),gm)
            move = p2.make_move(coord)
            gm.update_board(move,p2)
            if gm.check_winner():
                print("The winner is {}".format(gm.winner))
                break

    # system exit when break out of the loop
    print("Thank you for playing")
    sys.exit(0)

if __name__ == "__main__":
    play_game()







    