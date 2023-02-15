class Solution:
    def canChange(self, start: str, target: str) -> bool:
        s=[]
        t=[]
        for i ,val in enumerate(start):
            if val != "_":
                s.append([i,val])
        for i,val in enumerate(target):
            if val != "_":
                t.append([i,val])
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            s_index,s_value=s[i][0] ,s[i][1]
            t_index,t_value=t[i][0] ,t[i][1]
            if s_value != t_value:
                return False
            else:
                if s_value == "L":
                    if s_index < t_index:
                        return False
                else:
                    if s_index >t_index:
                        return False
        return True
