def problem1():
    chosen_numbers, boards = get_input()

    index = 0
    numbers_so_far = []
    for i in range(0, 4):
        numbers_so_far.append(chosen_numbers[i])
        index = i
    index += 1

    bingo = None
    winning_board = None
    while bingo == None:
        numbers_so_far.append(chosen_numbers[index])
        index += 1

        for board in boards:
            bingo = check_rows(board, numbers_so_far)
            if bingo != None:
                winning_board = board
                break

            bingo = check_columns(board, numbers_so_far)
            if bingo != None:
                winning_board = board
                break

    last_number = int(numbers_so_far[len(numbers_so_far)-1])
    sum = 0
    for x in winning_board:
        if x not in numbers_so_far:
            sum += int(x)
    print("answer: ", last_number * sum)

def problem2():
    chosen_numbers, boards = get_input()

    index = 0
    numbers_so_far = []
    for i in range(0, 4):
        numbers_so_far.append(chosen_numbers[i])
        index = i
    index += 1

    winning_board = None
    last_winning_number = -1
    bingo = None
    while len(boards) > 0:
        numbers_so_far.append(chosen_numbers[index])
        index += 1

        for board in boards:
            bingo = check_rows(board, numbers_so_far)
            if bingo != None:
                last_winning_number = numbers_so_far[len(numbers_so_far)-1]
                winning_board = board
                boards.remove(board)

            bingo = check_columns(board, numbers_so_far)
            if bingo != None:
                last_winning_number = numbers_so_far[len(numbers_so_far)-1]
                winning_board = board
                try:
                    #a board can win with a row and a column on the same number,
                    #just eat the exception, it doesn't matter which wins
                    boards.remove(board)
                except ValueError as e:
                    print(e)

    sum = 0
    for x in winning_board:
        if x not in numbers_so_far:
            sum += int(x)
    print("answer: ", int(last_winning_number) * sum)
    

def get_input():
    chosen_numbers = []
    boards = []
    with open("../input/day4/problem1.in") as f:
        lines = f.readlines()
        chosen_numbers = lines.pop(0).strip()
        chosen_numbers = chosen_numbers.split(",")

        board = ""
        for line in lines:

            if line == '\n':
                if len(board) > 0:
                    board = board.split()
                    boards.append(board)
                    board = ""
                continue
            
            line = line.strip()
            board = board + " " + line

        board = board.split()
        boards.append(board)
    
    return chosen_numbers, boards

def check_rows(board, numbers):
    i = 0
    while i < len(board):
        row = board[i:i+5]

        count = 0
        for x in numbers:
            if x in row:
                count += 1

        if count == 5:
            return row

        i = i+5

def check_columns(board, numbers):

    col_num = 0
    while col_num < 5:
        column = []
        for i in range(0, 5):
            column.append(board[i*5+col_num])
            i += 5

        count = 0
        for x in numbers:
            if x in column:
                count += 1

        if count == 5:
            return column

        col_num += 1
    
if __name__ == "__main__":
    problem2()