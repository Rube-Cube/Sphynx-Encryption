def find_greatest(input_list : list[int]) -> int:
    greatest_so_far = float('-inf')
    for i in input_list:
        if i > greatest_so_far:
            greatest_so_far = i
    return int(greatest_so_far)

def convert_UTF_8(input_string : str) -> list[int]:
    return [ord(char) for char in input_string]