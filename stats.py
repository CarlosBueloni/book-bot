def count_words(text):
    words = " ".join(text.split("\n"))
    return len(words.split())

