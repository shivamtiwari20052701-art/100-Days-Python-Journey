from art import logo

print(logo)

#dictionary
name_and_bid={}

def find_max_bidder(name_and_bid):
    winner=""
    max_bid=0
    for bid in name_and_bid:
        bid_amount=name_and_bid[bid]
    if bid_amount > max_bid:
        max_bid=bid_amount
        winner=bid
    print(f"winner is :{winner}")


continue_bidding=True
while continue_bidding==True:
    name=input("enter the name of user:")
    bid=int(input("enter your bid $:"))

    #store the name and bid

    name_and_bid[name] = bid

    #ask for other bid
    next_entry=input("Are there any other bidders ? Type 'yes' or 'no' \n")

    if  next_entry=="yes":
     print("\n"*20)
    else:
       continue_bidding=False
       find_max_bidder(name_and_bid)
    

   





          
       


    
