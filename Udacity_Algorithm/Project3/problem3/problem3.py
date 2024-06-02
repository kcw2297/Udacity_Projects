def heapify(arr, n, i):
    largest_index = i
    left_node = 2 * i + 1
    right_node = 2 * i + 2

    # compare with left child
    if left_node < n and arr[i] < arr[left_node]:
        largest_index = left_node

    # compare with right child
    if right_node < n and arr[largest_index] < arr[right_node]:
        largest_index = right_node

    # if either of left / right child is the largest node
    if largest_index != i:
        arr[i], arr[largest_index] = arr[largest_index], arr[i]

        heapify(arr, n, largest_index)

def heapsort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap
        heapify(arr, i, 0)


def rearrange_digits(input_list):
    heapsort(input_list)

    first_list = []
    second_list = []

    length = len(input_list)
    if (length%2) != 0:
        last_element = input_list[-1]
        first_list.append(last_element)
        input_list.remove(last_element)

    for index in range(len(input_list)-1,-1,-1):
        if index == 0:
            second_list.append(input_list[index])
            continue
        elif index == 1:
            first_list.append(input_list[index])
            continue
        elif (index%2)==0:
            second_list.append(input_list[index])
        elif (index%2)!=0:
            first_list.append(input_list[index])

    first_list = ''.join(map(str,first_list))
    second_list = ''.join(map(str,second_list))
    result = []
    result.append(int(first_list))
    result.append(int(second_list))
    return result

# ------------------------------------------------------------------------------
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# Testing 1 : regular testing
test_function([[1, 2], [542, 31]])


# Testing 2 : input 0
test_function([[0,0], [0, 0]])

# Testing 3 : input very huge number and 0
test_function([[1000000000,0], [1000000000, 0]])
