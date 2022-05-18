def length_of_string(word):
    if word == '': return 0
    return 1 + length_of_string(word[:-1])

if __name__ == "__main__":
    print("Enter the word:")
    print(length_of_string(input()))