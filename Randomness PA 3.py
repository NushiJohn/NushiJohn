import random

def gsr(l):     #gsr function
    length = len(l)
    left_hand_pile = []   #create empty lists for the left hand pile,
    right_hand_pile = []   #right hand pile, and the resulting shuffled deck
    shuffled_deck = []
    desired_shuffles = 3   #set how many shuffles are to be done
    while desired_shuffles > 0:
        desired_shuffles -= 1
        while length > 0:
            length -= 1
            top_card = l[length]   #position of the current top card
            x = random.randint(1,3)
            if x == 1:
                left_hand_pile.append(top_card)   #add that card to the left pile
            else:
                right_hand_pile.append(top_card)  #or add that card to the right pile
        length = len(l)
        left_length = len(left_hand_pile)
        right_length = len(right_hand_pile)
        while length > 0:
            length -= 1
            x = random.randint(1,3)
            if x == 1:
                if left_length == 0:   #if the left pile is empty, add from the right pile
                    right_length -= 1
                    right_top = right_hand_pile[right_length]
                    shuffled_deck.append(right_top)
                else:
                    left_length -= 1  #add from the left pile
                    left_top = left_hand_pile[left_length]
                    shuffled_deck.append(left_top)
            else:
                if right_length == 0:  #if the right pile is empty, add from the left pile
                    left_length -= 1
                    left_top = left_hand_pile[left_length]
                    shuffled_deck.append(left_top)
                else:
                    right_length -= 1   #add from the right pile
                    right_top = right_hand_pile[right_length]
                    shuffled_deck.append(right_top)

    #print("Original deck:", l)
    #print("Left hand:", left_hand_pile)
    #print("Right hand:", right_hand_pile)
    #print("GSR shuffled deck:", shuffled_deck)

            
def top_to_random(l):  #top to random function
    length = len(l)
    shuffled_deck = list.copy(l)
    desired_shuffles = 7   #set how many times the deck is to be shuffled
    while desired_shuffles > 0:
        desired_shuffles -= 1
        random_position = random.randint(0,length)  #random position where the card will go  
        top_card = shuffled_deck[length-1]
        shuffled_deck.insert(random_position,top_card)  #put the card in that position
        shuffled_deck.pop(); #pop off that card's original position

    #print("Original deck:", l)
    #print("TtR shuffled deck:", shuffled_deck)


successful_trials = 0
total_trials = 0  
def test_order_gsr(i,j,l):
    desired_card1 = i
    desired_card2 = j
    position1 = l.index(i)
    position2 = l.index(j)
    global successful_trials
    global total_trials
    if position1 > position2:
        #print(i, "is above", j)
        successful_trials += 1
        total_trials += 1
        return True
    else:
        #print(i, "is not above", j)
        total_trials += 1
        return False

def test_order_ttr(i,j,l):
    desired_card1 = i
    desired_card2 = j
    position1 = l.index(i)
    position2 = l.index(j)
    global successful_trials
    global total_trials
    if position1 > position2:
        #print(i, "is above", j)
        successful_trials += 1
        total_trials += 1
        return True
    else:
        #print(i, "is not above", j)
        total_trials += 1
        return False

def main_gsr():
    l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    i = 6
    j = 8
    trials = 20
    global successful_trials
    global total_trials
    while trials > 0:
        trials -= 1
        gsr(l)
        test_order_gsr(i,j,l)
    success_rate = successful_trials/total_trials
    print("Success rate:",success_rate)

def main_ttr():
    l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    i = 3
    j = 11
    trials = 20
    global successful_trials
    global total_trials
    while trials > 0:
        trials -= 1
        top_to_random(l)
        test_order_ttr(i,j,l)
    success_rate = successful_trials/total_trials
    print("Success rate:",success_rate)
