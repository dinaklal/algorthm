class Binarysearch:
    def __init__(self,input,key):
        self.input=input
        self.key=key
        print(self.binarySearch_al(input,0,len(self.input)-1,self.key)
    # Returns index of x in arr if present, else -1 
    def binarySearch_al(self,arr, l, r, x): 
       # Check base case 
        print("Binary Search doing with recursion, Values Lower index={}, Upper Index={}, Key = {}",l,r,x)
        if r >= l: 
      
            mid = l + (r - l)/2
      
            # If element is present at the middle itself 
            if arr[mid] == x: 
                return mid 
              
            # If element is smaller than mid, then it  
            # can only be present in left subarray 
            elif arr[mid] > x: 
                return self.binarySearch_al(arr, l, mid-1, x) 
      
            # Else the element can only be present  
            # in right subarray 
            else: 
                return self.binarySearch_al(arr, mid + 1, r, x) 
      
        else: 
             # Element is not present in the array 
            return -1
