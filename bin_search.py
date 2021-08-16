#Binary search function by s.meshkov

def pre_binary_searching(arr, num):
    """
    Функция бинарного поиска целого числа в отсортированном по возрастанию массиве целых чисел.
    Возвращает индекс числа в массиве или -1
    :param arr: отсортированный по возрастанию массив целых чисел
    :param num: искомое целое число
    :return:    индекс искомого целого числа в массиве или -1 (если число не найдено)
    """
    def binary_searching(array, number):
        length_array = len(array)
        if length_array <= 0:
            return -1
        half_index = int(length_array / 2)
        if number == array[half_index][1]:
            return array[half_index][0]
        elif length_array == 1:
            return -1
        elif number < array[half_index][1]:
            return binary_searching(array[0:half_index], number)
        elif number > array[half_index][1]:
            return binary_searching(array[half_index:], number)
    array_with_index = []
    for x in range(len(arr)):
        array_with_index.append([x, arr[x]])
    return binary_searching(array_with_index, num)


if __name__ == '__main__':
    sorted_array = [x for x in range(1, 1000)]
    print(f'sorted_array={sorted_array}')
    print('index of searching number:' + str(pre_binary_searching(sorted_array, 997)))