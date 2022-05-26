from config import GAME_CHOICES, RULES, scoreboard
import random


def get_user_choice():
    user_input = input("your choice(p, r, s): ")
    if user_input not in GAME_CHOICES:
        print("Oops! this wrong, try again")
        return get_user_choice()

    return user_input


def get_system_choice():
    system_choice = random.choice(GAME_CHOICES)
    return system_choice


def find_winner(user_choice, system_choice):
    match = {user_choice, system_choice}

    if len(match) == 1:
        return None

    return RULES[tuple(sorted(match))]


def update_scoreboard(result):
    if result["user"] == 3:
        scoreboard["user"] += 1
        msg = "YOU WIN"
    else:
        scoreboard["system"] += 1
        msg = "YOU LOSE"

    print("#" * 30)
    print("##", f"user: {scoreboard['user']}".ljust(24), "##")
    print("##", f"system: {scoreboard['system']}".ljust(24), "##")
    print("##", f"last game: {msg}".ljust(24), "##")
    print("#" * 30)


def play():
    result = {"user": 0, "system": 0}
    while result["user"] < 3 and result["system"] < 3:
        user_choice = get_user_choice()
        system_choice = get_system_choice()
        winner = find_winner(user_choice, system_choice)

        if winner == user_choice:
            msg = "You win"
            result["user"] += 1

        elif winner == system_choice:
            msg = "You lose"
            result["system"] += 1
        else:
            msg = "draw"

        print(f"You: {user_choice}, system: {system_choice}, result: {msg}")

    update_scoreboard(result)
    again = input("do you want play again?(y/n): ")
    if again == "y":
        return play()


if __name__ == "__main__":
    play()
