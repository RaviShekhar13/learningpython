def ExtracMin(heap:list):
    if(heap):
        return heap[0],heap[1:]

def BuildHeap(KList:list):
    if (not KList or len(KList) == 1):
        return KList
    n = len(KList)//2

    for i in range(n-1,-1,-1):
        VALUE = 0 #VALUE of the Node
        PARENT = i #Non-Leaf Node
        LEFT_CHILD = 2*i+1
        RIGHT_CHILD = 2*i+2
        if(RIGHT_CHILD < len(KList)):#If RIGHT_CHILD EXISTS
            if (KList[RIGHT_CHILD][VALUE] <=  KList[LEFT_CHILD][VALUE] and KList[RIGHT_CHILD][VALUE] <= KList[PARENT][VALUE]):
                # swap PARENT & RIGHT_CHILD
                KList[RIGHT_CHILD] , KList[PARENT] = KList[PARENT] , KList[RIGHT_CHILD] 
            elif(KList[RIGHT_CHILD][VALUE] >  KList[LEFT_CHILD][VALUE] and KList[LEFT_CHILD][VALUE] < KList[PARENT][VALUE]):
                # swap PARENT & LEFT_CHILD
                KList[LEFT_CHILD] , KList[PARENT] = KList[PARENT] , KList[LEFT_CHILD]

        else:
            if (KList[LEFT_CHILD][0] <  KList[PARENT][0]):#If RIGHT_CHILD does not EXISTS 
                # swap PARENT & LEFT_CHILD
                KList[LEFT_CHILD] , KList[PARENT] = KList[PARENT] , KList[LEFT_CHILD] 

    return KList


def mergeKLists(L:list):
    mList=[]
    heap=[]
    k = len(L)
    
    kElements = [(L[i][0],i,0) for i in range(len(L)) if(L and L[i])]

    heap.extend(BuildHeap(kElements))

    while(heap):
        minElement, nonHeap=ExtracMin(heap)
        mList.append(minElement[0])
        listIndex = minElement[1]
        eleIndex = minElement[2]

        if(len(L[listIndex]) > eleIndex+1):
            nonHeap.append((L[listIndex][eleIndex+1], listIndex,eleIndex+1))
            
        heap = BuildHeap(nonHeap)

    return mList


k = int(input())
LL=[]
for i in range(k):
    subL = [int(item) for item in input().split(" ")]
    LL.append(subL)
print(*mergeKLists(LL))