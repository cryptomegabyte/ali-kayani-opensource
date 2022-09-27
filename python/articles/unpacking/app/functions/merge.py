def merge(data_a: any, data_b: any) -> tuple:
    """
    Demonstrates the use of packing operator * to merge.
    """
    merged = (*data_a,*data_b)
    return merged

def merge_list(data_a: any, data_b: any) -> tuple:
    """
    Demonstrates the use of packing operator * to merge list
    """
    merged_list = [*data_a,*data_b]
    return merged_list
