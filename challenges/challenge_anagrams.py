def is_anagram(first_string, second_string):
    if(
        len(first_string) != len(second_string) or
        first_string == "" or second_string == ""
        ):
        return False

    f_string = list(first_string.casefold())
    s_string = list(second_string.casefold())

    has_swapped = True
    num_of_iterations = 0

    while has_swapped:
        has_swapped = False
        for letter in range(len(s_string) - num_of_iterations - 1):
            if f_string[letter] != s_string[letter]:
                f_string[letter], f_string[letter + 1] = f_string[letter + 1], f_string[letter]
                has_swapped = True
        num_of_iterations += 1

    f_string = "".join(f_string)
    s_string = "".join(s_string)

    if (f_string != s_string):
        return False

    return True
