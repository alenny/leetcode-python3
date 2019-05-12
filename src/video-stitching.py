class Solution:
    def videoStitching(self, clips, T: int) -> int:
        if T == 0:
            return 0
        clips.sort(key=lambda c: c[0])
        ret = 1
        prevEnd = 0
        currEnd = 0
        ci = 0
        N = len(clips)
        while ci < N:
            begin, end = clips[ci]
            if begin <= prevEnd:
                currEnd = max(currEnd, end)
                if currEnd >= T:
                    break
                ci += 1
            elif begin > currEnd:
                break
            else:
                ret += 1
                prevEnd = currEnd
        return ret if T <= currEnd else -1


sol = Solution()
ret = sol.videoStitching([[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], 10)
print(ret)
ret = sol.videoStitching([[0, 1], [1, 2]],  5)
print(ret)
ret = sol.videoStitching([[0, 1], [6, 8], [0, 2], [5, 6], [0, 4], [0, 3], [6, 7], [
                         1, 3], [4, 7], [1, 4], [2, 5], [2, 6], [3, 4], [4, 5], [5, 7], [6, 9]], 9)
print(ret)
ret = sol.videoStitching([[0, 4], [2, 8]], 5)
print(ret)
ret = sol.videoStitching([[5, 7], [1, 8], [0, 0], [2, 3], [
                         4, 5], [0, 6], [5, 10], [7, 10]], 5)
print(ret)
