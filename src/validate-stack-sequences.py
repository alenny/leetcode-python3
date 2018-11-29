class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        ui, oi = 0, 0
        stack = []
        while ui < len(pushed):
            if pushed[ui] == popped[oi]:
                oi += 1
                ui += 1
            elif stack and stack[-1] == popped[oi]:
                stack.pop()
                oi += 1
            else:
                stack.append(pushed[ui])
                ui += 1
        return stack == popped[oi:][::-1]
