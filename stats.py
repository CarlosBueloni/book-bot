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

def sort_characters(dict):
    lst = []
    for key, value in dict.items():
        lst.append({"char": key, "num": value})
    lst.sort(key=get_num, reverse=True)
    return lst


def get_num(dict):
    return dict["num"]


