import re
from collections import Counter


# 1. Count Specific Word
def count_specific_word(text, word):
    if text == "" or word == "":
        return 0

    words = re.findall(r'\b\w+\b', text.lower())

    count = 0
    for w in words:       
        if w == word.lower():  
            count += 1

    return count


# 2. Most Common Word
def identify_most_common_word(text):
    if text.strip() == "":
        return None

    words = re.findall(r'\b\w+\b', text.lower())

    counter = Counter(words)
    return counter.most_common(1)[0][0]


# 3. Average Word Length
def calculate_average_word_length(text):
    if text.strip() == "":
        return 0

    words = re.findall(r'\b\w+\b', text)

    total = 0

    for word in words:     
        total += len(word)

    return total / len(words)


# 4. Count Paragraphs
def count_paragraphs(text):
    if text.strip() == "":
        return 1

    paragraphs = [p for p in text.split("\n") if p.strip()]

    return len(paragraphs)


# 5. Count Sentences
def count_sentences(text):
    if text.strip() == "":
        return 1

    sentences = re.split(r'[.!?]+', text)
    valid_sentences = []

    for sentence in sentences:    
        if sentence.strip():      
            valid_sentences.append(sentence)

    return len(valid_sentences)


# MAIN PROGRAM
def main():

    while True:       
        print("\nTEXT ANALYSIS MENU")
        print("1. Analyze Text")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == "1":     
            text = input("Enter article text: ")
            word = input("Enter word to search: ")

            print("Specific word count:",
                  count_specific_word(text, word))

            print("Most common word:",
                  identify_most_common_word(text))

            print("Average word length:",
                  calculate_average_word_length(text))

            print("Paragraph count:",
                  count_paragraphs(text))

            print("Sentence count:",
                  count_sentences(text))

        elif choice == "2":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


main()