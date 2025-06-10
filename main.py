from stats import *
def get_book_text(filepath):
    with open(filepath) as f:
        string = f.read()
        return string

def main():
    filecontent = get_book_text("books/frankenstein.txt")
    print(f"{get_words_count(filecontent)} words found in the document")
    tt = get_letters_count(filecontent)
    print(tt)

main()
