import hashlib
import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()


    def calc_hash(self):
      sha = hashlib.sha256()

      hash_str = self.data.encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()

    def __str__(self):
        return f'Timestamp: {self.timestamp}\nData: {self.data}\nPrevious Hash: {self.previous_hash}\nHash: {self.hash}'

class BlockChain:
    def __init__(self):
        self.current_block = None

    def add_block(self,value):
        timestamp = datetime.datetime.now()
        data = value
        previous_hash = self.current_block.hash if self.current_block else 0
        self.current_block = Block(timestamp,data,previous_hash)


#Testing

blockchain = BlockChain()
blockchain.add_block("hahahah")
print(blockchain.current_block)

# Adding empty data
blockchain2 = BlockChain()
blockchain2.add_block("")
print(blockchain2.current_block)

# Run two block chain at the same time if the time is same
# Result : two different block have different time, but two different blocks in same block chain has same time
blockchain2 = BlockChain() #blockchain2
blockchain2.add_block("")
print(blockchain2.current_block)
blockchain3 = BlockChain() #blockchain3
blockchain3.add_block("test")
print(blockchain3.current_block)
blockchain3.add_block("gogo")
print(blockchain3.current_block)
