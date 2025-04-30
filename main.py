import sys

from stats import get_book_characters, get_book_words, show_report

BOOKPATH = "books/frankenstein.txt"


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    book_text = get_book_text(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    words = get_book_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    characters = get_book_characters(book_text)
    chars = show_report(characters)
    print("--------- Character Count -------")
    for item in chars:
        print(f"{item['char']}: {item['num']}")


if __name__ == "__main__":
    main()
