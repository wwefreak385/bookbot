def count_book_words(text):
    words = text.split()
    number = 0
    for word in words:
        number +=1
    return number

def count_book_characters(text):
    text_lower = text.lower()
    characters = {}

    for c in text_lower:
        if c not in characters:
            characters[c] = 1

        else:
            characters[c] = characters[c] + 1

    return characters

def sort_on(items):
    return items["num"]

def character_counts_sort(dict):
    list = []

    for c in dict:
        list.append({"char": c, "num": dict[c]})
    
    list.sort(reverse=True, key=sort_on)
    return list