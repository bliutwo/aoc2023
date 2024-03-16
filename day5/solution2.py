# TODO: I think the strategy rests on "reversing" the path, i.e.
# Go from the lowest possible location number, and then go backwards
# through the list of maps to find whether the corresponding seed
# is in the initial list of seeds in the first place.

# e.g. start at lowest possible location number, -> humidity ->
# temperature -> light -> water -> fertilizer -> soil -> seed
# then check if seed is in our initial list / range

# you'll probably also want to populate the list of seed ranges
# just like you did when going forwards

import argparse
import json
import sys

def corresponds_to_seed(key, seeds):
    for seed_pair in seeds:
        lo, hi = seed_pair
        if key >= lo and key < hi:
            return True
    return False

def traverse_maps(location, keys, maps, seeds):
    # keys are already reversed, so you're going backwards
    curr_key = location
    #print(location)
    #print(f"Location: {curr_key}")
    #print(keys)
    for key in keys:
        #print(f"Checking map: {key}")
        curr_map = maps[key]
        #print(curr_map)
        for keys, values in curr_map.items():
            #print(keys)
            #print(values)
            source_lo, source_hi = keys
            dest_lo, dest_hi = values
            if curr_key >= source_lo and curr_key < source_hi:
                offset = curr_key - source_lo
                curr_key = dest_lo + offset
                #print(f"Set curr_key: {curr_key}")
    # At this point, you've made it all the way through - see if the curr_key corresponds to a seed
    return corresponds_to_seed(curr_key, seeds)

def main():
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
                # This is just how to do pairs as stated in part 2
                start = None
                for index, value in enumerate(nums):
                    if index % 2 == 0:
                        start = value
                    else:
                        end = start + value
                        seeds.append((start, end))
            else:
                if line:
                    if 'map' in line:
                        line = line.replace(':', '')
                        description_and_map = line.split(' ')
                        description = description_and_map[0]
                        description += "_reversed"
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
                        # Notice that `source` and `destination` are reversed here compared to solution 1
                        #curr_map[(source, source + length)] = (destination, destination + length)
                        curr_map[(destination, destination + length)] = (source , source + length)

    #print(seeds)
    #print(maps)

    # Produce the path backwards via reversing the list of keys of the maps
    keys = list(maps)
    keys.reverse()
    #print(keys)

    # Now that we have a reversed list of keys, i.e. path backwards, let's produce
    # the actual locations we need to check
    #print(f"Supposed locations: {keys[0]}")
    locations = maps[keys[0]]
    #print(locations)

    # Do we need to check all the locations?
    # The answer _must_ be no - otherwise, it'd be too difficult to check all?
    # OR maybe it _should_ short circuit at some point...? Any way to do some kind of pruning?
    # TODO: Try brute force, then optimize later



    # NOTE: This was wrong because I forgot that a location didn't have to be in that list
    # i.e. if a location is not in this list, then it corresponds to itself, e.g. 48 -> 48
    """
    #all_locations = []
    #for start, end in locations:
    #    for i in range(start, end):
    #        all_locations.append(i)

    #all_locations.sort()

    #print(all_locations)
    """

    # TODO: Make an "all_locations" that actually corresponds to all possible locations
    # TODO: What are the bounds of all_locations? min and max value?


    for location in all_locations:
        hit = traverse_maps(location, keys, maps, seeds)
        if hit:
            print(location)
            return 0

    print("Nothing was found.")
    return 1

if __name__ == "__main__":
    sys.exit(main())
