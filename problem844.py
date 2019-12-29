class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        S_res = []
        T_res = []

        for c in S:
            if c == '#':
                if len(S_res) > 0:
                    del S_res[-1]
            else:
                S_res.append(c)

        for c in T:
            if c == '#':
                if len(T_res) > 0:
                    del T_res[-1]
            else:
                T_res.append(c)
        return "".join(S_res) == "".join(T_res)