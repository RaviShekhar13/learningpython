def countIntersection(L1,L2):
    # print("--------")
    # points=[(x,y) for x ,y in zip(L1,L2)]
    # points.sort(key=lambda x: (x[1], x[0]))
    # print(points)
    x=merge_Sort_And_Count_Inversion(L1,len(L1))
    y=merge_Sort_And_Count_Inversion(L2,len(L2)-1)
    # print(f"x={x}, y={y}")
    merge_And_Count(x,y)
    # print(x)



def merge_Sort_And_Count_Inversion(L:list,n):
    # print("merge_Sort_And_Count_Inversion")
    if n==1:
        return L
    else:
        print(f"L={L}, n={n}")
        (start,end)=0,n
        mid = (start + end)//2
        print(f"Mid:{mid}")
        leftArray=L[:mid]
        rightArray=L[mid:]
        # print(f"Recursive call: leftArray: {leftArray}, Right Array:{rightArray}")
        left=merge_Sort_And_Count_Inversion(leftArray,len(leftArray))
        right=merge_Sort_And_Count_Inversion(rightArray,len(rightArray))
        print(left,right)
        return merge_And_Count(left,right)

def merge_And_Count(left:list,right:list):
    global inversion_count
    print(f"meging={left} & {right}")
    li,lr=0,0
    A=[]
    while li<len(left) and lr<len(right):
        if left[li]<right[lr]:
            A.append(left[li])
            li+=1
        elif left[li]>right[lr]:
            # print(f"inversion_count={inversion_count}")
            inversion_count=inversion_count+len(left)-li
            A.append(right[lr])
            lr+=1
        else:
            A.append(left[li])
            li+=1
    if li>=len(left):
        A.extend(right[lr:])

    elif lr>=len(right):
        inversion_count=inversion_count+len(left)-li
        A.extend(left[li:])

    return A
    





inversion_count = 0 

L1 = [4, 8, 12, 16, 24, 26, 35]
# L1 = [4, 8]
L2 = [16, 18, 19, 29, 32, 39, 40]
# L2 = [16, 18]
# print(L1,L2)
countIntersection(L1,L2)
print(inversion_count)