from heapq import merge


def merge(data_a: any, data_b: any) -> tuple:
    """
    Demonstrates the use of packing operator * to merge
    """
    merged = (*data_a,*data_b)
    return merged
