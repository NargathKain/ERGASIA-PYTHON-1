import random

def board_creation(j):
    global rows
    global col
    if j==0:
        rows=9
        col=rows
    elif j==1:
        rows = 8
        col=rows
    else:
        rows = 8
        col = 9
    tamplo = []
    for i in range(1,rows):
        for j in range(1,col):
            tamplo.append([i,j])
    rows-=1
    col-=1
    return tamplo 

for j in range (3):
    r_scr = 0
    b_scr = 0 
    board = board_creation(j)
    for i in range (100):
        logiki = True
        while logiki:
            rook = random.choice(board)
            bishop = random.choice(board)
            while bishop == rook:
                bishop = random.choice(board)
            if rook[0] == bishop[0] or rook[1] == bishop[1]:
                r_scr+=1
                logiki = False
            else:
                apolsthlh = abs(bishop[0] - rook[0])
                apolgrammh = abs(bishop[1] - rook[1])
                if j < 2:
                    if apolgrammh == apolsthlh:
                        b_scr+=1
                        logiki = False
                if j == 2:
                    if apolgrammh == apolsthlh + 1:
                        b_scr+=1
                        logiki = False
            del rook
            del bishop
    print(f"- - - - - apotelesmata pinaka {rows} epi {col} - - - - -")
    print(f"           score aksiomatikou {b_scr}")
    print(f"                 score pyrgoy {r_scr}\n")
