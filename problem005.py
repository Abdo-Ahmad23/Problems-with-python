class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if i==')':
                    if(len(stack)>0 and stack[-1]!='('):
                        return False
                    else:
                        if len(stack)>0:
                            stack.pop()
                        else:
                            return False
                elif i==']':
                    if(len(stack)>0 and stack[-1]!='['):
                        return False
                    else:
                        if len(stack)>0:
                            stack.pop()
                        else:
                            return False
                elif i=='}':
                    if(len(stack)>0 and stack[-1]!='{'):
                        return False
                    else:
                        if len(stack)>0:
                            stack.pop()
                        else:
                            return False
        if(len(stack)):
            return False
        else:
            return True