def get_min_max(ints):
    length_list = len(ints)
    min = ints[0]
    max = ints[0]

    for index in range(length_list):
        if min > ints[index]:
            min = ints[index]
        if max < ints[index]:
            max = ints[index]

    return min, max




#-------------------------------------------------------------------------------

import random




# Testing 1 : Regular test
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")



# Testing 2 : 0 edge test
l = [i for i in range(0, 1)]
random.shuffle(l)

print ("Pass" if ((0, 0) == get_min_max(l)) else "Fail")


# Testing 3 : Not starting from 0
l = [i for i in range(1, 7)]
random.shuffle(l)

print ("Pass" if ((1, 6) == get_min_max(l)) else "Fail")
