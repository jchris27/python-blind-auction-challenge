from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
auction_start = True
bid = {}
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = 0
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while auction_start:

  bidders_name = input("What is your name?: ")
  bid_price = int(input("What is your asking bid?: $"))
  bid[bidders_name] = bid_price
  choice = input("Are there any other bidders? Yes or No? \n").lower()
  
  if choice == "no":
    find_highest_bidder(bid)
    auction_start = False
  elif auction_start == "yes":
    clear()
