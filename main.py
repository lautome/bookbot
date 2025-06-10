def get_book_text(filepath):
    with open(filepath) as f:
        string = f.read()
        return string


def main():
    print(get_book_text("books/frankenstein.txt"))

main()
