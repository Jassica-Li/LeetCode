class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left_symbol = ["(", "{", "["]
        right_symbol = [")", "}", "]"]

        for symbol in s:
            if symbol in left_symbol:
                stack.append(symbol)
            else:
                if len(stack) == 0:
                    return False
                else:
                    top_symbol = stack.pop()
                    left_index = left_symbol.index(top_symbol)
                    right_index = right_symbol.index(symbol)
                    if left_index != right_index:
                        return False
        return len(stack) == 0

    print(isValid("{[]}"))