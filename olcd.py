# # WORD UNSCRAMBLE CODE
# import random
# words = ["ramen" , "carbonara" , "steak" , "sushi" , "dumpling" , "nugget" , "wagyu_beef" , "cookies & cream icecream" , "chicken katsu don"
# ]
# # choose a word randomly

# word = random.choice(words)

# #split this into characters in a list
# character_list = list(word)

# # shuffle the items in a list
# random.shuffle(character_list)

# # put the list back into a string
# scrambled = ''
# for c in character_list:
#     scrambled = scrambled + c + ''

# # while true
# while True:
# #    #display the word
#     print("###########################################")
#     print("can you guess this word?")
#     print(scrambled)

#     # options Type 1 to scramble again, 2 to guess, 3 to give up:
#     uoption = input("type 1 to scramble again , type 2 to guess , type 3 to give up ")

#     # if option 1
#     if uoption == '1':
#         random.shuffle(character_list)
#         scrambled = ''
#         for c in character_list:
#           scrambled = scrambled + c + ''

    
#     # elif option 2
#     elif uoption == '2':
#         uguess = input("So, what is the word??? ")
#         if uguess == word:
#             print("CORRECT GUESS")
#             break
#         else:
#             print("NAH WRONG, WOMP WOMP")
    
#     # elif option 3
#     elif uoption == '3':
#        print("LOL U SUCK, OK HERES THE ANSWER")
#        print(word)
#        break

#     # # else invalid
#     else:
#         print("dummy it says 1 , 2 , 3")



'''
2018 - Task 3 [10]
The following program should identify if a student receives either 
a gold, silver or bronze award for joint achievement in Computing 
and Mathematics. 
Each student has taken a test in Computing and a test in Mathematics. 

The program uses the rules:
- A student receives a gold award for a test score of 
100 or greater in both Computing and Mathematics.

- A student receives a silver award for a test score 
of 100 or greater in Computing or Mathematics. 

They also need a combined Computing and Mathematics
score of 180 or greater.

- A student receives a bronze award for a test score 
of 75 or greater in both Computing and Mathematics.

The test scores are whole numbers only. 
The program finishes when there are no more 
student test scores to be input. 

The award a student receives is output after the 
test scores for that student are input.z

There are several syntax and logic errors in the program.

9. Identify and correct the errors in the program so 
that it works according to the rules given. 
Save your program.
[10]

'''

students = True                                               #changed to true
while students == True:                                       #changed students==True
    comp = int(input("Enter the Computing test score "))       #change into integer
    math = int(input("Enter the Mathematics test score " ))     #missing quotation mark
    joint_score = math + comp                                  #math + comp is not comp + comp
    if comp >= 100 and math >= 100:                            #>= 100 changed to >
        print("Student is awarded a gold award")            
    elif (comp >= 100 and math >= 100) or joint_score >= 180:  #fixed or conditions
        print("Student is awarded a silver award")
    elif comp >= 75 and math >= 75:
        print("Student is awarded a brone award")
    else:
        print("NO award this time, keep trying")
    more_scores = input("Any more test scores to enter? Type 'Y' or 'N' ")
    if more_scores == 'N':                                    #capital M change to lower case
        students = False                                      #change to false
    else:                                                     #changed elke to else
        students = True                                    



#this is a backup
# students = False
# while students == True:
#     comp = input("Enter the Computing test score ")
#     math = int(input("Enter the Mathematics test score ))
#     joint_score = comp + comp
#     if comp > 100 and math > 100:
#         print("Student is awarded a gold award")
#     elif comp >= 100 and math >= 100 or joint_score >= 180:
#         print("Student is awarded a silver award")
#     elif comp >= 75 and math >= 75:
#         print("Student is awarded a bronze award")
#     else:
#         print("NO award this time, keep trying")
#     more_scores = input("Any more test scores to enter? Type 'Y' or 'N' ")
#     if More_scores == 'N':
#         students = True
#     ekse:
#         students = True
