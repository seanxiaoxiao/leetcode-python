class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.doGenerateParenthesis(res, "", 0, 0, n)
        return res

    def doGenerateParenthesis(self, res, tmp, left, right, n):
        if left + right == n * 2:
            res.append(tmp)
        elif left == n:
            self.doGenerateParenthesis(res, tmp + ")", left, right + 1, n)
        elif left > right:
            self.doGenerateParenthesis(res, tmp + "(", left + 1, right, n)
            self.doGenerateParenthesis(res, tmp + ")", left, right + 1, n)
        else:
            self.doGenerateParenthesis(res, tmp + "(", left + 1, right, n)