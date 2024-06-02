## Huffman Encoding
### a data compression algorithm reduces the amount of memory (bits) required to represent a message (data)

### Explanation : I used min-heap library, heapq, to build huffman tree.

##### time complexity : O(nlogn), Using a heap to store the weight of each tree, each iteration requires O(logn) time to determine the cheapest weight and insert the new weight. There are O(n) iterations, one for each item.
##### space complexity : O(n), to decode text, loop all the input
