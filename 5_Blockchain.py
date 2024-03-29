import hashlib
import datetime
import time


class Block:

    def __init__(self, timestamp, data, previous_hash=None, previous=None):
        self.timestamp = str(timestamp)
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.previous = previous

    def calc_hash(self):
        sha = hashlib.sha256()
        for i in [self.timestamp, self.data]:
            print("encoding this...{}".format(i))
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
            new_block = Block(timestamp, data, previous_block.hash, previous_block)
            self.head = new_block
        else:
            self.head = Block(timestamp, data)
        time.sleep(0.5)

    def print_chain(self):
        print("Printing chain:")
        for block in self._chain_traverser():
            print(block)

    def check_hash(self):
        current_block = self.head

        while current_block:
            cur_hash = current_block.previous_hash
            prev_hash = current_block.previous.hash
            if cur_hash == prev_hash:
                print("Block {} has coincident hash with previous: {} ".format(
                    current_block.data, cur_hash))
            else:
                print("Block {} has different hash than previous: {}, previous hash={}".format(
                    current_block.data, cur_hash, prev_hash))
            current_block = current_block.previous

    def _chain_traverser(self):
        current_block = self.head
        while current_block:
            yield (current_block.timestamp, current_block.data)
            current_block = current_block.previous


chain = BlockChain()

chain.add_block("Transaction  01")
chain.add_block("Transaction  02")
chain.add_block("Transaction  03")
for x in range(10):
    chain.add_block("Transaction " + str(x + 3))
chain.print_chain()
chain.check_hash()
