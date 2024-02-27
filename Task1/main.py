def reverse_between_max_and_min(lst):
    # Находим индексы первого максимального и последнего минимального элементов
    max_index = lst.index(max(lst))
    min_index = len(lst) - 1 - lst[::-1].index(min(lst))

    # Определяем начальный и конечный индексы для переворота подсписка
    start_index = min(max_index, min_index) + 1
    end_index = max(max_index, min_index)

    # Переворачиваем подсписок между первым максимальным и последним минимальным элементами
    lst[start_index:end_index] = reversed(lst[start_index:end_index])

    return lst


nums = [2, -11, 8, 11, 2, 3, 2, 2, 6, 7, 12, 3, 5, 10]
# [-1, -2, -3, -1, -8]
# [0, 0, 0, 0, 0]
result = reverse_between_max_and_min(nums)
print(result)
