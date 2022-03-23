def is_palindrome_iterative(word):
    if (
        word == "" or
        word[0] != word[len(word) - 1]
        ):
        return False
    if (len(word) == 1):
        return True
    for index in range(len(word) // 2):
        if (word[index] != word[len(word) - 1 - index]):
            return False
    return True
