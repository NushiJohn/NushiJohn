import numpy


d = int(input("Enter number of dice: "))    #dice to be rolled during each trial
a = int(input("Enter first desired value: "))
b = int(input("Enter second desired value: "))  #target numbers that the user wants to compare
diceRolled = d   #retains value of d for while loop
aOccurences = 0
bOccurences = 0  #keep track of how often a and b show up as sums respectively
s = 0       #variable to keep track of sums during each trial
trials = 1000000   #number of trials to be ran, can be adjusted

while trials > 0:   #outer loop runs individual trials
    trials -= 1
    d = diceRolled
    s = 0  #reset s and d to their original values for use in inner loop
    #print("Trial"), optional marker for seeing individual trials
    while d > 0:        #inner loop runs and sums individual rolls
        x = numpy.random.randint(1,7)
        s += x      #add a roll to the sum for the current trial
        #print(x), optional marker for each individual roll
        d -= 1
        if d == 0:
            #print (s), optional marker for each individual sum
            if a == s:
                aOccurences += 1
            if b == s:
                bOccurences += 1    #keep track of how often a and b are a sum
       
print("aOccurences:")
print(aOccurences)
print("bOccurences:")
print(bOccurences)
proportion = aOccurences/bOccurences    #Divide aOccurences by bOccurences to see which number 
print("aOccurences/bOccurences:")       #occurs more often, or if they are equally likely.
print(proportion)                       #If the two numbers' occurences are within
                                        #5% of each other, they are about equally likely.
if proportion > 1:
    if proportion < 1.05:
        print("a and b both occur just as often")
    elif proportion > 1.05:
        print("a occurs more often than b")
elif proportion < 1:
    if proportion > 0.95:
        print("a and b both occur just as often")
    elif proportion < 0.95:
        print("b occurs more often than a")
