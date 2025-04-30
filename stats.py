from collections import Counter


def get_book_words(book_text: str) -> int:
    return len(book_text.split())


def get_book_characters(book_text: str) -> Counter:
    c = Counter(book_text.lower())
    return c


def show_report(counter: Counter) -> list[dict[str, str | int]]:
    return [{"char": item[0], "num": item[1]} for item in counter.most_common()]
