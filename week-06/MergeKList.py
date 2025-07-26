def mergeKLists(L:list):
    mList=[]
    heap=[]
    k = len(L)
    # kth Element = (value, list_index, element_index) 
    kElements = [(L[i][0],i,0) for i in range(len(L)) if(L and L[i])]

    print(f"Before : {kElements}")
    heap.extend(BuildHeap(kElements))

    print(f"After: {heap}")

    print("-------------")

    while(heap):
        print(f"Before : {heap}")

        minElement, nonHeap=ExtracMin(heap)
        # print(minElement)
        mList.append(minElement[0])
        listIndex = minElement[1]
        eleIndex = minElement[2]

        if (minElement[0] == 17):
            print(f"minElement={minElement},....nonHeap={nonHeap},... len={len(L[listIndex])},...listIndex={listIndex},....eleIndex={eleIndex}")

        if(len(L[listIndex]) != eleIndex+1):
            nonHeap.append((L[listIndex][eleIndex+1], listIndex, eleIndex+1))
        
            
        heap = BuildHeap(nonHeap)
        print(f"After: {heap}")
        print("-----------------")

        # break;

    print(mList)

    return mList


def BuildHeap(KList:list):
    if (not KList or len(KList) == 1):
        return KList

    print(f"KList= {KList}")
    n = len(KList)//2

    print(f"n={n}")
    for i in range(n-1,-1,-1):
        rightNodePosition = 2*i+2

        if(rightNodePosition < len(KList)):
            if (KList[2*i+2][0] <  KList[2*i+1][0] and KList[2*i+2][0] < KList[i][0]):
                KList[2*i+2] , KList[i] = KList[i] , KList[2*i+2] 
            elif(KList[2*i+2][0] >  KList[2*i+1][0] and KList[2*i+1][0] < KList[i][0]):
                KList[2*i+1] , KList[i] = KList[i] , KList[2*i+1]

        else:
            if (KList[2*i+1][0] <  KList[i][0]):
                KList[2*i+1] , KList[i] = KList[i] , KList[2*i+1] 

    return KList


def ExtracMin(heap:list):
    if(heap):
        return heap[0],heap[1:]


# L = [[1,4,5],[1,3,4],[2,6]]
# L = [[2,5,9],[5,23,67,212],[1,10,22]]
L = [[4, 5, 13, 17,35],[8, 26, 69, 122, 135],[10, 101, 125, 450]]

mergeKLists(L)