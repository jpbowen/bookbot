import sys
from stats import *

def main(): 
    if len(sys.argv) < 2: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) # Exit with an error code
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = count_words(text)
    lowered_words = get_lowercase(text)
    count_letters = get_char_dict(lowered_words)
    sorted_char = get_dict_sort(char_dict)
    print ("\n============ BOOKBOT ============\n")
    print ("Analyzing book found at books/frankenstein.txt...\n")
    print ("----------- Word Count ----------\n")
    print(f"Found {num_words} total words\n")
    print ("--------- Character Count -------")
    for items in sorted_char:
        for char, value in items.items():
            print(f"{char}: {value}")
    print(f"============= END ===============")

def get_book_text(path):
    with open(path) as f:
         return f.read()

def get_lowercase(text):
    lowered_string = text.lower()
    return lowered_string

char_list = []
def get_dict_sort(char_dict):
    for char, count in char_dict.items():
        char_list.append({char:count})
    char_list.sort(reverse=True, key=sort_on)
    return char_list
    
main()