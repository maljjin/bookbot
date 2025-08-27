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




def main():
    letter_count("books/frankenstein.txt")

main()