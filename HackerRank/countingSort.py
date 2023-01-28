def countingSort(arr):
    # Write your code here
    dict1={}

    for i in range(0,100):
        dict1[i]=0
    for j in (arr):
        if j  in dict1.keys():
            #dict1[i]=0
        #else:
            dict1[j]+=1
        
    return dict1.values()
