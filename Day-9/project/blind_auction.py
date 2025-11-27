from art import logo
print(logo)

def find_highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for bid in bids:
        if bids[bid] > highest_bid:
            highest_bid = bids[bid]
            winner = bid
    print(f"The winner is {winner} with a bid of ${highest_bid}")


bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bids[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes or no'.\n")
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    else:
        print("\n" * 100)

