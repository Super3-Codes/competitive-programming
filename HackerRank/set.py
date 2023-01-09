set_a = set(input().split())
flag = True
for i in range(int(input())):
    a_set = set(input().split())
    if a_set.issubset(set_a) and len(set_a-a_set) >= 1:
        pass
    else:
        flag = False
        break
print(flag)  
