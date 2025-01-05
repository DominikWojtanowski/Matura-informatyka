from typing import List

ciag = [1,-2,6,-5,7,-3,7]

def max_subseq_of_arr(arr: List[int]) -> int:
    max_ending_here = ciag[0]
    max_so_far = ciag[0]

    # print(max_ending_here)
    # print(max_so_far)

    for i in range(1,len(ciag)):
        max_ending_here = ciag[i] if ciag[i] > max_ending_here + ciag[i] else max_ending_here + ciag[i]
        max_so_far = max_ending_here if max_ending_here > max_so_far else max_so_far

    return max_so_far

def most_popular_element(arr: List[int]) -> List:
    num_dict = {}

    for num in arr:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] = num_dict[num] + 1
    max_list = []
    max_count = 0

    for key, item in num_dict.items():
        # print(max_count, item, key)
        if max_count < item:
            max_count = item
            max_list.clear()
            max_list.append(key)
        elif max_count == item:
            max_list.append(key)

    return max_list
most_popular_element(ciag)




