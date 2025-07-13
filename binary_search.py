def binary_search(arr, item):
    """
    Функция выполняет Бинарный Поиск.
    Параметры:
    arr: Отсортированный список элементов.
    item: объект, который нужно найти в списке.
    """
    # Область проверки
    low = 0
    high = len(arr) - 1

    # Поиск нужного объекта
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


# Пример использования.
print(binary_search(list(range(1, 11)), 5))

    