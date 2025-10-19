from stats import get_num_words
print(get_num_words, get_num_words.stats)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    path_to_file = "books/frankenstein.txt"
    the_text = get_book_text(path_to_file)
    #print(the_text)
    num = get_num_words(the_text)
    print(f"Found {num} total words")

if __name__ == "__main__":
    main()


