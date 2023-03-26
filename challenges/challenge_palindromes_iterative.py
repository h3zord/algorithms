def is_palindrome_iterative(word):
    if not word:
        return False

    n = len(word) - 1

    for index in range(0, len(word)):
        if word[index] != word[n - index]:
            return False

    return True
