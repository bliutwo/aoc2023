import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('input')
args = parser.parse_args()

def pretty_print(obj):
  print(json.dumps(obj, indent=2))

grid = []

with open(args.input) as f:
  for line in f:
    line = line.replace('\n', '')
    grid.append(line)

coordinates_to_identification = {}
identification_to_num = {}
symbol_coordinates = []

digits = "0123456789"

identification = 0

for i, row in enumerate(grid):
  coordinates = []
  num_builder = ""
  for j, c in enumerate(row):
    if c in digits:
      num_builder += c
      coordinates.append((i, j))
    else:
      if num_builder:
        num = int(num_builder)
        num_builder = ""
        for coordinate in coordinates:
          coordinates_to_identification[coordinate] = identification
        identification_to_num[identification] = num
        identification += 1
        coordinates = []
      if c != '.':
        symbol_coordinates.append((i, j))
  if num_builder:
    #print(f"non-empty num_builder outside j: {num_builder}")
    num = int(num_builder)
    for coordinate in coordinates:
      coordinates_to_identification[coordinate] = identification
    identification_to_num[identification] = num
    identification += 1

#print(coordinates_to_identification)
#print(symbol_coordinates)

def generate_adjacent_coordinates(x, y):
  l = []
  l.append((x-1, y))
  l.append((x+1, y))
  l.append((x, y-1))
  l.append((x, y+1))
  l.append((x+1, y+1))
  l.append((x-1, y+1))
  l.append((x+1, y-1))
  l.append((x-1, y-1))
  return l

added_already = set()
total = 0

for x, y in symbol_coordinates:
  adjacent_coordinates = generate_adjacent_coordinates(x, y)
  for adjacent in adjacent_coordinates:
    if adjacent in coordinates_to_identification:
      identity = coordinates_to_identification[adjacent]
      if identity not in added_already:
        num = identification_to_num[identity]
        #print(f"Adding: {num}")
        total += num
        added_already.add(identity)

print(total)
