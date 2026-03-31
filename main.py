import random

choose = ["rock", "paper", "scissor"]
short = {"r": "rock", "p": "paper", "s": "scissor"}

counter_comp = 0
counter_user = 0

print("=== Rock Paper Scissors ===")
print("Enter r (rock), p (paper), s (scissor), or n to quit\n")

while True:
    comp = random.choice(choose)
    user = input("Enter your choice: ").lower()

    if user == "n":
        print(f"\nGame Over! Final Score → You: {counter_user} | Computer: {counter_comp}")
        break

    elif user not in short:
        print("Invalid input. Please enter r, p, or s\n")

    else:
        user_ch = short[user]

        if user_ch == comp:
            print(f"Draw! You both chose {user_ch}\n")

        elif (
            (comp == "rock" and user_ch == "scissor")
            or (comp == "paper" and user_ch == "rock")
            or (comp == "scissor" and user_ch == "paper")
        ):
            counter_comp += 1
            print(f"You lose! Computer: {comp} | You: {user_ch}")
            print(f"Score → You: {counter_user} | Computer: {counter_comp}\n")

        else:
            counter_user += 1
            print(f"You win! Computer: {comp} | You: {user_ch}")
            print(f"Score → You: {counter_user} | Computer: {counter_comp}\n")
