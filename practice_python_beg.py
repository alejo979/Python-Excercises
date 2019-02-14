# https://www.practicepython.org/
#
# 1
# import datetime
# name = input("Please enter your name: ")
# age = int(input("Please enter your age: "))
# number = int(input("Please enter a random number: "))
# year = datetime.datetime.now().year
# calc = (100-age) + year
# for i in range(number):
#     print("Hi {}, you will be 100 years old in the year {}".format(name, calc))


# 2 even or odd
# number = int(input("Please enter a number: "))
# if number % 4 == 0:
#     print("{} is an even number and multiple of 4.".format(number))
# elif number % 2 == 0:
#     print("{} is an even number.".format(number))
# else:
#     print("{} is an odd number.".format(number))

# 3
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = []
# for n in a:
#     if 5 > n:
#         #print(n)
#         b.append(n)
# print(b)
#
# print([n for n in a if 5 > n])

# 4
# num = int(input("Please enter a number, and I will tell you all it's divisors: "))
# for i in range(1, num+1):
#     if num % i == 0:
#         print(i)

# 5 intersections
# import random
# a = random.sample(range(1, 20), 8)  #
# #a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# a.sort()
# print(a)
# b = random.sample(range(1, 20), 5)
# #b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# b.sort()
# print(b)
# print("Sets Intersection", sorted(set(a).intersection(set(b))))
# d = [i for i in a if i in b]
# # d = [x for x in a if x in b and not in d]
# print("Comprehension: ", d)
# print("one line", sorted(set(a) & set(b)))
#
# c = []
# for i in b:
#     if i in c:
#         continue
#     elif i in a:
#         c.append(i)
# print("For Loop and Append", c)

# 6 palindrome
# word = input("Please enter a word: ")
# w_up = word.upper()
# reverse = w_up[::-1]
# if w_up == reverse:
#     print("It's a palindrome")
# else:
#     print("It's not a palindrome")

# 7  evens from list
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# print([i for i in a if i % 2 == 0])

# 8  Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
# compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
#
# Remember the rules:
#
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

# MY SOLUTION:
# print("Welcome to scissors, paper, rock game!!")
# while True:
#     play = input("New game? (yes, no): ")
#
#     if play == 'yes':
#         try:
#             p1 = int(input("Player 1, please enter your choice (1: Scissors, 2: Paper, 3: Rock): "))
#             p2 = int(input("Player 2, please enter your choice (1: Scissors, 2: Paper, 3: Rock): "))
#
#
#             if (p1 and p2) not in (1, 2, 3):
#                 print("Please choose just 1, 2 or 3")
#                 continue
#             if p1 == p2:
#                 print("You tie")
#                 continue
#             else:
#                 if p1 == 1 and p2 == 2:
#                     print("Scissors beat paper, Player 1 wins!")
#                 elif p1 == 1 and p2 == 3:
#                     print("Rock beats scissors, Player 2 wins!")
#                 elif p1 == 2 and p2 == 1:
#                     print("Scissors beat paper, Player 2 wins!")
#                 elif p1 == 2 and p2 == 3:
#                     print("Paper beats rock, Player 1 wins!")
#                 elif p1 == 3 and p2 == 1:
#                     print("Rock beats scissors, Player 1 wins!")
#                 elif p1 == 3 and p2 == 2:
#                     print("Paper beats rock, Player 2 wins!")
#         except ValueError:
#             print("Please don't type in text, just numbers")
#     else:
#         break
#
# print("Thanks for playing")

# ALTERNATIVE 1
# print('''Please pick one:
#             rock
#             scissors
#             paper''')
#
# while True:
#     game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
#     player_a = str(input("Player a: "))
#     player_b = str(input("Player b: "))
#     a = game_dict.get(player_a)
#     b = game_dict.get(player_b)
#     dif = a - b
#
#     if dif in [-1, 2]:
#         print('player a wins.')
#         if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
#             continue
#         else:
#             print('game over.')
#             break
#     elif dif in [-2, 1]:
#         print('player b wins.')
#         if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
#             continue
#         else:
#             print('game over.')
#             break
#     else:
#         print('Draw.Please continue.')
#         print('')

# ALTERNATIVE 2
# print("Welcome to scissors, paper, rock game!!")
#
# options = ['paper', 'rock', 'scissors']
#
# while True:
#     play = input("New game? (yes, no): ")
#
#     if play == 'yes':
#
#         p1 = input("Player 1, please enter your choice (1: Paper, 2: Rock, 3: Scissors): ").lower()
#         p2 = input("Player 2, please enter your choice (1: Paper, 2: Rock, 3: Scissors): ").lower()
#
#         if (p1 and p2) not in options:
#             print("Please type in correctly: paper - rock - scissors")
#             continue
#
#         if p1 == p2:
#             print("You tie")
#             continue
#         elif options.index(p1) == (options.index(p2) + 1) % 3:
#             print(options.index(p1))
#             print((options.index(p2) + 1) % 3)
#             print(2 % 3)
#
#             print("Player 2 Wins!")
#         elif options.index(p2) == (options.index(p1) + 1) % 3:
#             print((options.index(p1) + 1) % 3)
#             print(options.index(p2))
#
#             print("Player 1 Wins!")
#
#     else:
#         break
#
# print("Thanks for playing")
