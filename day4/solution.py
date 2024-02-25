import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('input')
args = parser.parse_args()

def pretty_print(obj):
    print(json.dumps(obj, indent=2))

total = 0

with open(args.input) as f:
    for line in f:
        line = line.replace('\n', '')
        label_and_numbers = line.split(':')
        numbers = label_and_numbers[1]
        winning_and_mine = numbers.split('|')
        winning = winning_and_mine[0].split()
        mine = winning_and_mine[1].split()
        count = 0
        for num in mine:
            if num in winning:
                count += 1
        if count > 0:
            points = pow(2, count - 1)
            total += points

print(total)
