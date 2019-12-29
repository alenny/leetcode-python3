# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

import math

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        # Calculate total node count
        totalCount = 0
        nd = head
        while nd:
            totalCount += 1
            nd = nd.getNext()

        # Partition the list to size sqrt(totalCount)
        partSize = math.floor(math.sqrt(totalCount))

        # Find the head of each partition
        nd = head
        partHeads = []
        cnt = 0
        while nd:
            if cnt % partSize == 0:
                partHeads.append(nd)
            nd = nd.getNext()
            cnt += 1
        
        # print by partition
        partCount = len(partHeads)
        stack = []
        for i in range(partCount - 1, -1, -1):
            stack.clear()
            nd = partHeads[i]
            nextHead = None if i == partCount - 1 else partHeads[i + 1]
            while nd != nextHead:
                stack.append(nd)
                nd = nd.getNext()
            for x in stack[::-1]:
                x.printValue()

