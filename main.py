from operator import itemgetter

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(book_text):
    words = book_text.split()
    return len(words)

def count_letters(book_text):
    letter_counts = {}
    letter_counts.setdefault()

    for letter in book_text.lower():
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

    return ({ "letter": k, "count": v } for k, v in letter_counts.items())

def create_report(book_path):

    text = get_book_text(book_path)

    # Analyze the book
    num_words = count_words(text)
    letter_counts = count_letters(text)
    letter_counts = sorted(letter_counts, key=itemgetter("count"), reverse=True)
    
    print(f"--- Begin Report of {book_path} ---")
    print(f"{num_words} words found in this document")
    
    for letter in letter_counts:
        if not letter["letter"].isalpha():
            continue

        print(f"The letter {letter["letter"]} occurs {letter["count"]} times")        

    print("--- End report ---")


def main():
    book_path = "books/frankenstein.txt"

    create_report(book_path)

main()