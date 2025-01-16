with open("books/frankenstein.txt") as file:
    contents = file.read()

def wordCount(string):
    count = len(string.split())
    return count

def charCount(string):
    result = {}
    lString = string.lower()
    for char in lString:
        if char.isalpha():
            if char in result:
                result[char] += 1
            else:
                result[char] = 1
    return result

def report(string):
    WC = wordCount(string)
    CC = charCount(string)
    prettyCC = sorted(CC.items(), key=lambda x: x[1], reverse=True)
    print("--- Begin report of books/frankenstein.txt ---")
    print("Word count: " + str(WC))
    for char, count in prettyCC:
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")
    
