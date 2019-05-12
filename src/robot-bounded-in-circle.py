class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0
        direction = 0
        for ins in instructions:
            if ins == 'G':
                dx, dy = deltas[direction]
                x, y = x + dx, y + dy
            elif ins == 'L':
                direction = 3 if direction == 0 else direction - 1
            else:
                # ins == 'R'
                direction = 0 if direction == 3 else direction + 1
        return (x, y) == (0, 0) or direction != 0
