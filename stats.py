def count_words(text):
    words = " ".join(text.split("\n"))
    return len(words.split())

def count_characters(text):
    chars = {}
    for char in text:
        if char.lower() in chars:
            chars[char.lower()] += 1
        else:
            chars[char.lower()] = 1

    return chars

