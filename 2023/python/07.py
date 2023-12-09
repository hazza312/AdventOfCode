from collections import Counter
import sys

COUNT_RANKING = [  # in ascending score order
    (1, 1, 1, 1, 1),  # five of a kind
    (1, 1, 1, 2),  # four of a kind
    (1, 2, 2),  # full house
    (1, 1, 3),  # three of a kind
    (2, 3),  # two pair
    (1, 4),  # one pair
    (5,)  # high card
]


def sort_key(real_hand, hand_counts, card_order):
    card_scores = map(card_order.index, real_hand)
    return COUNT_RANKING.index(hand_counts), *card_scores


def compare_part_1(hand):
    hand_counts = tuple(sorted(Counter(hand).values()))
    return sort_key(hand, hand_counts, '23456789TJQKA')


def compare_part_2(hand):
    hand_no_jokers = [c for c in hand if c != 'J']
    better_hand_counts = sorted(Counter(hand_no_jokers).values() or [0])
    better_hand_counts[-1] += hand.count('J')
    return sort_key(hand, tuple(better_hand_counts), 'J23456789TQKA')


def read_input():
    hands_bids = []
    for line in sys.stdin:
        hand, bid = line.split()
        hands_bids.append((hand, int(bid)))

    return hands_bids


def total_winnings(hands_bids, compare):
    in_order = sorted(hands_bids, key=lambda hb: compare(hb[0]))
    return sum(i * b for i, (_, b) in enumerate(in_order, start=1))


if __name__ == '__main__':
    hands_bids = read_input()
    print(total_winnings(hands_bids, compare_part_1))
    print(total_winnings(hands_bids, compare_part_2))
