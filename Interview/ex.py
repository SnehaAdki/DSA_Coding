class Solution:
    def prisonAfterNDays(self, cells, n: int):
        def next_day(state):
            new = [0] * len(state)
            for i in range(1, len(state) - 1):
                new[i] = 1 if state[i - 1] == state[i + 1] else 0
            return new

        seen = {}
        while n > 0:
            key = tuple(cells)
            if key in seen:
                cycle_len = seen[key] - n
                n %= cycle_len
            seen[key] = n

            if n >= 1:
                n -= 1
                cells = next_day(cells)

        return cells

s1 = Solution()
print(s1.prisonAfterNDays([0,1,0,1,1,0,0,1],7))