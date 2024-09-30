def isvalid(s: str) -> bool:
   
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

test_strings = ["()", "{[]}", "(]", "([)]", "{[()]}"]
for s in test_strings:
    print(f"{s}: {isvalid(s)}")







    



  

