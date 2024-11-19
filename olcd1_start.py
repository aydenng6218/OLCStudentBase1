# random
# print("my name is ayden")
# print("my hobby is reading")
# y= 10
# x= 20
# z = x + y
# print(z)
# hobby = 'play soccer'
# print("i like to", hobby)
# name = "steven"
# title = "king"
# print("my name is", name)
# print("i am a", title)
# print("you shall now know me as", title , name )
# number = 3800
# number2 = 2325
# answer = number + number2
# print(answer)



#ask_questions
# name = input("who are you")
# command = input("why are you here")
# print(name, "is here to" , command)


#simple_addition
# num1 = (int)(input("what is the first number?"))
# num2 = (int)(input("what is the second number?"))
# answer = num1 + num2 

#for_loops
# for i in range(3):
#     print("hello")
#     print("bye")

# for i in range(3):
#     for i in range(3):
#       print("hello")
#     for i in range(3):
#       print("bye")

#loop all values of a string
#cheer program
# name = input("who to cheer?")
# for i in name:                   #i refers to each continious letter
#     print("give me a" ,  i)
#     print(i , "!")

# print("who is the best?")
# print(name , "!!!!!!!!!")

#how to count numbers
# for i in range(10):
#     print(i)

#how to use range start,stop
# for i in range(67 , 97):
#     print(i)


#print start, stop ,step (only increase by-)
# for i in range(6 , 72 , 6):
#     print(i)

#countdown
# for i in range(15 , 0 , -1):        #note when countdown must be -1
#     print(i)

#calculate how much money
# name = input("what is your name? ")
# allowance = int(input("how much do you get a week? "))
# print("in one year" , name , "will have" , allowance * 52)
# print("from primary one to secondary 4" , name , "will have gotten" , allowance * 520)

#calculate how long is a name
# fname = input("what is your first name? ")
# lname = input("what is your last name? ")
# #calculate how long is name len()
# total = len(fname) + len(lname)
# print("the total length of the name" , fname , lname , "is" , total)

#random number generator (might repeat)
# import random 
# for i in range(7):
#     num = random.randint(1, 47)
#     print(num)

# #list  (wont repeat)
# rannums = []

# while len(rannums) < 6:
#     num = random.randint(1,47)
#     if num not in rannums:
#         rannums.append(num)

# print(rannums)


#times table program

number = int(input("what is the number?"))
for  i in range(1,13):
    print(number , "x" , i , "=" , number*i)
