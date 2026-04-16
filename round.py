def play_round(player_name, balance):
    deck = create_deck()
    bet = get_bet(balance)

    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    print("\n--- Dealing cards ---")
    print(
        f"{player_name}: {hand_to_str(player_hand)} (points: {calculate_score(player_hand)})"
    )
    print(f"Dealer: {hand_to_str(dealer_hand, hide_first=True)}")

    player_blackjack = is_blackjack(player_hand)
    dealer_blackjack = is_blackjack(dealer_hand)

    if player_blackjack or dealer_blackjack:
        print("\n--- Blackjack check ---")
        print(
            f"{player_name}: {hand_to_str(player_hand)} (points: {calculate_score(player_hand)})"
        )
        print(
            f"Dealer: {hand_to_str(dealer_hand)} (points: {calculate_score(dealer_hand)})"
        )

        if player_blackjack and dealer_blackjack:
            print("Both hands hit blackjack. It's a draw.")
            return balance
        if player_blackjack:
            win = int(bet * 1.5)
            print(f"Blackjack! {player_name} wins {win}.")
            return balance + win
        else:
            print("The dealer has blackjack. You lose...")
            return balance - bet

    # Player's move
    while True:
        action = get_action()

        if action == "1":
            new_card = deck.pop()
            player_hand.append(new_card)
            score = calculate_score(player_hand)

            print(f"\n{player_name} took the card: {card_to_str(new_card)}")
            print(f"{player_name}: {hand_to_str(player_hand)} (points: {score})")

            if score > 21:
                print("Too much! You lost...")
                return balance - bet
        else:
            break

    # Dealer's move
    print("\n--- Dealer's move ---")
    print(
        f"Dealer: {hand_to_str(dealer_hand)} (points: {calculate_score(dealer_hand)})"
    )

    while calculate_score(dealer_hand) < 17:
        new_card = deck.pop()
        dealer_hand.append(new_card)
        print(f"Dealer takes the card: {card_to_str(new_card)}")
        print(
            f"Dealer: {hand_to_str(dealer_hand)} (points: {calculate_score(dealer_hand)})"
        )

    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    print("\n--- Round summary ---")
    print(f"{player_name}: {hand_to_str(player_hand)} (points: {player_score})")
    print(f"Dealer: {hand_to_str(dealer_hand)} (points: {dealer_score})")

    if dealer_score > 21:
        print(f"The dealer is overstocked. {player_name} wins {bet}.")
        return balance + bet
    if player_score > dealer_score:
        print(f"{player_name} wins {bet}.")
        return balance + bet
    if player_score < dealer_score:
        print(f"{player_name} loses {bet}.")
        return balance - bet

    print("Draw.")
    return balance
