import sys
from stats import count_char, count_word, sorted_dict

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():

    if len(sys.argv) >= 2:
        contents = get_book_text(sys.argv[1])
        print(f"Found {count_word(contents)} total words")

        chars = count_char(contents)
        print(chars)
        for d in sorted_dict(chars):
            print(f"{d['char']}: {d['num']}")

    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)



main()
