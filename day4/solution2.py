import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('input')
args = parser.parse_args()

def pretty_print(obj):
    print(json.dumps(obj, indent=2))

game_num_to_num_copies = {}

with open(args.input) as f:
    for line in f:
        line = line.replace('\n', '')
        label_and_numbers = line.split(':')
        label = label_and_numbers[0]
        game_num = int(label.split()[1])
        game_num_to_num_copies[game_num] = 1

with open(args.input) as f:
    for line in f:
        line = line.replace('\n', '')
        label_and_numbers = line.split(':')
        label = label_and_numbers[0]
        game_num = int(label.split()[1])
        num_copies_curr_card = game_num_to_num_copies[game_num]
        numbers = label_and_numbers[1]
        winning_and_mine = numbers.split('|')
        winning = winning_and_mine[0].split()
        mine = winning_and_mine[1].split()
        num_wins = 0
        for num in mine:
            if num in winning:
                num_wins += 1
        remaining_cards = []
        for i in range(num_wins):
            card_number = game_num + i + 1
            if card_number in game_num_to_num_copies:
                remaining_cards.append(card_number)
        for card in remaining_cards:
            game_num_to_num_copies[card] += num_copies_curr_card

total = 0
for game_num, num_copies in game_num_to_num_copies.items():
    total += num_copies
print(total)
