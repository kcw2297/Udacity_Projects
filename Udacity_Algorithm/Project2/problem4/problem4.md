## Active Directory
### In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by str representing their ids.

### Explanation : I used recursion because each user is in differnt group which has different depth

##### time complexity : O(n), it has to loop users and group separately
##### space complexity : O(n), there will be n times recursion, which means n number of call stack is taken memory
