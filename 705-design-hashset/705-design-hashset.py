class MyHashSet:

    def __init__(self):
        self.a={}

    def add(self, key: int) -> None:
        if key not in self.a.keys():
            self.a[key]=0
        self.a[key]+=1
        

    def remove(self, key: int) -> None:
        if key in self.a.keys():
            del self.a[key]

    def contains(self, key: int) -> bool:
        return 1 if key in self.a.keys() else 0


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)