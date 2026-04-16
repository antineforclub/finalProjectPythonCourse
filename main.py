def main():
    print("=== BLACKJACK ===")
    player_name = get_player_name()
    balance = get_deposit()

    while balance > 0:
        print("\n==============================")
        balance = play_round(player_name, balance)
        print(f"\nPlayer's balance {player_name}: {balance}")

        if balance <= 0:
            print("You don't have enough money. Game is over...")
            break

        if not ask_continue():
            break

    print(f"\nThank you for your game, {player_name}. Final balance: {balance}")


if __name__ == "__main__":
    main()
