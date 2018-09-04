# python 3.5
# Word Counter
# Find N most frequent word from a file

from collections import Counter
import re
import os.path

def find_and_print(input_file, top_frequent=20):
    """
    Method that open the file and find frequent words
    @param input_file
    @param top_frequent
    @return tuple top_frequent words
    """
    if top_frequent <= 0:
        raise Exception("Wrong argument top_frequent")  # raise exception when number is <= 0
    try:
        # opening the file and divide it with regex
        words = re.findall(r'\w+', open(input_file).read().lower())

        #most_common from Counter collection counts n top frequent words
        existing_words = Counter(words).most_common(top_frequent)
    except:
        raise Exception("Error opening file: " + input_file) #raise opening file exception

    return existing_words

def main():
    while True:
        file = input("Please enter a file name: ")
        if(os.path.isfile(file)):
            break
        print(file + " Does not exist. Try again." )

    try:
        top_frequent = int(input("Enter number of top words to find: "))
        words = find_and_print(file, top_frequent)
        print("Top " + str(top_frequent) + " frequent words in " + file + " are:")
        print(words)

    except Exception as arg:
        print(arg)

    try:
        int(input("Press Enter key to continue..."))
    except:
        pass

if __name__ == '__main__':
    main()

