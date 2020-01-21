class HashTable:
    def __init__(self, size):
        self.data = [None] * size

    def _hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % len(self.data)
        return hash

    def set(self, key, value):
        address = self._hash(key)
        if not self.data[address]:
            self.data[address] = []

        self.data[address].append([key, value])

    def get(self, key):
        address = self._hash(key)
        current_buccket = self.data[address]
        if current_buccket:
            for i in range(len(current_buccket)):
                if current_buccket[i][0] == key:
                    return current_buccket[i][1]

        return None


myHashTable = HashTable(50)
myHashTable.set('grapes', 10000)
myHashTable.set("apples", 43)
myHashTable.get("apples")
