from math import floor

def binary_search(numbers: list[int], search_item: int) -> int:
    
    index = floor(len(numbers)/2)
    print(f"index: {index}")
    print(f"search_item: {search_item}")

    if numbers[index] == search_item:
        return index
    