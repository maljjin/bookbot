def word_count(path_to_file):
    with open(path_to_file) as text:
        text_content = text.read()
    list_of_words = text_content.split()
    return len(list_of_words)

def letter_count(path_to_file):
    with open(path_to_file) as text:
        text_content = text.read()
    letters = set()
    for character in text_content:
        letters.add((character.lower()))
    #print(letters)
    character_count = {}
    for letter in letters:
        count = 0
        for element in text_content:
            if letter == element.lower():
                count += 1
        character_count[letter] = count
    #print(character_count)
    return character_count

def report(items):
    list_of_dict = []
    new_dict = {}
    for item in items:
        #list_of_dict = []
        if item.isalpha():
            tmp_dict = {}
            tmp_dict["char"] = item
            tmp_dict["num"] = items[item]
            #print(tmp_dict)
            list_of_dict.append(tmp_dict)
    #print(list_of_dict)
    list_of_dict.sort(key=sort_on, reverse = True)
    #print(list_of_dict)
    return list_of_dict

def sort_on(items):
    return items["num"]

def main():
    dict_1 = letter_count("books/frankenstein.txt")
    report(dict_1)

main()