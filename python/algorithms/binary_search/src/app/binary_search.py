from math import floor

def binary_search(numbers: list[int], search_item: int) -> int:

    index = floor(len(numbers)/2)

    if search_item == numbers[index]:
        print(f"{type(index)}")
        return index
        
    if search_item < numbers[index]:
        binary_search(numbers[:index], search_item)

    if search_item > numbers[index]:
        binary_search(numbers[index:], search_item)
