import datetime as date

from block import Block


class Generator(object):

    def __init__(self):
        pass

    @staticmethod
    def create_genesis_block():
        return Block(0, date.datetime.now(), 'Genesis Block', '0')

    @staticmethod
    def create_next_block(previous_block, data):
        this_block_index = previous_block.index + 1
        this_block_timestamp = date.datetime.now()
        this_block_data = data
        this_block_previous_hash = previous_block.hash

        # Create block according to previous block
        return Block(this_block_index, this_block_timestamp, this_block_data, this_block_previous_hash)

