if __name__ == '__main__':
    N = int(input())
    arr = []
    
    for _ in range(N):
        command_input = input().split(" ")
        command = command_input[0];
        arguments = command_input[1:]
        
        if command !="print":
            command += "(" + ",".join(arguments) + ")"
            eval("arr."+command)
        else:
            print(arr)
