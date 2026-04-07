def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def count_words(text):
    words = " ".join(text.split("\n"))
    return len(words.split())

def main():
    text = get_book_text("books/frankenstein.txt")
    count = count_words(text)
    print(f"Found {count} total words")

if __name__ == "__main__":
    main()
