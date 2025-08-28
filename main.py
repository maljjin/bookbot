import sys
from stats import word_count, letter_count, report

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_to_analyse = sys.argv[1]
    #count = word_count("books/frankenstein.txt")
    #print(f"{count} words found in the document")
    #num_of_letter = letter_count("books/frankenstein.txt")
    #print(num_of_letter)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_to_analyse}...")
    print("----------- Word Count ----------")
    count = word_count(book_to_analyse)
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    num_of_letter = letter_count(book_to_analyse)
    list_of_letters = report(num_of_letter)
    #print(list_of_letters)
    for element in list_of_letters:
        print(f"{element["char"]}: {element["num"]}")
    print("============= END ===============")

main()