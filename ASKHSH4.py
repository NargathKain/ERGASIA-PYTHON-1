import random

figure=["10","J","Q","K"]
card=[i for i in range(1,10)]+figure
colour=["C","S","H","D"]
DECK=[]
for i in colour:
	for j in card:
		DECK.append([i,j])
random.shuffle(DECK)

def card_value(c):
	if c[1] in figure:
		return 10
	else:
		return c[1]
		
def sum_score(LST):
	score=0
	for c in LST:
		score+=card_value(c)
	return score

for i in range(2):
    p1_count=0
    p2_count=0
    tie_count=0
    for j in range(100):
        random.shuffle(DECK)
        
        p1_score=0
        p2_score=0

        p1_cards=[]
        p2_cards=[]
        #prwto kai apeiraxto
        if i ==0:
            p1_cards=[DECK[0],DECK[1]]
            p1_score=sum_score(p1_cards)
            if p1_score < 15:
                p1_cards.append(DECK[4])
            p1_score=sum_score(p1_cards)
            
            p2_cards=[DECK[2],DECK[3]]
            p2_score=sum_score(p2_cards)
            if p2_score < 15:
                p2_cards.append(DECK[5])
            p2_score=sum_score(p2_cards)
        #deutero to peiragmeno
        if i ==1:
            tost= DECK[0]
            while True:
                if tost[1] in figure:
                    break
                else:
                    tost=[]
                    tost= random.choice(DECK)
                    random.shuffle(DECK)
            p1_cards = [tost, DECK[1]]
            p1_score=sum_score(p1_cards)
            tost=[]

            tost= DECK[2]
            while True:
                if tost[1] in figure:
                    tost=[]
                    tost= random.choice(DECK)
                    random.shuffle(DECK)
                else:
                    break
            p2_cards = [tost, DECK[3]]
            p2_score=sum_score(p2_cards)
            tost=[]
            
        if p1_score>p2_score:
            p1_count+=1
        elif p2_score>p1_score:
            p2_count+=1
        else:
            tie_count+=1
    print("\n")
    print(f"paixnidi {i+1}")
    print(f"nikes paixth 1: {p1_count}")
    print(f"nikes paixth 2: {p2_count}")
    print(f"     isopalies: {tie_count}")