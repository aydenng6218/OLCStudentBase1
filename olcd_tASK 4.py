'''
2018 - Task 4 [20]
You have been asked to create a guessing game program.
The program should:
- Allow player 1 to input a whole number between 
1 and 50 inclusive, for player 2 to guess. 

There must be validation present to check that the 
number entered is between 1 and 50 inclusive.

-	Allow player 2 to have 5 guesses to correctly guess 
the number input by player 1. 
You do not need to validate the input for player 2.

-	Output “You guessed the correct number.” 
When player 2 inputs the same number as player 1. 
The game must end if the correct number is guessed.

-	Output “You did not guess the correct number.” 
When player 2 does not input the same number as player 1.

-	Output “Game over!” when player 2 has five incorrect guesses.
'''

'''
10.	Write your program and test that it works.
[10]
'''
# Write and test your code here

# while True:
#     P1number = int(input("player 1 please enter a number between 1 , 50 "))
#     if P1number >=1 and P1number <=50:
#         print("number accepted ")
#         break
#     else:
#         print("dummy it said 1 to 50! ")

# for i in range(5):
#     P2guess = int(input("player 2 please guess a number between 1 , 50 "))
#     if P2guess == P1number:
#         print("You guessed the correct number!")
#         break
#     else:
#         print("INCORRECT ANSWER")

# else:
#     print("Game over!")



##### END QUESTION
'''
11.	When your program is complete, test it for the following:
a.	Test 1 - Player 1 inputs the number 55
b.	Test 2 - Player 1 inputs the number 0
c.	Test 3 - Player 1 inputs the number 10 and player 2 guesses 
    the numbers 15 and 10
d.	Test 4 - Player 1 inputs the number 20 and player 2 guesses 
    the numbers 30, 35, 22, 15, 49
[4]
'''
# Test Your Code ABOVE



##### END QUESTION
'''
12.	
Extend your program to identify if player 2's 
guess is lower or higher than the number input by player 1. 
A suitable message must then be output.

Save your program.
[2]
'''
# Copy your code from above. Write and test your code here

# while True:
#     P1number = int(input("player 1 please enter a number between 1 , 50 "))
#     if P1number >=1 and P1number <=50:
#         print("number accepted ")
#         break
#     else:
#         print("dummy it said 1 to 50! ")

# for i in range(5):
#     P2guess = int(input("player 2 please guess a number between 1 , 50 "))
#     if P2guess == P1number:
#         print("You guessed the correct number!")
#         break
#     else:
#         print("INCORRECT ANSWER")
#         if P2guess>P1number:
#             print("number too big")
#         elif P2guess<P1number:
#             print("number too small")

# else:
#     print("Game over!")



##### END QUESTION
'''
13.	

Extend your program to allow player 2 to choose an 
easy, medium or hard game. 

An easy game allows eight guesses, a medium game allows 
six guesses and a hard game allows four guesses.

If player 2 inputs a correct guess, the program must output the 
number of guesses made.

You are not required to validate the input for player 2.

Save your program.
[4]
'''
# Copy your code from above. Write and test your code here


while True:
    P1number = int(input("player 1 please enter a number between 1 , 50 "))
    if P1number >=1 and P1number <=50:
        print("number accepted ")
        break
    else:
        print("dummy it said 1 to 50! ")
difficulty = input("player 2 what difficulty would you like to play? Easy Medium or Hard ")
if difficulty == "Easy":
    chances = 8
elif difficulty == "Medium":
    chances = 6
elif difficulty == "Hard":
    chances = 4
for i in range(chances):
    P2guess = int(input("player 2 please guess a number between 1 , 50 "))
    if P2guess == P1number:
        print("You guessed the correct number!")
        break
    else:
        print("INCORRECT ANSWER")
        if P2guess>P1number:
            print("number too big")
        elif P2guess<P1number:
            print("number too small")

else:
    print("Game over!")

##### END QUESTION


