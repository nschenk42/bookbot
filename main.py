from stats import get_num_words

import stats
print("stats file:", stats.__file__)
print("has func:", hasattr(stats, "get_num_words"))
print("argcount:", stats.get_num_words.__code__.co_argcount)

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()


