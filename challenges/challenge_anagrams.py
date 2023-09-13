"""
Requisito 3: Passos a se seguir
1 - Criar um algoritmo que compare duas strings e identifique se uma
    é anagrama da outra
2 - Deve ser case insensitve

Lógica a se pensar:
1 - Verificar se as strings são vazias, caso contrário retornar False
2 - Criar uma função que vai converter cada string para lista e realizar
    o sorting, trazendo essa lista ordenada como retorno da função
3 - Utilizar bubble sort para fazer a ordenação
    - Algoritmo bubble sort consultado no link do conteúdo do course:
"""


def sort_string(string):
    text = ''
    while len(string) > 0:
        # monta a string com a menor letra da palavra
        text += min(string)
        # remove a menor letra da palavra original (apenas uma vez)
        string = string.replace(min(string), '', 1)
    return text


def is_anagram(first_string, second_string):
    first_sorted = tim_sort(first_string)
    second_sorted = tim_sort(second_string)
    anagram = True

    if first_string == "" and second_string == "":
        anagram = False

    if first_sorted != second_sorted:
        anagram = False

    return (first_sorted, second_sorted, anagram)


def tim_sort(word):
    min_run = 32
    n = len(word)
    array = list(word.lower())

    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(array, start, end)

    size = min_run

    while size < n:
        for start in range(0, n, size * 2):
            mid = min(n - 1, start + size - 1)
            end = min(n - 1, mid + size)
            merged_arr = merge(
                array[start: mid + 1], array[mid + 1: end + 1]
            )
            array[start: start + len(merged_arr)] = merged_arr

        size *= 2

    return "".join(array)


def insertion_sort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1

    for i in range(left + 1, right + 1):
        key_item = array[i]

        j = i - 1

        while j >= left and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key_item

    return array


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result
