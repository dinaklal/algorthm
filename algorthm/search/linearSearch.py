def linearSearch(arr,x): 
    flag=0
    for i in range (0, len(arr)): 
        if (arr[i] == x): 
            
            print(x,"found at position =",i+1) 
            flag=1
            return (i)
    if flag ==0 :
        print(x," is not found in the input") 
        return(-1)
         