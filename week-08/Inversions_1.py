def countIntersection(L1,L2):
    pairs = list(zip(L1, L2))
    
    pairs.sort()
    
    B_sorted_by_A = [b for a, b in pairs]

    mergedArray,invCount=merge_Sort_And_Count_Inversion(B_sorted_by_A,len(B_sorted_by_A))
    return invCount



def merge_Sort_And_Count_Inversion(L:list,n):
    if n<=1:
        return L,0
    else:
        (start,end)=0,n
        mid = (start + end)//2
        leftArray=L[:mid]
        rightArray=L[mid:]
        (left,lcount)=merge_Sort_And_Count_Inversion(leftArray,len(leftArray))
        (right,rcount)=merge_Sort_And_Count_Inversion(rightArray,len(rightArray))
        merged,mergecount=merge_And_Count(left,right)
        return merged,lcount+rcount+mergecount

def merge_And_Count(left:list,right:list):
    inversion_count=0
    li,lr=0,0
    A=[]
    while li<len(left) and lr<len(right):
        # print(left,right)
        if left[li]<right[lr]:
            A.append(left[li])
            li+=1
        elif left[li]>right[lr]:
            inversion_count+=len(left)-li
            A.append(right[lr])
            lr+=1
        else:
            A.append(left[li])
            # inversion_count+=len(left)-li
            li+=1
    if li>=len(left):
        A.extend(right[lr:])

    elif lr>=len(right):
        A.extend(left[li:])

    return (A,inversion_count)



inversion_count = 0 

L1 = [4, 8, 12, 16, 24, 26, 35]
# L1 = [4, 8]
L2 = [16, 18, 19, 29, 32, 39, 40]
# L2 = [16, 18]
# print(L1,L2)
L1=[8, 22, 10, 4, 17, 14]
L2=[15, 18, 3, 12, 10, 23]
inversion_count=countIntersection(L1,L2)
print(inversion_count)

    
    

