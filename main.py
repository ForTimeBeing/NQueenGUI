import pygame

QUEENS = 15
SIZE_OF_SQUARES = 30


def printSolution(board):
    for i in range(QUEENS):
        for j in range(QUEENS):
            print(board[i][j], end=" ")
        print()


def main():
    board = [[0 for col in range(QUEENS)] for row in range(QUEENS)]
    if not backTrack(board, 0):
        print("Solution does not exist")
        return False
    printSolution(board)
    return True


def backTrack(board, col):
    # base case: If all queens are placed
    # then return true
    if col >= QUEENS:
        return True
    # Consider this column and try placing
    # this queen in all rows one by one
    for i in range(QUEENS):
        if canPlace(board, i, col):
            # Place this queen in board[i][col]
            board[i][col] = 1

            placeQueen((board[i],board[col]))

            # recur to place rest of the queens
            if backTrack(board, col + 1):
                return True
            # If placing queen in board[i][col
            # doesn't lead to a solution, then
            # queen from board[i][col]
            board[i][col] = 0

    # if the queen can not be placed in any row in
    # this colum col then return false
    return False


def placeQueen(row,col):
    print("x")


def canPlace(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
        # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
        # Check lower diagonal on left side
    for i, j in zip(range(row, QUEENS, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def createBoard():
    pygame.init()
    running = True
    (width, height) = (SIZE_OF_SQUARES * QUEENS, SIZE_OF_SQUARES * QUEENS)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('N-Queens')
    background_colour = (255, 255, 255)
    screen.fill(background_colour)
    while running:
        width_of_board = 0
        height_of_board = 0
        every_other_color = 0
        for i in range(0, QUEENS):
            for n in range(0, QUEENS):
                if every_other_color == 0:
                    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(width_of_board, height_of_board, 30, 30))
                    every_other_color = every_other_color + 1
                else:
                    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(width_of_board, height_of_board, 30, 30))
                    every_other_color = 0
                width_of_board = width_of_board + SIZE_OF_SQUARES
            height_of_board = height_of_board + SIZE_OF_SQUARES
            width_of_board = 0
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


main()
# createBoard()
