import random

def compare_numbers(number, user_guess):
    ## your code here
    cows = 0 #cows = digit correct but wrong place
    bulls = 0 # bulls = digits correct and correct place
    for i in range(len(number)): #loop through each index
        if user_guess[i] == number[i]: #check if digit is exactly correct (bulls)
            bulls += 1 #add bull because its right digit in right place. also counted first because bull should not be counted as cow as well
        elif user_guess[i] in number: #or if digit is right somewhere in nbumber
            cows += 1 #add cow because right digit wrong place
    cowbull = (cows, bulls) #stores tuple result in var
    #my code ends here
    return (cowbull)

playing = True #gotta play the game
number = str(random.randint(0,9999)) #random 4 digit number
guesses = 0
print(number) #is printing the answer, but without brackets is giving error. kept with brackets and is displaying the ans but if we wanna remove cheating, we can comment this out. 

print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while playing:
    user_guess = input("Give me your best guess!") #raw_input never defined, changed to just input
    if user_guess == "exit":
        break
    cowbullcount = compare_numbers(number,user_guess)
    guesses+=1

    print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

    if cowbullcount[1]==4:
        playing = False
        print("You win the game after " + str(guesses) + "! The number was "+str(number))
        break #redundant exit
    else:
        print("Your guess isn't quite right, try again.")

