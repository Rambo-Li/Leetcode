class Solution:
    def checkValidString(self, s: str) -> bool:
        left = leftstar = 0
        for letter in s:
            if letter == '(':
                left += 1
                leftstar += 1
            elif letter == ')':
                left -= 1
                leftstar -= 1
                if leftstar < 0:
                    return False
            else:
                leftstar +=1
                left -= 1
            if left < 0:
                left = 0
        return left == 0
    
# This is a hard one. The key is to conclude that invalid means either too may left (left > star+right) or too many right(left+star < right). So along the way,
# we keep leftstar to detect the latter case, and keep left to detect the former case, since the left could be negative, and we need to reset it to zero to make
# sure the count from next '(' is correct. 