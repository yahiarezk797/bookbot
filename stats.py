
def get_num_words(content):
    words = content.split()
    return len(words)

def get_num_litters(content):
    chars = {}
    for i in content:
        if i.lower() not in chars and i != " ":
            chars[i.lower()] = 1
        elif i != " ":
            chars[i.lower()] += 1
    return chars

def sort_on(items):
    return items["num"]

def get_sorted(chars):
    char_list = []
    for char, num in chars.items():
        x = {"char": char, "num": num}
        char_list.append(x)
    char_list.sort(reverse=True, key=sort_on)
    return char_list