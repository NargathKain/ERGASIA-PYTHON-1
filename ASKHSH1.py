import random 

global counter1
global game_not_over
global TAMPLO

TAMPLO = [0] * 9
THESEIS=[0,1,2,3,4,5,6,7,8]
game_not_over = False
counter1=0

#elegxoume an mporei na topo8eth8ei o daktylios sth 8esh
def seira_paixth(TAMPLO, THESEIS):
    
    log1 = False
    epilogh = random.randint(1,3)
    
    while log1 == False:
        
        if TAMPLO[random.choice(THESEIS)] == 0:
            TAMPLO[random.choice(THESEIS)] = epilogh
            log1 = True
        elif TAMPLO[random.choice(THESEIS)] < epilogh:
            TAMPLO[random.choice(THESEIS)] = epilogh
            log1 = True
        elif TAMPLO[random.choice(THESEIS)] > epilogh:
            log1 = True
    return TAMPLO


#tsekaroume an exei niki mesw twn functions
def check_if_game_over():
    if check_vert_horiz():
        return check_vert_horiz()
    if check_diagonal():
        return check_diagonal()




#elegxoume orizontia kai ka8eta an exoume niki me isa h au3ousa seira
def check_vert_horiz():
    log2 = False
    for i in range (3):
        if TAMPLO[i] == TAMPLO[3+i] == TAMPLO[i+6] !=0 :
            log2 = True
        if TAMPLO[i] == TAMPLO[i+1] == TAMPLO[i+2]  !=0 :
            log2 = True
        if TAMPLO[i] < TAMPLO[3+i] < TAMPLO[i+6] !=0 :
            log2 = True
        if TAMPLO[i] < TAMPLO[i+1] < TAMPLO[i+2]  !=0 :
            log2 = True    
        if TAMPLO[i] > TAMPLO[3+i] > TAMPLO[i+6] !=0 :
            log2 = True
        if TAMPLO[i] > TAMPLO[i+1] > TAMPLO[i+2]  !=0 :
            log2 = True  
    return log2

#elegxoume kai tis dyo diagwnies an exoume niki me isa h au3ousa seira
def check_diagonal():
    log3 = False
    if TAMPLO[0] == TAMPLO[4] == TAMPLO[8] !=0 :
        log3 = True
    if TAMPLO[2] == TAMPLO[4] == TAMPLO[6] !=0 :
        log3 = True
    if TAMPLO[0] < TAMPLO[4] < TAMPLO[8] !=0 :
        log3 = True
    if TAMPLO[2] < TAMPLO[4] < TAMPLO[6] !=0 :
        log3 = True
    if TAMPLO[0] > TAMPLO[4] > TAMPLO[8] !=0 :
        log3 = True
    if TAMPLO[2] > TAMPLO[4] > TAMPLO[6] !=0 :
        log3 = True
    return log3

#auto edw einai to kyrio programma opoy 8a kalesei ta function
#pou me th seira toys kai ekeina 8a kalesoun ta ypoloipa
counter1 = 1 
for j in range (100):
    TAMPLO = [0] * 9
    game_not_over = False
    while not game_not_over:
        #print(TAMPLO, counter1) to check if it works
        counter1 +=1 
        seira_paixth(TAMPLO, THESEIS)
        if counter1 >= 3:
            if check_vert_horiz():
                game_not_over = check_vert_horiz()
            if check_diagonal():
                game_not_over=check_diagonal() 

counter1=counter1/100
print(counter1)