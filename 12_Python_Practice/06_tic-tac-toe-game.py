class TicTacToe:
    def __init__(self):
        self.board =  [' ' for _ in range(9)] #we will use a single list to represent 3x3 board
        self.current_winner = None #Keep track of the winner! whether there is a current winner, and there is, who is the winner.

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            #first row : i=0 -> first row is ....
            #갑자기 어려워짐
            # https://youtu.be/8ext9G7xspg
            #39:30 부터 다시보기
