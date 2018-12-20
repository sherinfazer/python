def reorder(arr,index, s): 
  
    temp = [0] * s; 
  
 
    for i in range(0,s): 
        temp[index[i]] = arr[i] 
  
   
    for i in range(0,s): 
        arr[i] = temp[i] 
        index[i] = i 
      

arr = [50, 40, 70, 60, 90] 
index = [3, 0, 4, 1, 2] 
s= len(arr) 
  
reorder(arr, index, s) 
  
print("Reordered array is:") 
for i in range(0,s): 
    print(arr[i],end = " ") 
  
print("\nModified Index array is:") 
for i in range(0,s): 
    print(index[i],end = " ") 
