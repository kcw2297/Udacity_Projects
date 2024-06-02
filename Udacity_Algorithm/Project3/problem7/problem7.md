# HTTPRouter using a Trie
# Introduction
### For this exercise we are going to implement an HTTPRouter like you would find in a typical web server using the Trie data structure we learned previously.

### There are many different implementations of HTTP Routers such as regular expressions or simple string matching, but the Trie is an excellent and very efficient data structure for this purpose.

### The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return. In a dynamic web server, the content will often come from a block of code called a handler.

### First we need to implement a slightly different Trie than the one we used for autocomplete. Instead of simple words the Trie will contain a part of the http path at each node, building from the root node /

### In addition to a path though, we need to know which function will handle the http request. In a real router we would probably pass an instance of a class like Python's SimpleHTTPRequestHandler which would be responsible for handling requests to that path. For the sake of simplicity we will just use a string that we can print out to ensure we got the right handler

### We could split the path into letters similar to how we did the autocomplete Trie, but this would result in a Trie with a very large number of nodes and lengthy traversals if we have a lot of pages on our site. A more sensible way to split things would be on the parts of the path that are separated by slashes ("/"). A Trie with a single path entry of: "/about/me" would look like:

### (root, None) -> ("about", None) -> ("me", "About Me handler")

### We can also simplify our RouteTrie a bit by excluding the suffixes method and the endOfWord property on RouteTrieNodes. We really just need to insert and find nodes, and if a RouteTrieNode is not a leaf node, it won't have a handler which is fine.

### Next we need to implement the actual Router. The router will initialize itself with a RouteTrie for holding routes and associated handlers. It should also support adding a handler by path and looking up a handler by path. All of these operations will be delegated to the RouteTrie.

### Hint: the RouteTrie stores handlers under path parts, so remember to split your path around the '/' character

### Bonus Points: Add a not found handler to your Router which is returned whenever a path is not found in the Trie.

### More Bonus Points: Handle trailing slashes! A request for '/about' or '/about/' are probably looking for the same page. Requests for '' or '/' are probably looking for the root handler. Handle these edge cases in your Router.




### Work Flow : This exercise is similar to exercise 5, but adding split_path
1. Define basic trie format, attribute : next and word
2. Define add and insert method to add next node
3. Define lookup and find method to search input element
4. return the word which is in the node

#### Time Complexity : O(n), searching and inserting require to loop the elements in the list
#### Space Complexity : O(n), In the worst case, inserting should add to the end of the node trie
