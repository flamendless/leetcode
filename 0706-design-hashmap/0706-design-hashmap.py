class MyHashMap:

    def __init__(self):
        self.keys = []
        self.values = []

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            i = self.keys.index(key)
            self.values[i] = value
        else:
            self.keys.append(key)
            self.values.append(value)

    def get(self, key: int) -> int:
        if key in self.keys:
            i = self.keys.index(key)
            return self.values[i]
        return -1

    def remove(self, key: int) -> None:
        if key in self.keys:
            i = self.keys.index(key)
            del self.keys[i]
            del self.values[i]
            


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)