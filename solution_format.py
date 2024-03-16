import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('input')
args = parser.parse_args()

def pretty_print(obj):
    print(json.dumps(obj, indent=2))

with open(args.input) as f:
    for line in f:
        # TODO: Do something
        line = line.replace('\n', '')
        print(line)
