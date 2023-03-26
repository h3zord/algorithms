def is_anagram(first_str, second_str):
    if testing_cases(first_str, second_str):
        return testing_cases(first_str, second_str)

    first_str_list = merge_sort(list(first_str.lower()), 0, len(first_str))
    second_str_list = merge_sort(list(second_str.lower()), 0, len(second_str))

    if not first_str:
        return (first_str, "".join(second_str_list), False)
    if not second_str:
        return ("".join(first_str_list), second_str, False)

    bool_anagram = "".join(first_str_list) == "".join(second_str_list)

    return ("".join(first_str_list), "".join(second_str_list), bool_anagram)


def testing_cases(first_str, second_str):
    if (not len(first_str)) and not len(second_str):
        return (first_str, second_str, False)

    if first_str.lower() == second_str.lower():
        return (first_str.lower(), second_str.lower(), True)

    if len(first_str) == 1 and len(second_str) == 1:
        return (first_str.lower(), second_str.lower(), False)
    else:
        return None


def merge_sort(word, start=0, end=None):
    if end is None:
        end = len(word)
    if (end - start) > 1:  # se não reduzi o suficiente, continua
        mid = (start + end) // 2  # encontrando o meio
        merge_sort(word, start, mid)  # dividindo as listas
        merge_sort(word, mid, end)
        return merge(word, start, mid, end)  # unindo as listas


def merge(word, start, mid, end):
    left = word[start:mid]  # indexando a lista da esquerda
    right = word[mid:end]  # indexando a lista da direita

    # as duas listas começarão do início
    left_index, right_index = 0, 0

    # percorrer sobre a lista inteira como se fosse uma
    for general_index in range(start, end):
        if left_index >= len(left):
            word[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            word[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            word[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            # caso o da direita seja menor, ele será o escolhido
            word[general_index] = right[right_index]
            right_index = right_index + 1

    return word


print(is_anagram("roma", "amor"))
