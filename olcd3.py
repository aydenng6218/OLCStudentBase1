# # number checker (finished)
# # while True:
# #     number = input("what is your phone number?")
# #     if number.startswith("8") or number.startswith("9"):
# #         print("number accepted")
# #         break
# #     else:
# #         print("not accepted try again")

# # email checker (unfinished)
# # while True:
# #     email = 


# # #lists
# planets = [ "mercury" , "venus", "earth" , "mars" , "jupiter" ,  "saturn" , "uranus" , "neptune"]
# # # planets[4] = "123456789" #square bracketto extract from list
# # print(planets[4])

# #how add NEW value to list .append
# # planets.append("pluto")
# # # print(planets)

# #add new value in ANY position
# # planets.insert(0 , "lalaland")
# # print(planets)

# # #REMOVE items from list
# # del( planets[0])      #specific place
# # print(planets)

# # planets.remove("venus")      #specific value in list
# # print(planets)

# # planets.pop()
# # print(planets)                #always remove last one


# #to check length of list
# # num = len(planets)
# # print("there are" , num , "planets in the solar system")

# #loop through each item in the list
# # for p in planets:
# #     print("someday i will visit", p)

# for i in range(len(planets)):            #everything add smt
#     print(planets[i])
#     planets[i] = "new " + planets[i]
#     print (planets)



#actual question

'''
2020 - Task 2 [10]
The following program checks it the personal identification number (PIN) 
entered for a locker is correct. There are 10 lockers available and the 
correct PIN for each locker is stored in an array.
A PIN cannot start with the digit 0.

The program allows the user to enter the number of the locker they 
want to open, and a PIN. It checks if the PIN is correct for that locker.
'''
# arraypins = [1234, 1654, 1936, 3957, 2058, 7689, 2749, 2265, 1010, 9966]
# locker = int(input("Please enter the locker you would like to open: "))
# pin = float(input("PLease enter the PIN for the locker: "))
# if pin == arraypins[locker-1]:
#     print("The locker is open.")
# else: 
#     print("Incorrect PIN for that locker")

'''
1.	Edit the program so that it converts the PIN input 
by the user to an integer.
Save your program
[1] 
'''
# Write and test your code here
# arraypins = [1234, 1654, 1936, 3957, 2058, 7689, 2749, 2265, 1010, 9966]
# locker = int(input("Please enter the locker you would like to open: "))
# pin = int(input("PLease enter the PIN for the locker: "))
# if pin == arraypins[locker-1]:
#     print("The locker is open.")
# else: 
#     print("Incorrect PIN for that locker")


'''
2.	Edit the program to only accept a locker number between 1 and 10 
(inclusive) to be input. A suitable error message must be displayed 
if the locker number input is not in this range. The program must 
loop until a valid locker number is input.
Save your program.
[3]
'''
# Write and test your code here
# arraypins = [1234, 1654, 1936, 3957, 2058, 7689, 2749, 2265, 1010, 9966]

# while True:
#     locker = int(input("Please enter the locker you would like to open: "))
#     if locker <=10 and locker >=1:
#         print ("Locker accepted")
#     else:
#         print("Invalid locker number. Must be between 1 and 10")

#     pin = int(input("PLease enter the PIN for the locker: "))


# if pin == arraypins[locker-1]:
#     print("The locker is open.")
# else: 
#     print("Incorrect PIN for that locker")



'''
3.	Edit the program to only accept a PIN of 4 digits to be 
entered by the user. A suitable error message must be displayed 
if an incorrect input is given. The program must loop until the PIN 
input is 4 digits.
Save your program
[3]
'''
# Write and test your code here

# arraypins = [1234, 1654, 1936, 3957, 2058, 7689, 2749, 2265, 1010, 9966]
# while True:
#     while True:
#         locker = int(input("Please enter the locker you would like to open: "))
#         if locker <=10 and locker >=1:
#             print ("Locker accepted")
#             break
#         else:
#             print("Invalid locker number. Must be between 1 and 10")

#     while True:
#         pin = int(input("PLease enter the PIN for the locker: "))
#         if len(str(pin)) == 4:
#             print("valid number of digits")
#             break
#         else:
#             print("must be 4 digits")


#     if pin == arraypins[locker-1]:
#         print("The locker is open.")
#         break
#     else:
#         print("Incorrect PIN for that locker")
        


'''
4.	Edit the program to loop until the user inputs both a 
correct locker number and the matching PIN for that locker.
Save your program.
[3]
'''
# Write and test your code here




#how to define dictionary 
# fruit_price =  {"apple":"$3",
#                 "orange":"$4",
#                 "watermelon":"$5"}

#my shop
shop_prices = {'steak':15.99,'cabonara':10.99,'ramen':12.99,'lasagne':13.49,'egg fried rice':19.49,'xiao long bao':10.99}

#how to retrieve the value of your item
# print(shop_prices["ramen"])

# #change value of item
# shop_prices['ramen']=15.99
# print(shop_prices) 

# #add a new item
# shop_prices['cookies & cream icecream']=6.49
# print(shop_prices)

# #delete a value from dictionary
# del(shop_prices['cabonara'])
# print(shop_prices)

# #loop through everything in dictionary
# for item in shop_prices:
#     print(item)

#check if something exists in dictionary
# food = input("what food are u looking for bud?")
# if food in shop_prices:
#     print("yes we sell" , food , ",please pay $" , shop_prices[food])
# else:
#     print("no we do not sell that")



#challenge
wallet = 100
while True:
    food = input("what would you like to buy sir?")
    if wallet<=0:
        print("your broke")
        break
    elif food in shop_prices:
        print("yes we sell" , food , ",please pay $" , shop_prices[food])
        wallet = wallet - shop_prices[food]
        print(wallet)
    else:
        print("no we do not sell that")




























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































