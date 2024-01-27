#HINT: You can call clear() to clear the output in the console.

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
run_again= True
bidders = {}

def find_winner(bidders):
  winner = ""
  highest_bid=0
  for key in bidders:
    value = bidders[key]
    if value>highest_bid:
      highest_bid = value
      winner = key
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while run_again:
  name = input("What is your name?\n")
  bid = int(input("What is your bid?\n$"))
  bidders[name] = bid
  if input("Are there any other bidders? Type 'yes' or 'no'.\n") == "yes":
    print("Next Entry")
  else:
    run_again = False
    find_winner(bidders)