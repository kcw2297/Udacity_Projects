# Finding the Square Root of an Integer
### Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

#### For example if the given number is 16, then the answer would be 4.
#### If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.
#### The expected time complexity is O(log(n))

### Work Flow : Binary Search
1. Find the pivot of the number
2. Squared the pivot and base on the result, find another pivot
3. Loop until we find the answer

#### Time Complexity : O(log(n)), Every loop will look only half of input and if we count the number of loop, it is 2^nth which is log2(n)
#### Space Complexity : O(1), because we do not allocate new value
