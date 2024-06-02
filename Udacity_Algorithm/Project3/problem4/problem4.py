def sort_012(input_list):

    if len(input_list) < 2:
        return input_list


    pos_0 = 0
    pos_2 = len(input_list) - 1
    current = 0

    while current < pos_2:
        if input_list[mid] == 0:
            input_list[current] = input_list[pos_0]
            input_list[pos_0] = 0

            current += 1
            pos_0 += 1


        elif input_list[mid] == 2:
            input_list[current] = input_list[pos_2]
            input_list[pos_2] = 2

            pos_2 -= 1

        else:
            current += 1

#-------------------------------------------------------------------------------
def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


# Testing 1 : Regular case
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])

# Testing 2 : input 0
test_function([0])

# Testing 3 : input nothing
test_function([])
