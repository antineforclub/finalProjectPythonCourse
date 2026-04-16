import round
import input


def main():
    print("=== BLACKJACK ===")
    player_name = input.get_player_name()
    balance = input.get_deposit()

    while balance > 0:
        print("\n==============================")
        balance = round.play_round(player_name, balance)
        print(f"\n{player_name}'s balance: {balance}")

        if balance <= 0:
            print("You don't have enough money. Game over.")
            break

        if not input.ask_continue():
            break

    print(f"\nThank you for playing, {player_name}. Final balance: {balance}")


if __name__ == "__main__":
    main()
