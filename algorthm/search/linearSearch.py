def linearSearch(arr,x): 
    flag=0
    for i in range (0, len(arr)): 
        if (arr[i] == x): 
            
            print("{}found at position ={}",x,i+1) 
            flag=1
            return (i)
    if flag ==0 :
        print("{} is not found in the input",x) 
        return(-1)
         