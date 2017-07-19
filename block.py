import hashlib as hasher


'''Constructs a new Block.
Args:
  index: The index position of current block in block chain.
  timestamp: The create timestamp of current block.
  data: The data storing in this block.
  previous_hash: Previous block's hash string.
'''


class Block(object):

    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update((str(self.index) +
                   str(self.timestamp) +
                   str(self.data) +
                   str(self.previous_hash)).encode('utf-8'))
        return sha.hexdigest()

