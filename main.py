from stats import count_words, count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    count = count_words(text)
    char_count = count_characters(text)
    print(f"Found {count} total words")
    print(char_count)

if __name__ == "__main__":
    main()
