import sys
from stats import count_words, count_characters, sort_characters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    count = count_words(text)
    char_count = count_characters(text)
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    sorted = sort_characters(char_count)
    for c in sorted:
        if c["char"].isalpha():
            print(f'{c["char"]}: {c["num"]}')
    
    print("============= END ===============")

if __name__ == "__main__":
    main()
