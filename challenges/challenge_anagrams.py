def check_string(f_str, s_str):
    has_swapped = True
    num_of_iterations = 0

    while has_swapped:
        has_swapped = False
        for letr in range(len(s_str) - num_of_iterations - 1):
            if f_str[letr] != s_str[letr]:
                f_str[letr], f_str[letr + 1] = f_str[letr + 1], f_str[letr]
                has_swapped = True
        num_of_iterations += 1

    f_str = "".join(f_str)
    s_str = "".join(s_str)

    if (f_str != s_str):
        return False

    return True


def is_anagram(first_string, second_string):
    if (
        len(first_string) != len(second_string) or
        first_string == "" or second_string == ""
    ):
        return False

    f_str = list(first_string.casefold())
    s_str = list(second_string.casefold())

    return check_string(f_str, s_str)
