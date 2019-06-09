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
        for i in (self.timestamp, self.data):
            enc = str(i).encode('utf-8')
            sha.update(enc)
            return sha.hexdigest()


class BlockChain:

    def __init__(self):

        self.head = None
        self.blockDict = {}
        self.add_block("First Block")

    def add_block(self, data):
        timestamp = datetime.datetime.utcnow()
        if self.head:
            previous_block = self.head
            new_block = Block(timestamp, data, previous_block.hash)
            self.head = new_block
            self.blockDict[self.head.hash] = self.head
        else:
            self.head = Block(timestamp, data, 0)
            self.blockDict[self.head.hash] = self.head

    def print_chain(self):
        print("Printing chain:")
        for block in self._chain_traverser():
            print(block)

    def _chain_traverser(self):
        current_block = self.head
        while current_block:
            yield (current_block.timestamp, current_block.data)
            previous_block = self.blockDict.get(current_block.previous_hash, None)


chain = BlockChain()
chain.add_block("Transaction  01")
chain.add_block("Transaction  02")
chain.print_chain()
