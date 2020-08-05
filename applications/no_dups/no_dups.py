def no_dups(s):
    cache = {}
    new_string = ""

    # Split words, add word if not in cache.
    # If it's in the cache, it won't be added
    # to our new string.
    for word in s.split():
        if word not in cache:
            new_string += word + " "
            cache[word] = True
    new_string = new_string[:-1]  # Eliminates last space
    return new_string


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))