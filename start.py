from blockchain import BlockChain

_blockchain = BlockChain().create()

for i in range(20):
    hash = _blockchain.add(i)
    print(hash)
    print(_blockchain.retrieve_data_by_block_hash(hash))
