s pLargest(arr, p):
     
    arr.sort(reverse=True)
   
    for i in range(p):
        print (arr[i],end=" ") 
 
arr = [1, 23, 12, 9, 30, 2, 50]
j = len(arr)
p = 3
pLargest(arr, p)
 
