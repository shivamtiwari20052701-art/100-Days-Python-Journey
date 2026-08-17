import random
import art
import game_data

score = 0
continue_game = True

print(art.higher_lower)

# Return a random account different from Account A
def get_unique_account(account_to_avoid):
     account = random.choice(game_data.data)
     while account == account_to_avoid:
          account = random.choice(game_data.data)
     return account

Account_A = random.choice(game_data.data)
Account_B = get_unique_account(Account_A)

# Main game loop
while continue_game:
    print(f"Account A: {Account_A['name']},{Account_A['description']},{Account_A['country']}")
    print(art.vs)
    print(f"Account B: {Account_B['name']},{Account_B['description']},{Account_B['country']}")

    # Get user's choice
    user_choice = input("enter 'A' to choose account A and 'B' for B \n").strip().upper()

    # Decide which account has more followers
    if Account_A['follower_count'] > Account_B['follower_count']:
        winner = "A"
    else:
        winner = "B"

    # Check the answer and update the game
    if user_choice == winner:
        score += 1
        print("\n" * 20)
        print("Correct!!")
        print(f"your Score is : {score}")

        # Move to the next round
        Account_A = Account_B
        Account_B = get_unique_account(Account_A)

    else:
        print("Game Over!!")
        print(f"Final Score is: {score}")
        continue_game = False