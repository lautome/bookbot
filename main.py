import sys
from stats import *

def get_book_text(filepath):
    with open(filepath) as f:
        string = f.read()
        return string

def check_argv(list):
    if len(list) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def main():
    check_argv(sys.argv)
    filepath = sys.argv[1]
    filecontent = get_book_text(filepath)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {get_words_count(filecontent)} total words")
    print("--------- Character Count -------")
    get_ordered_letters(get_letters_count(filecontent))
    print("============= END ===============")

main()
