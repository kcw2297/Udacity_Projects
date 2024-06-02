class TrieNode:
    def __init__(self):
        # Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def find_words(self, prefix):
        """Find all words starting with given prefix"""
        matches = []
        if self.is_word:
            matches += [prefix]
        for (char, node) in self.children.items():
            matches += node.find_words(prefix + char)

        return matches

    def insert(self, char):
        self.children[char] = TrieNode()

# The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        # Add a word to the Trie
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.insert(char)
            current_node = current_node.children[char]
        current_node.is_word = True

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node

    def match(self, prefix):
        # Return all matching words in the tree
        node = self.find(prefix)
        if node:
            return node.find_words(prefix)
        else:
            return []



#-------------------------------------------------------------------------------
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]

for word in wordList:
    MyTrie.insert(word)



# Testing 1 : Regular Case
print(MyTrie.match("ant"))

# Testing 2 : Adding nothing => Returns all
print(MyTrie.match(""))


# Testing 3 : Checking not in trie
print(MyTrie.match("pop"))
