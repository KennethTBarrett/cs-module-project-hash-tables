# Because why WOULDN'T you re-use what's already done? :)
def word_count(s):
    counts = {}

    # First, we need to remove the characters we're supposed to ignore.
    ignored_characters = ['"', ":", ";", ",", ".", "-", "+",
                          "=", "/", "\\", "|", "[", "]", "{",
                          "}", "(", ")", "*", "^", "&"]

    for character in ignored_characters:
        s = s.replace(character, '')

    # Split the string, and make it lowercase.
    split = s.lower().split()
    # Iterate through the split string, adding 1
    # to the count if it already exists, or making
    # an entry if it doesn't.
    for word in split:
        if word in counts.keys():
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

# Open the file, we'll use this as `s`
with open('robin.txt') as file:
    s = file.read()

# Get the word counts.
counts = word_count(s)
# Define our width to be used in our histogram.
width = max([len(word) for word in counts.keys()])

# We need to sort our counts.
counts = sorted(counts.items(), key=lambda x:(-x[1], x[0]))

# This will print the actual histogram line-by-line.
for count in counts:
     print(f'{count[0].ljust(width)}' + '#' * count[1])