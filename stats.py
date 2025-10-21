def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_letters(path):
    with open(path) as f:
        lower_case = f.lower()
        print(lower_case)