def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    path_to_file = "books/frankenstein.txt"
    the_text = get_book_text(path_to_file)
    #print(the_text)

#starting a counter here
    splitter = the_text.split()
    splitcounter = len(splitter)
    print(f"Found {splitcounter} total words")
main() 

