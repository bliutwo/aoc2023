number_words_to_digit = {
  "one": '1',
  "two": '2',
  "three": '3',
  "four": '4',
  "five": '5',
  "six": '6',
  "seven": '7',
  "eight": '8',
  "nine": '9',
}

def get_digit_word_locations(line):
  locations = []
  for word in number_words_to_digit:
    #index = line.find(word)
    found_indices = [i for i in range(len(line)) if line.startswith(word, i)]
    for index in found_indices:
      locations.append((index, word))
  locations.sort()
  print(locations)
  if len(locations) == 1:
    return locations[0][1], locations[0][0], locations[0][1], locations[0][0]
  elif len(locations) == 0:
    return None, float("inf"), None, float("-inf")
  else:
    return locations[0][1], locations[0][0], locations[-1][1], locations[-1][0]

lines = []

with open("input.txt") as f:
#with open("single_input.txt") as f:
#with open("sample_input.txt") as f:
  for line in f:
    # Empty newlines
    line = line.replace("\n", "")
    lines.append(line)

total = 0

digits = "0123456789"

for line in lines:
  print(line)
  first_digit = ''
  first_digit_index = float('inf')
  last_digit = ''
  last_digit_index = float('-inf')
  for i, c in enumerate(line):
    if c in digits:
      if not first_digit:
        first_digit = c
        first_digit_index = i
      last_digit = c
      last_digit_index = i
  earliest_digit_word, early_index, latest_digit_word, late_index = get_digit_word_locations(line)
  #print(f"{earliest_digit_word}, {early_index}, {latest_digit_word}, {late_index}")
  if earliest_digit_word:
    earliest_digit_word = number_words_to_digit[earliest_digit_word]
  if latest_digit_word:
    latest_digit_word = number_words_to_digit[latest_digit_word]
  #print(f"{earliest_digit_word}, {early_index}, {latest_digit_word}, {late_index}")
  if early_index < first_digit_index:
    first_digit = earliest_digit_word
  if late_index > last_digit_index:
    last_digit = latest_digit_word
  #print(f"first digit: {first_digit}")
  #print(f"last digit: {last_digit}")
  number = int(first_digit + last_digit)
  print(number)
  total += number

print(total)
