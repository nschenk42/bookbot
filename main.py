from stats import get_num_words, get_book_letters

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_book_letters(text)
    print(f"Found {num_words} total words")
    print(num_letters)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()


