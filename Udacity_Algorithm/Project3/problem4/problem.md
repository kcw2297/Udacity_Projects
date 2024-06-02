# Dutch National Flag Problem
### Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.
### Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an O(n) solution but it will not count as single traversal.

### Work Flow : Putting 0 and 2 on right place will automatically put 1 on right place
1. Initialize two pointers start and end  
2. Swap the 0 or 2 with current index if it match

#### Time Complexity : O(n), current index might loop to end
#### Space Complexity : O(1), There is no additional allocation, only swapping the elements
