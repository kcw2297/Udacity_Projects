import time
import random


def game():
    intro()
    global total_dist, move_dist, turn_head
    total_dist = 5
    move_dist = 1
    die = 0
    turn_head = ["hide", "see"]
    game_start()
    game_process()
    restart_game()


def player_choice():
    global player
    choice = input("enter move or stop for this turn : ").lower()
    while True:
        if "move" in choice:
            player = "moving"
            break
        elif "stop" in choice:
            player = "wait"
            break
        else:
            print("You did not enter move or stop")
            choice = input("enter move or stop for this turn : ").lower()


def intro():
    # This is intro function.
    print("Welcome to 'Green Light Red Light Game'")
    time.sleep(2)
    print("You will have to bet on moving or stop every beep")
    time.sleep(2)
    print("If you made it to the end, you win")
    while True:
        intro = input("Enter udacity to start : ").lower()
        print(intro)
        time.sleep(2)
        if intro == "udacity":
            break
        print("you did not type udacity")
    print("Great i hope you survive and get award")
    time.sleep(2)


def game_start():
    # This is game_start function.
    print("beep! game start")
    time.sleep(2)
    player_choice()
    time.sleep(2)
    print(f"You choose {player}")
    time.sleep(2)


def game_process():
    global total_dist, move_dist, turn_head
    while total_dist > 0:
        head = random.choice(turn_head)
        if head == "hide" and player == "moving":
            print("you move one step")
            time.sleep(2)
            total_dist -= move_dist
            if total_dist <= 0:
                print("You made it to the end, Congratulation!")
            else:
                print(f'{total_dist} left to go')
                player_choice()
        elif head == "see" and player == "moving":
            print("booom")
            time.sleep(2)
            print("you die")
            time.sleep(2)
            break
        else:
            print("Big toy doesn't do anything")
            time.sleep(2)
            print("nothing happen this turn")
            time.sleep(2)
            player_choice()


def restart_game():
    # This is restart game function.
    print("Do you want to restart?")
    time.sleep(1)
    restart = input("Enter continue to restart : ").lower()
    print(restart)
    if "continue" in restart:
        print("Start new game")
        time.sleep(2)
        total_dist = 5
        move_dist = 0
        game()
    else:
        exit()


if __name__ == '__main__':
    game()
