import random

#elegxoume an mporei na topo8eth8ei o daktylios sth 8esh
def seira_paixth(TAMPLO):
    epilogh = random.randint(1,3)
    a = random.randint(0,8)
    while True:
        if TAMPLO[a] == 0:
            TAMPLO[a] = epilogh
            break
        elif TAMPLO[a] == epilogh:
            epilogh = random.randint(1,3)
        elif TAMPLO[a] > epilogh:
            break
        else:
            TAMPLO[a] = epilogh
            break
    return TAMPLO

#elegxoume orizontia
def check_horiz():
    gram1 = TAMPLO[0] == TAMPLO[1] == TAMPLO[2] !=0
    gram2 = TAMPLO[3] == TAMPLO[4] == TAMPLO[5] !=0
    gram3 = TAMPLO[6] == TAMPLO[7] == TAMPLO[8] !=0
    
    gram1m = TAMPLO[0] < TAMPLO[1] < TAMPLO[2] !=0
    gram2m = TAMPLO[3] < TAMPLO[4] < TAMPLO[5] !=0
    gram3m = TAMPLO[6] < TAMPLO[7] < TAMPLO[8] !=0

    if gram1:
        return True
    elif gram2:
        return True
    elif gram3:
        return True
    elif gram1m:
        return True
    elif gram2m:
        return True
    elif gram3m:
        return True
#elegxoume ka8eta
def check_vert():
    sthl1 = TAMPLO[0] == TAMPLO[3] == TAMPLO[6] !=0
    sthl2 = TAMPLO[1] == TAMPLO[4] == TAMPLO[7] !=0
    sthl3 = TAMPLO[2] == TAMPLO[5] == TAMPLO[8] !=0

    sthl1m = TAMPLO[0] < TAMPLO[3] < TAMPLO[6] !=0
    sthl2m = TAMPLO[1] < TAMPLO[4] < TAMPLO[7] !=0
    sthl3m = TAMPLO[2] < TAMPLO[5] < TAMPLO[8] !=0

    if sthl1:
        return True
    elif sthl2:
        return True
    elif sthl3:
        return True
    elif sthl1m:
        return True
    elif sthl2m:
        return True
    elif sthl3m:
        return True
#elegxoume kai tis dyo diagwnies
def check_diag():
    diag1 = TAMPLO[0] == TAMPLO[4] == TAMPLO[8]
    diag2 = TAMPLO[2] == TAMPLO[4] == TAMPLO[6]

    diag1m = TAMPLO[0] < TAMPLO[4] < TAMPLO[8]
    diag2m = TAMPLO[2] < TAMPLO[4] < TAMPLO[6]

    if diag1:
        return True
    elif diag2:
        return True
    elif diag1m:
        return True
    elif diag2m:
        return True
#auto edw einai to kyrio programma opoy 8a kalesei ta function
#pou me th seira toys kai ekeina 8a kalesoun ta ypoloipa
counter1 = 0
for j in range (100):
    TAMPLO =[0]*9
    metrhths=0
    logiki = True
    while logiki:
        counter1 +=1 
        metrhths +=1
        seira_paixth(TAMPLO)
        if metrhths >= 3:
            if check_horiz():
                logiki = False
            elif check_vert():
                logiki = False
            elif check_diag():
                logiki = False

counter1=counter1/100
print(counter1)