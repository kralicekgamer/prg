import random
import os

black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
zero = [0, 00]

bet_valid_type = ["red", "black", "odd", "even", "1-18", "19-36", "1st 12", "2nd 12", "3rd 12", "0", "00"]

money = 100

r = "\033[41m"
b = "\033[40m"
g = "\033[42m"
a = "\033[0m"



def print_roulette():
     print(f"""
     +-------------------+-------------------+-------------------+
     |      1st 12       |      2nd 12       |      3rd 12       |    
+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
|{g}  0 {a}|{r}  3 {a}|{b}  6 {a}|{r}  9 {a}|{b} 12 {a}|{r} 15 {a}|{b} 18 {a}|{r} 21 {a}|{b} 24 {a}|{r} 27 {a}|{b} 30 {a}|{r} 33 {a}|{b} 36 {a}|2:1 |
|{g}    {a}+----+----+----+----+----+----+----+----+----+----+----+----+----+
+----|{b}  2 {a}|{r}  5 {a}|{b}  8 {a}|{r} 11 {a}|{b} 14 {a}|{r} 17 {a}|{b} 20 {a}|{r} 23 {a}|{b} 26 {a}|{r} 29 {a}|{b} 32 {a}|{r} 35 {a}|2:1 |
|{g}    {a}+----+----+----+----+----+----+----+----+----+----+----+----+----+
|{g} 00 {a}|{r}  1 {a}|{b}  4 {a}|{r}  7 {a}|{b} 10 {a}|{r} 13 {a}|{b} 16 {a}|{r} 19 {a}|{b} 22 {a}|{r} 25 {a}|{b} 28 {a}|{r} 31 {a}|{b} 34 {a}|2:1 |
+----+---------+---------+---------+---------+---------+---------+----+   
     |   1-18  |  EVEN   |{r}   RED   {a}|{b}  BLACK  {a}|   ODD   |  19-36  |
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
