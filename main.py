from stats import *
def get_book_text(filepath):
    with open(filepath) as f:
        string = f.read()
        return string

def main():
    filepath = "books/frankenstein.txt"
    filecontent = get_book_text(filepath)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {get_words_count(filecontent)} total words")
    print("--------- Character Count -------")
    get_ordered_letters(get_letters_count(filecontent))
    print("============= END ===============")

main()
