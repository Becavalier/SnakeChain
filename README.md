# SnakeChain
A tiny implement of blockchain prototype.

### Block Structure 
```
|-------|-----------|------|---------------------|------|
|       |           |      |                     |      |
| index | timestamp | data | previous_block_hash | hash |
|       |           |      |                     |      |
|-------|-----------|------|---------------------|------|

- index:               the index of current block in blockchain;
- timestamp:           the create time of current block;
- data:                the data of currrent of block;
- previous_block_hash: the hash of previous block in this block chain;
- hash:                the hash of current block (calculate according to other four fields);
```

### Features TODO

- [ ] Restful api supported, saving data with json encoding;
