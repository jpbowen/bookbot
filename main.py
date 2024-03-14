def main(): 
    path = "/Users/jpbowen/workspace/github.com/jpbowen/bookbot/books/frankenstein.txt" 
    text = get_book_text(path)
    num_words = count_words(text)
    lowered_words = get_lowercase(text)
    count_letters = get_char_dict(lowered_words)
    sorted_char = get_dict_sort(char_dict)
    print ("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    for items in sorted_char:
        for char, value in items.items():
            print(f"The {char} character was found {value} times")
    print(f"--- End report ---")

def count_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
         return f.read()

def get_lowercase(text):
    lowered_string = text.lower()
    return lowered_string

char_dict = {}
def get_char_dict(lowered_words):
    for char in lowered_words:
        if char.isalpha() != True:
            continue
        elif char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict 

def sort_on(char_dict):
    count_list = list(char_dict.values())
    return count_list[0]

char_list = []
def get_dict_sort(char_dict):
    for char, count in char_dict.items():
        char_list.append({char:count})
    char_list.sort(reverse=True, key=sort_on)
    return char_list
    
main()