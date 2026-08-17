'''Black jack game'''
import random
from art import logo    

def deal_card():
    '''Returns a random card from the deck '''
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def calculate_score(cards):
    '''take a list of cards and returns the score calculated from the cards '''

    # if 11 in cards and 10 in cards and len(cards)==2:
    if sum(cards)==21 and len(cards)==2:
        '''this is the logic of two cards in  hand (ace + 10)==21'''
        return 0 #user or computer the blakjack =21 
    
    if sum(cards) > 21 and 11 in cards:
        '''here we have to remove the 11 and 1 '''
        #use remove() to dlt 11 and append() to add 1
        cards.remove(11)
        cards.append(1)

    return sum(cards) 
def compare(u_score,c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score==0:
        return "Lose, Computer has the blackjack"
    elif u_score==0:
        return "Won you have a blackjack "
    elif u_score > 21:
        return "You went over!! \n You lose"
    elif c_score > 21:
        return "OPonent went over!! \n You win!!"
    elif u_score > c_score:
        return "You win "
    else:
        return "YOu lose"
def play_game():
    print(logo)
    user_cards=[]
    computer_cards=[]

    computer_score=-1
    user_score=-1
    is_game_over= False

    for _ in range(2):
     user_cards.append(deal_card())
     computer_cards.append(deal_card())

    '''here we call the function by passing the parameter'''
    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"user cards : {user_cards}, user score:{user_score}")
        print(f"computers first cards : {computer_cards[0]}")

        if user_score==0 or computer_score==0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal=input("Type 'y' to add another card and 'n' to Pass:")
            if user_should_deal=="y":
                user_cards.append(deal_card())
            else:
                is_game_over=True

        '''its time to let computer draw the card utill the sum is less than 17'''

        while computer_score!=0 and computer_score<17:
            computer_cards.append(deal_card())
            computer_score=calculate_score(computer_cards)

        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        print(compare(user_score, computer_score))


while input("Do you want to play a game of blackjack ? type 'y'or 'n'") == 'y':
    print("\n"*20)
    play_game()

 

    
    








