class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket_map = {
            '{': '}',
            '(': ')',
            '[': ']'
        }

        for item in s:
            if item in bracket_map:
                stack.append(item)
            else:
                if not stack:
                    return False

                cur_left = stack.pop()
                if bracket_map[cur_left] != item:
                    return False

        return not stack
