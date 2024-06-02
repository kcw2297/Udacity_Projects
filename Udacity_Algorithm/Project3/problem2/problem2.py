def rotated_array_search(input_list, number):
    if number is not int:
        return -1

    return recursive(input_list, number, 0, len(input_list)-1)



def recursive(input_list, number, start, end):
    if start > end:
        return -1

    mid_index = start + (end - start)//2
    mid_element = input_list[mid_index]

    if mid_element == number:
        return mid_index

    if input_list[start] <= mid_element:
        if mid_element > number and input_list[start] <= number:
            return recursive(input_list, number, start, mid_index -1)
        return recursive(input_list, number, mid_index+1, end)

    if mid_element < number and input_list[end] >= number:
        return recursive(input_list, number, mid_index+1, end)
    return recursive(input_list, number, start, mid_index-1)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


# ------------------------------------------------------------------------------



def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

#Testing 1 : Find number not in list
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 100])

#Testing 2 : Find not number
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], "string"])

#Testing 3 : Find 0
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 0])
