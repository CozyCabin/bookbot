def count_words(text):
    return len(text.split())

def chars_in_text(text):
    chars_dict = {}
    for char in text:
        char = char.lower()
        if not char in chars_dict:
            chars_dict[char] = 1
        else:
            chars_dict[char] += 1
    return chars_dict

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    word_count = count_words(file_contents)
    chars = chars_in_text(file_contents)

    valid_chars = []
    for char in chars:
        if char.isalpha():
            valid_chars.append(char)
    valid_chars.sort()

    print("----------------- Word Count Report -----------------")
    print(f"Total words in document: {word_count}\n")
    print(f"--- Total count for each letter ---")
    for char in valid_chars:
        print(f"{char}: {chars[char]}")
