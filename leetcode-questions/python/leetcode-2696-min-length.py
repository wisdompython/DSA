# initial thought, was to check for the characters presence and pop the, out the list, worked fine but 



# initial solution
class Solution:
    def minLength(self, s: str) -> int:
        # convert into list
        s_list = list(s)
        i = 0
        count = 0
        while i < len(s_list):


            if i+1 < len(s_list):
                if (s_list[i] == "A" and s_list[i+1] == "B" ) or (s_list[i] == "C" and s_list[i+1] == "D"):

                    s_list.pop(i)
                    s_list.pop(i) 
                    i = 0

                    count += 1
                else:
                    i += 1
            else:
                break
        return len(s_list)
    


""" 
optimised solution

"""


class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        
        # Loop through the string
        for char in s:
            # If stack is not empty and a valid pair is formed, pop the stack
            if stack and ((stack[-1] == 'A' and char == 'B') or (stack[-1] == 'C' and char == 'D')):
                stack.pop()  # Remove the top of the stack
            else:
                stack.append(char)  # Otherwise, push the character onto the stack
        
        return len(stack)