import unittest
import collections
# Time: O(n)
# Space: O(n)

def minStep_bfs(start:int, end: int) -> int:
    queue = collections.deque()
    steps = [None] * (end + 1)
    queue.append((start, 0))
    while queue:
        pos, cnt = queue.popleft()
        if 0 <= pos <= end and not steps[pos]:
            steps[pos] = cnt
            if pos == end:
                return steps[pos]
            queue.append((pos - 1, cnt + 1))
            queue.append((pos + 1, cnt + 1))
            queue.append((pos * 2, cnt + 1))


def minStep_dfs(start:int, end: int) -> int:
    # backward thinking
    if start >= end: # only -1
        return start - end
    if end % 2 == 0:
        if start < end // 2:
            return minStep_dfs(start, end // 2) + 1
        elif start == end // 2:
            return 1
        else: # start > end // 2
            return min(end - start, 1 + start - end // 2)   # 1 is one operation of //, start - end // 2 is backward
    else:
        return min(minStep_dfs(start, end + 1), minStep_dfs(start, end - 1)) + 1

def minStep_dfs1(start:int, end: int) -> int:
    # backward thinking
    if start >= end: # only -1
        return start - end
    if end % 2 == 0:
        return min(end - start, minStep_dfs1(start, end // 2) + 1)
    else:
        return min(minStep_dfs1(start, end + 1), minStep_dfs1(start, end - 1)) + 1




def minStep_dfs2(start:int, end: int) -> int:
    if start >= end: # only -1
        return start - end
    if end % 2 == 0:
        return min(end - start, minStep_dfs2(start * 2, end) + 1)
    else:
        return min(minStep_dfs2(start, end + 1), minStep_dfs2(start, end - 1)) + 1



class Test(unittest.TestCase):
    inp = [3, 8]
    outp = [2, 3]

    def test_unique(self):
        res = []
        for x in self.inp:
            res.append(minStep_dfs2(1, x))
        self.assertEquals(self.outp, res)

if __name__ == "__main__":
    unittest.main()