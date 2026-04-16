def get_player_name():
    while True:
        name = input("Enter player name: ").strip()
        if name:
            return name
        print("Player name cannot be empty.")


def get_deposit():
    while True:
        raw = input("Enter starting deposit: ").strip()
        try:
            deposit = int(raw)
            if deposit > 0:
                return deposit
            print("Deposit must be greater than 0.")
        except ValueError:
            print("Please enter an integer.")


def get_bet(balance):
    while True:
        raw = input(f"Your balance: {balance}. Enter your bet: ").strip()
        try:
            bet = int(raw)
            if bet <= 0:
                print("Bet must be greater than 0.")
            elif bet > balance:
                print("Insufficient funds for this bet.")
            else:
                return bet
        except ValueError:
            print("Please enter an integer.")


def get_action():
    while True:
        action = input("Choose an action: [1] Hit  [2] Stand: ").strip()
        if action in ("1", "2"):
            return action
        print("Please enter 1 or 2.")


def ask_continue():
    while True:
        answer = input("Play another round? [y/n]: ").strip().lower()
        if answer in ("y", "n"):
            return answer == "y"
        print("Please enter y or n.")
