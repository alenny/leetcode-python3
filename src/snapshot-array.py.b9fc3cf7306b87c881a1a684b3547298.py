from collections import OrderedDict


class SnapshotArray:

    def __init__(self, length: int):
        self.curSnapId = 0
        self.arr = [OrderedDict() for _ in range(length)]
        for dic in self.arr:
            dic[self.curSnapId] = 0

    def set(self, index: int, val: int) -> None:
        self.arr[index][self.curSnapId] = val

    def snap(self) -> int:
        si = self.curSnapId
        self.curSnapId += 1
        return si

    def get(self, index: int, snap_id: int) -> int:
        dic = self.arr[index]
        if snap_id in dic:
            return dic[snap_id]
        for snapId, val in reversed(dic.items()):
            if snapId < snap_id:
                return val
        raise Exception('incorrect snap_id')

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)


sa = SnapshotArray(3)
sa.set(0, 5)
