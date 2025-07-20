from stats import count_book_words, count_book_characters, character_counts_sort
import sys

def get_book_text(file):
    with open(file) as f:
        return f.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    num_words = count_book_words(get_book_text(sys.argv[1]))
    characters = count_book_characters(get_book_text(sys.argv[1]))
    characters_sorted = character_counts_sort(characters)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for c in characters_sorted:
        if c["char"].isalpha() == True:
            print(f"{c["char"]}: {c["num"]}")
    print("============= END ===============")

main()