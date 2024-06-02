# Search in a Rotated Sorted Array
### You are given a sorted array which is rotated at some random pivot point.
### Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]
### You are given a target value to search. If found in the array return its index, otherwise return -1.
### You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

### Work Flow : Sorted Array Binary Search and Recursive
1. The input_array is sorted in two different parts
2. Compare the number with middle, left, right
3. Recurse until we find the number index or return -1

#### Time Complexity : O(log(n)), Every loop will look only half of input and if we count the number of loop, it is 2^nth which is log2(n)
#### Space Complexity : O(1), There is no additional value allocated
