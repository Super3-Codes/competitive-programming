t = int(input())

def isValid(a  , b , mid):
        
    if b > a: a,b = b,a 
    difference = b - mid

    if difference < 0:
        return False
    else:
        a += difference
        if a // 3 >= mid:
            return True
        else:
            return False


for _ in range(t):
    a , b = map(int,input().split())

    maxRange = (a+b)//2 

    left = 0 
    right = maxRange
    lastValid = 0

    while right >= left:
        mid = (right + left) // 2 

        if isValid(a,b,mid):
            lastValid = mid
            left = mid + 1
        else:
            right = mid - 1
    print(lastValid)
