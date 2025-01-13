import random
import os

black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
zero = [0, 00]

bet_valid_type = ["red", "black", "odd", "even", "1-18", "19-36", "1st 12", "2nd 12", "3rd 12", "0", "00"]

money = 100

def print_roulette():
     print("""
     +-------------------+-------------------+-------------------+
     |      1nd 12       |      2nd 12       |      3rd 12       |    
+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
|  0 |  3 |  6 |  9 | 12 | 15 | 18 | 21 | 24 | 27 | 30 | 33 | 36 |2:1 |
|    +----+----+----+----+----+----+----+----+----+----+----+----+----+
+----|  2 |  5 |  8 | 11 | 14 | 17 | 20 | 23 | 26 | 29 | 32 | 35 |2:1 |
|    +----+----+----+----+----+----+----+----+----+----+----+----+----+
| 00 |  1 |  4 |  7 | 10 | 13 | 16 | 19 | 22 | 25 | 28 | 31 | 34 |2:1 |
+----+---------+---------+---------+---------+---------+---------+----+   
     |   1-18  |  EVEN   |   RED   |  BLACK  |   ODD   |  19-36  |
     +---------+---------+---------+---------+---------+---------+     
""")

def print_money():
    print("You have", money, "money.")

def play(entered_bet, entered_bet_type, money):
     number = random.choice(black + red + zero)

     if number in black:
          color = "black"

     elif number in red:
          color = "red"

     else:
          color = "green"

     if color != "green":
          if number % 2 == 0:
               odd_even = "even"
          else:
               odd_even = "odd"
          
          if number in range(1, 19):
               radius = "1-18"
          else:
               radius = "19-36"
          
          if number in range(1, 13):
               twelve = "1st 12"
          elif number in range(13, 25):
               twelve = "2nd 12"
          else:
               twelve = "3rd 12"
     
     else:
          odd_even = False
          radius = False
          twelve = False


     if entered_bet_type == "red" or entered_bet_type == "black":
          if entered_bet_type == color:
               print("You won.")
               entered_bet = entered_bet * 2
               money += entered_bet
               return money
          else:
               print("You lost.")
               money -= entered_bet
               return money

     elif entered_bet_type == "odd" or entered_bet_type == "even":
          if entered_bet_type == odd_even:
               print("You won.")
               entered_bet = entered_bet * 2
               money += entered_bet 
               return money
          else:
               print("You lost.")
               money -= entered_bet
               return money

     elif entered_bet_type == "1-18" or entered_bet_type == "19-36":
          if entered_bet_type == radius:
               print("You won.")
               entered_bet = entered_bet * 2
               money += entered_bet 
               return money
          else:
               print("You lost.")
               money -= entered_bet
               return money   

     elif entered_bet_type == "1st 12" or entered_bet_type == "2nd 12" or entered_bet_type == "3rd 12":
          if entered_bet_type == twelve:
               print("You won.")
               entered_bet = entered_bet * 3
               money += entered_bet 
               return money
          else:
               print("You lost.")
               money -= entered_bet
               return money
     
     elif entered_bet_type == "0" or entered_bet_type == "00":
          if entered_bet_type == number:
               print("You won.")
               entered_bet = entered_bet * 36
               money += entered_bet 
               return money
          else:
               print("You lost.")
               money -= entered_bet
               return money

     elif entered_bet_type.isdigit() and entered_bet in range(1, 37):
          if entered_bet_type.isdigit() and int(entered_bet_type) == number:
               print("You won.")
               entered_bet = entered_bet * 36
               money += entered_bet 
               return money
          else:
               print("You lost.")
               money -= entered_bet
               return money
     
     else:
          print("Invalid bet type.")
     
def place_bet():
     bet = int(input("Enter your bet: "))

     if bet > money:
          print("You don't have enough money.")
          place_bet()

     print("Bet types: ")
     print("""
1. red("red"), black("black")
2. odd("odd"), even("even")
3. 1-18("1-18"), 19-36("19-36")
4. 1st 12("1st 12"), 2nd 12("2nd 12"), 3rd 12("3rd 12")
5. number("5")
6. zero("0")
""")
     bet_type = str(input("Enter your bet type: "))

     if bet_type not in bet_valid_type:
         print("Invalid bet type.")
         bet()
     
     return bet, bet_type


while money > 0:
     print_roulette()
     print_money()
     bet, bet_type = place_bet()
     money = play(bet, bet_type, money)
     input("Press enter to play again.")
     os.system("cls")
