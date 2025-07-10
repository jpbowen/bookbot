def count_words(text):
    words = text.split()
    return len(words)

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