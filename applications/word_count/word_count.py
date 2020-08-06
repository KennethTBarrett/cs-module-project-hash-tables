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
        




if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))