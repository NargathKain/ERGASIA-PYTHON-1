import random

global figure

p1_count=0
p2_count=0
tie_count=0

card=[i for i in range(1,11)]
colour=["C","S","H","D"]
figure=["J","Q","K"]
card=card+figure

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

#edw 8a ginetai to aplo paixnidi
for j in range(100):
    random.shuffle(DECK)
    
    p1_score=0
    p2_score=0
    
    p1_cards=[]
    p2_cards=[]
    #ebala to if score < 15 
    #wste na moiazei pio alh8ino to paixnidi
    p1_cards=[DECK[0],DECK[1]]
    p1_score=sum_score(p1_cards)
    if p1_score < 15:
        p1_cards.append(DECK[5])
    p1_score=sum_score(p1_cards)
    
    p2_cards=[DECK[2],DECK[3]]
    p2_score=sum_score(p2_cards)
    if p2_score < 15:
        p2_cards.append(DECK[6])
    p2_score=sum_score(p2_cards)

    p1_cards.clear
    p2_cards.clear

    if p1_score>p2_score:
        p1_count+=1
    elif p2_score>p1_score:
        p2_count+=1
    else:
	    tie_count+=1


print("nikes paixth 1: ", p1_count)
print("nikes paixth 2: ", p2_count)
print("isopalies: ", tie_count)

p1_count=0
p2_count=0
tie_count=0

#edw 8a ginetai to klemmeno paixnidi
for k in range(100):
    random.shuffle(DECK)
    
    p1_score=0
    p2_score=0
    
    p1_cards=[]
    p2_cards=[]
    
    p1_cards=[DECK[0]]
    p1_score=sum_score(p1_cards)
    #edw pera kanw to klepsimo gia ton paixth 1
    #wste na 3ekinaei me 10 h figoura
    while p1_score < 9:
        p1_cards.clear
        random.shuffle(DECK)
        p1_cards.append(DECK[0])
        p1_score=sum_score(p1_cards)
    
    p1_cards.append(DECK[1])

    p1_score=sum_score(p1_cards)

    p2_cards=[DECK[2],DECK[3]]
    p2_score=sum_score(p2_cards)
    if p2_score < 15:
        p2_cards.append(DECK[6])
    p2_score=sum_score(p2_cards)

    p1_cards.clear
    p2_cards.clear

    if p1_score>p2_score:
        p1_count+=1
    elif p2_score>p1_score:
        p2_count+=1
    else:
	    tie_count+=1



print("nikes paixth 1: ", p1_count)
print("nikes paixth 2: ", p2_count)
print("isopalies: ", tie_count)

