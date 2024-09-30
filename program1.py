def is_valid(s: str) -> bool:
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            if stack and stack[-1] == bracket_map[char]:
                stack.pop()
            else:
                return False
    return not stack

s = "{[()]}"
print(is_valid(s))







    



  

