def sort_on(dict):
    return dict["count"]


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(book_text):
    words = book_text.split()
    return len(words)

def count_letters(book_text):
    letter_counts = []
    
    for letter in book_text.lower():

        letter_count = next((x for x in letter_counts if x['letter'] == letter), None)
        if letter_count == None:
            new_letter_count = { "letter": letter, "count": 1 }
            letter_counts.append(new_letter_count)
        else:
            letter_count["count"] += 1
            
    return letter_counts

def create_report(book_path):

    text = get_book_text(book_path)

    # Analyze the book
    num_words = count_words(text)
    letter_counts = count_letters(text)
    letter_counts.sort(reverse=True, key=sort_on)
    
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