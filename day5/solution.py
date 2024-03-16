import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('input')
args = parser.parse_args()

def pretty_print(obj):
    print(json.dumps(obj, indent=2))

seeds = []
maps = {}
curr_description = None

with open(args.input) as f:
    for index, line in enumerate(f):
        line = line.replace('\n', '')
        if index == 0:
            label_and_nums = line.split(':')
            nums = label_and_nums[1].rstrip().lstrip().split(' ')
            nums = [int(num) for num in nums]
            seeds = nums
        else:
            if line:
                if 'map' in line:
                    line = line.replace(':', '')
                    description_and_map = line.split(' ')
                    description = description_and_map[0]
                    if description not in maps:
                        maps[description] = {}
                    curr_description = description
                else:
                    curr_map = maps[curr_description]
                    nums = line.split()
                    nums = [int(num) for num in nums]
                    assert len(nums) == 3
                    destination = nums[0]
                    source = nums[1]
                    length = nums[2]
                    curr_map[(source, source + length)] = (destination, destination + length)

#pretty_print(maps)
print(maps)
print(seeds)

lowest = float("inf")

for seed in seeds:
    #print()
    #print(f"Looking at seed: {seed}")
    curr_key = seed
    for name, m in maps.items():
        #print()
        #print(f"Looking at: {name}")
        #print(m)
        for source, destination in m.items():
            source_lo, source_hi = source
            dest_lo, dest_hi = destination
            if curr_key >= source_lo and curr_key < source_hi:
                #print(f"Attempting to map: {curr_key}")
                difference = curr_key - source_lo
                curr_key = dest_lo + difference
                #print(f"Mapped to: {curr_key}")
                break
    #print(f"===Location for {seed}: {curr_key}===")
    if curr_key < lowest:
        lowest = curr_key

print(lowest)
