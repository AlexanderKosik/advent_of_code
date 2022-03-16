import copy

class Bingo:
    def __init__(self, board):
        self.board = copy.deepcopy(board)

    def strike_out(self, number):
        for x, row in enumerate(self.board):
            for y, board_number in enumerate(row):
                if board_number == number:
                    self.board[x][y] *= -1

    def __str__(self):
        board = ""
        for row in self.board:
            line = " ".join(str(number) for number in row) + "\n"
            board += line
        return board


    def has_bingo(self):
        bingo = False
        for row in self.board:
            bingo |= all(number < 0 for number in row)
            if bingo:
                return True
        for column in zip(*self.board):
            bingo |= all(number < 0 for number in column)
            if bingo:
                return True
        return bingo

    def board_sum(self):
        return sum(number for row in self.board for number in row if number > 0)


    __repr__ = __str__

def create_bingo(f):
    board = []
    for _ in range(5):
        line = next(f)
        line.replace("\n", "")
        row = [int(number) for number in line.split()]
        board.append(row)
    return Bingo(board)

bingos = []
with open('si.txt') as f:
    numbers = next(f)
    try:
        while True:
            next(f) # skip newline
            b = create_bingo(f)
            bingos.append(b)
            #print(b)
    except  StopIteration:
        pass

    for number in numbers.split(","):
        for b in bingos:
            b.strike_out(int(number))
            if b.has_bingo():
                print("Bingo!")
                print(b)
                print("Board sum:", b.board_sum())
                print("Curr number:", number)
                print("Result:", b.board_sum() * int(number))


