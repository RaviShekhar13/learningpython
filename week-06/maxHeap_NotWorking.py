def isMaxHeap(KList:list, i):
    j=2*i+2
    bR = False
    if (j < len(KList)): 
        bR = (KList[i] > KList[j])
    else:
        bR=not bR
    
    bL = False
    k=2*i+1
    if (k < len(KList)):
        bL = (KList[i] > KList[k]) 
    else:
        bL = not bL

    return bL and bR

    

def maxHeapify(Klist:list, n, i):
    PARENT = i #Non-Leaf Node
    if not isMaxHeap(KList, PARENT):

        LEFT_CHILD = 2*i+1
        RIGHT_CHILD = 2*i+2
        if(RIGHT_CHILD < len(KList)):#If RIGHT_CHILD EXISTS
            if (KList[RIGHT_CHILD] >=  KList[LEFT_CHILD] and KList[RIGHT_CHILD] > KList[PARENT]):
                # swap PARENT & RIGHT_CHILD
                KList[RIGHT_CHILD] , KList[PARENT] = KList[PARENT] , KList[RIGHT_CHILD]
                maxHeapify(KList, len(KList, RIGHT_CHILD))
                    
            elif(KList[LEFT_CHILD] > KList[RIGHT_CHILD] and KList[LEFT_CHILD] > KList[PARENT]):
                # swap PARENT & LEFT_CHILD
                KList[LEFT_CHILD] , KList[PARENT] = KList[PARENT] , KList[LEFT_CHILD]
                maxHeapify(KList, len(KList, LEFT_CHILD))

        else:
            if (KList[LEFT_CHILD] >  KList[PARENT]):#If RIGHT_CHILD does not EXISTS 
                # swap PARENT & LEFT_CHILD
                KList[LEFT_CHILD] , KList[PARENT] = KList[PARENT] , KList[LEFT_CHILD] 
                maxHeapify(KList, len(KList, LEFT_CHILD))
    return KList
