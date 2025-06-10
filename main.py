def get_book_text(filepath):
    with open(filepath) as f:
        string = f.read()
        return string

def count_words(filecontent):
    list = filecontent.split()
    return len(list)

def main():
    filecontent = get_book_text("books/frankenstein.txt")
    print(f"{count_words(filecontent)} words found in the document")
main()
