import json

def pretty_print(obj):
  print(json.dumps(obj, indent=2))

total = 0

with open("input.txt") as f:
  for line in f:
    color_to_maxcount = {
      'green': float('-inf'),
      'blue': float('-inf'),
      'red': float('-inf')
    }
    line = line.replace('\n', '')
    line = line.split(':')
    game_label = line[0]
    game_and_id = game_label.split(' ')
    game_id = int(game_and_id[1])
    showings = line[1]
    showings = showings.split(';')
    for showing in showings:
      showing = showing[1:]
      counts_and_colors = showing.split(', ')
      #pretty_print(color_to_maxcount)
      for count_and_color in counts_and_colors:
        count_and_color = count_and_color.split()
        #pretty_print(count_and_color)
        count = int(count_and_color[0])
        color = count_and_color[1]
        color_to_maxcount[color] = max(color_to_maxcount[color], count)
        #pretty_print(color_to_maxcount)
    #pretty_print(color_to_maxcount)
    power = 1
    for color,count in color_to_maxcount.items():
      if count != float('inf'):
        power *= count
    #print(f"power: {power}")
    total += power

print(total)
