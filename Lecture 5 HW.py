import random

trials = 100
while trials > 0:
    trials -= 1
    cats = {0: False}, {1: False}, {2: False}
    print (cats)

a = random.randint(0,2) #attacker's selection
#print("a:", a)
a_dict = cats[a]   #assign a cat to the value the attacker selected
cats[a] = True     #assign this cat as the winner
#print("a_dict:", a_dict)


b = random.randint(0,2) #victim's selection
#print("b:", b)
b_dict = cats[b]    #assign a cat to the value the victim selected
#print("b_dict:", b_dict)

c = random.randint(0,2)  #losing cat that attacker reveals
#print("c:", c)
if cats[c] == cats[a]|cats[b]:    #if this cat has already been selected by either party, select a different cat
   c = random.randint(0,2)
c_dict = cats[c]
#print("c_dict:", c)
pop.cats[c]


if cats[a] == cats[b]:
   print("You win if you didn't switch")
elif a != b:
     print("You lose if you didn't switch")
        
a_dict = cats[(a + 1) % 2]
if cats[a] == cats[b]:
   print("You win if you switch")
elif a != b:
     print("You lose if you switch")
