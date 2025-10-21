def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_letters(text):
        lower_case = text.lower()
        dictionary = {}
        for case in lower_case:
            if case in dictionary:
                dictionary[case] += 1
            else: 
                dictionary[case] = 1
        return dictionary