# Building a Trie in Python
### Before we move into the autocomplete function we need to create a working trie for storing strings. We will create two classes:

### A Trie class that contains the root node (empty string)
### A TrieNode class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.

# Finding Suffixes
### We need to add the ability to list suffixes to implement our autocomplete feature. To do that, we need to implement a new function on the TrieNode object that will return all complete word suffixes that exist below it in the trie. For example, if our Trie contains the words ["fun", "function", "factory"] and we ask for suffixes from the f node, we would expect to receive ["un", "unction", "actory"] back from node.suffixes().


### Work Flow : Using tree for balanced memory usage and performance
1. Insert the words making tree node
2. Linking the next word to the root node
3. Return the node in certain node

#### Time Complexity : O(n), prefix like "z" has to go through all the nodes, or for insertion, it has to go through all to the end
#### Space Complexity : O(n), all the words might be different
