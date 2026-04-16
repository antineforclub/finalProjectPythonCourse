import random

SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
VALUES = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11,
}


def create_deck():
    deck = [(rank, suit) for suit in SUITS for rank in RANKS]
    random.shuffle(deck)
    return deck


def card_to_str(card):
    rank, suit = card
    return f"{rank}{suit}"


def hand_to_str(hand, hide_first=False):
    if hide_first and hand:
        return "[??] " + " ".join(card_to_str(card) for card in hand[1:])
    return " ".join(card_to_str(card) for card in hand)


def calculate_score(hand):
    score = sum(VALUES[rank] for rank, _ in hand)
    aces = sum(1 for rank, _ in hand if rank == "A")

    while score > 21 and aces > 0:
        score -= 10
        aces -= 1

    return score


def is_blackjack(hand):
    return len(hand) == 2 and calculate_score(hand) == 21
