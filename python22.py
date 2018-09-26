def Nmaxelements(lists1, m): 
    final_lists = [] 
  
    for i in range(0, m):  
        max1 = 0
          
        for j in range(len(lists1)):      
            if lists1[j] > max1: 
                max1 = lists1[j]; 
                  
        lists1.remove(max1); 
        final_lists.append(max1) 
          
    print(final_lists) 
 
lists1 = [5, 66, 41, 85, 0, 3, 7, 6, 10] 
m = 2
  

maxelements(list1, m) 
