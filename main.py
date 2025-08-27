from stats import word_count, letter_count
def main():
    count = word_count("books/frankenstein.txt")
    print(f"{count} words found in the document")
    num_of_letter = letter_count("books/frankenstein.txt")
    print(num_of_letter)


main()