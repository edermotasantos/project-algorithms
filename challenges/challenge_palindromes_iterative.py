def is_palindrome_iterative(word):
    if (word == ""):
        return False
    high_index = len(word) - 1

    for index in range(len(word) // 2):
        if (word[index] != word[high_index]):
            return False
        high_index = high_index - 1
        index = index + 1
    return True
