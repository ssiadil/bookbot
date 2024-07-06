def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        words = word_count(file_contents)
        characters = characters_cout(file_contents)
        report(words, characters)
def word_count(text):
    words = text.split()
    return len(words)


def characters_cout(text):
    occurence = 0
    char_dict = {}
    lower_case = text.lower()
    for char in range(ord('a'), ord('z') + 1):
        c = chr(char)
        for i in lower_case:
            if i == c:
                occurence += 1
        
        char_dict[chr(char)] = occurence
        occurence = 0
    
    return char_dict


def report(num_words, characters):
    print('--- Begin report of books/frankenstein.txt ---')
    print(num_words, ' words found in the document')
    print("")
    l = list(characters.items())
    sorted_values =sorted(l, key=lambda x: x[1], reverse=True) 
    for i in sorted_values:
        print(f"The '{i[0]}' character was found {i[1]} times")

    print('--- End report ---')
main()