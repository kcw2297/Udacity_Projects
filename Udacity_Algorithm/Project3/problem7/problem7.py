
class RouteTrieNode:
    def __init__(self, ...):
        self.trie = {}
        self.handler = None

    def insert(self, path):
            if path not in self.trie:
                self.trie[path_block] = RouteTrieNode()
            else:
                pass


class RouteTrie:
    def __init__(self, handler):
        self.root = RouteTrieNode()
        self.handler = handler


    def insert(self, path, handler):
        node = self.root

        for path_block in path:
            node.insert(path)
            node = node.trie[path_block]

        node.handler = handler



    def find(self, path):
        node = self.root

        for path_block in path:
            node = node.trie[path_block]

        return node.handler


class Router:
    def __init__(self, root_handler, not_found_handler):
        self.root = RouteTrie(root_handler)
        self.not_found = not_found_handler


    def add_handler(self, path, handler):

        splited_path = self._split_path(path)
        self.root.insert(splited_path, handler)


    def lookup(self, path):
        splited_path = self._split_path(path)
        if len(splited_path) == 0:
            return self.root.handler


        handler = self.root.find(splited_path)

        if handler is None:
            return self.not_found

        if handler:
            return handler


    @staticmethod
    def _split_path(self, path):
        splited_path = path.split(sep='/')
        path = [element for element in splited_path if element != '']
        return path


#-------------------------------------------------------------------------------

# Testing 1 :
# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
