from generator import Generator


class BlockChain(object):

    def __init__(self):
        self.previous_block = None
        self.chain = []

    def create(self):
        self.previous_block = Generator.create_genesis_block()
        self.chain.append(self.previous_block)
        return self

    def add(self, data):
        new_block = Generator.create_next_block(self.previous_block, data)
        self.chain.append(new_block)
        self.previous_block = new_block
        return new_block.hash

    def retrieve_data_by_block_hash(self, hash):
        for block in self.chain:
            if block.hash == hash:
                return block.data

