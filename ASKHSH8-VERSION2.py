import random

rows =[1,2,3,4,5,6,7,8]
columns = [1,2,3,4,5,6,7,8]
board = []
for i in rows:
    for j in columns:
        board.append([i,j])

r_scr = 0
b_scr = 0 

#board 1 8*8
for i in range (100):
    game_not_over = False
    while not game_not_over:
        rook = random.choice(board)
        bishop = random.choice(board)
        while bishop == rook:
            bishop = random.choice(board)
        if rook[0] == bishop[0] or rook[1] == bishop[1]:
            r_scr+=1
            game_not_over = True
        else:
            apolsthlh = abs(bishop[0] - rook[0])
            apolgrammh = abs(bishop[1] - rook[1])
            if apolgrammh == apolsthlh:
                b_scr+=1
                game_not_over = True
        del rook
        del bishop

print("----------apotelesmata pinaka 8 epi 8--------------")
print("score pyrgoy ", r_scr)
print("score aksiomatikou ", b_scr)

rows =[1,2,3,4,5,6,7]
columns = [1,2,3,4,5,6,7]
board = []
for i in rows:
    for j in columns:
        board.append([i,j])

r_scr = 0
b_scr = 0 

#board 2 7*7
for i in range (100):
    game_not_over = False
    while not game_not_over:
        rook = random.choice(board)
        bishop = random.choice(board)
        while bishop == rook:
            bishop = random.choice(board)
        if rook[0] == bishop[0] or rook[1] == bishop[1]:
            r_scr+=1
            game_not_over = True
        else:
            apolsthlh = abs(bishop[0] - rook[0])
            apolgrammh = abs(bishop[1] - rook[1])
            if apolgrammh == apolsthlh:
                b_scr+=1
                game_not_over = True
        del rook
        del bishop

print("----------apotelesmata pinaka 7 epi 7--------------")
print("score pyrgoy ", r_scr)
print("score aksiomatikou ", b_scr)

rows =[1,2,3,4,5,6,7]
columns = [1,2,3,4,5,6,7,8]
board = []
for i in rows:
    for j in columns:
        board.append([i,j])

r_scr = 0
b_scr = 0 

#board 3 7*8
for i in range (100):
    game_not_over = False
    while not game_not_over:
        rook = random.choice(board)
        bishop = random.choice(board)
        while bishop == rook:
            bishop = random.choice(board)
        if rook[0] == bishop[0] or rook[1] == bishop[1]:
            r_scr+=1
            game_not_over = True
        else:
            apolsthlh = abs(bishop[0] - rook[0])
            apolgrammh = abs(bishop[1] - rook[1])
            if apolgrammh == apolsthlh + 1:
                b_scr+=1
                game_not_over = True
        del rook
        del bishop

print("----------apotelesmata pinaka 7 epi 8--------------")
print("score pyrgoy ", r_scr)
print("score aksiomatikou ", b_scr)