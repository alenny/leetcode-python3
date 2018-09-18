class UpdateNode:
    def __init__(self, begin, end, inc):
        self.begin = begin
        self.end = end
        self.inc = inc
        self.prev = None
        self.next = None


class Solution:
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        # change the range increment to delta since a specific index
        deltas = []
        for upd in updates:
            # inc upd[2] from index upd[0]
            deltas.append((upd[0], upd[2]))
            # dec upd[2] from index upd[1] + 1
            deltas.append((upd[1] + 1, -upd[2]))
        deltas.sort(key=lambda d: d[0])
        ret = [0 for i in range(length)]
        val = 0
        prevIdx = 0
        for idx, delta in deltas:
            for i in range(prevIdx, idx):
                ret[i] = val
            prevIdx = idx
            val += delta
        for i in range(prevIdx, length):
            ret[i] = val
        return ret

    def getModifiedArrayByMergeUpdates(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        if len(updates) == 0:
            return [0 for i in range(length)]
        updates.sort(key=lambda upd: upd[0])
        head = UpdateNode(-1, -1, 0)
        tail = UpdateNode(-2, -2, 0)
        head.next = tail
        tail.prev = head
        self.insertAfter(head, UpdateNode(*updates[0]))
        startNode = head.next
        for i in range(1, len(updates)):
            begin, end, inc = updates[i]
            while startNode != tail and startNode.end < begin:
                startNode = startNode.next
            cur = startNode
            while cur != tail and cur.begin <= end:
                if begin > cur.begin and end >= cur.end:
                    newNode = UpdateNode(begin, cur.end, cur.inc + inc)
                    self.insertAfter(cur, newNode)
                    cur.end = begin - 1
                    begin = newNode.end + 1
                    cur = newNode.next
                elif begin > cur.begin and end < cur.end:
                    newNode = UpdateNode(begin, end, cur.inc + inc)
                    self.insertAfter(cur, newNode)
                    newNode1 = UpdateNode(end + 1, cur.end, cur.inc)
                    self.insertAfter(newNode, newNode1)
                    cur.end = begin - 1
                    begin = newNode1.end + 1
                    cur = newNode1.next
                elif begin == cur.begin and end >= cur.end:
                    cur.inc += inc
                    begin = cur.end + 1
                    cur = cur.next
                else:
                    # begin == cur.begin and end < cur.end
                    newNode = UpdateNode(end + 1, cur.end, cur.inc)
                    self.insertAfter(cur, newNode)
                    cur.inc += inc
                    cur.end = end
                    begin = newNode.end + 1
                    cur = newNode.next
            if begin <= end:
                newNode = UpdateNode(begin, end, inc)
                self.insertAfter(tail.prev, newNode)
        ret = [0 for i in range(length)]
        cur = head.next
        while cur != tail:
            for i in range(cur.begin, cur.end + 1):
                ret[i] = cur.inc
            cur = cur.next
        return ret

    def insertAfter(self, oldNode, newNode):
        newNode.prev = oldNode
        newNode.next = oldNode.next
        oldNode.next = newNode
        newNode.next.prev = newNode


sol = Solution()
# ret = sol.getModifiedArray(5, [[1, 3, 2], [2, 4, 3], [0, 2, -2]])
ret = sol.getModifiedArray(10, [[2, 4, 6], [5, 6, 8], [1, 9, -4]])
print('ok')
