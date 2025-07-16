
from stats import get_num_words, get_num_litters, get_sorted
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    content = get_book_text(sys.argv[1])
    num_words = get_num_words(content)
    chars = get_num_litters(content)
    sorted_chars = get_sorted(chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_chars:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")

    print("============= END ===============")













def get_book_text(book):
    with open(book) as f:
        return f.read()



main()