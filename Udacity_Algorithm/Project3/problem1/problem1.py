def sqrt(num):
    if num is not int:
        return "input int"

    if num < 2:
        return num


    start = 0
    end = num

    while start < end:

        mid = (start + end)//2
        square = mid*mid

        if square == num:
            return mid

        elif square < num:
            start = mid+1
            result = mid

        else:
            end = mid
    return result


#-------------------------------------------------------------------------------

#Testing 1 : input 0
print ("Pass" if  (0 == sqrt(0)) else "Fail")

#Testing 2 : input float
print ("Pass" if  ("input int" == sqrt(-1)) else "Fail")

#Testing 3 : input 27
print ("Pass" if  (5 == sqrt(27)) else "Fail")
