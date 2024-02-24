color_to_maxcount = {
  'red': 12,
  'green': 13,
  'blue': 14
}
total = 0

#with open("sample.txt") as f:
with open("input.txt") as f:
  for line in f:
    valid_showing = True
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
      for count_and_color in counts_and_colors:
        count_and_color = count_and_color.split()
        count = int(count_and_color[0])
        color = count_and_color[1]
        if count > color_to_maxcount[color]:
          valid_showing = False
    if valid_showing:
      total += game_id

print(total)
