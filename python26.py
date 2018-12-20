def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        a=0
        l=0
        f=0
        while a < len(lefthalf) and l < len(righthalf):
            if lefthalf[a] < righthalf[l]:
                alist[f]=lefthalf[a]
                a=a+1
            else:
                alist[k]=righthalf[j]
                l=l+1
            f=f+1

        while a < len(lefthalf):
            alist[f]=lefthalf[a]
            a=a+1
            f=f+1

        while l < len(righthalf):
            alist[f]=righthalf[l]
            a=a+1
            f=f+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)

