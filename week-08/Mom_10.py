import math
position=0
def MoM7Pos(arr):
    val=MoM(arr)
    return position

def hasDuplicates(L):
    return len(L) != len(set(L))
    

def MoM(L): # Median of medians
    global position
    if len(L) <= 7:
        L.sort()
        if(hasDuplicates(L)):
            position+=(math.ceil(len(L)/2))
            return(L[math.ceil(len(L)/2)])

        else:
            position+=(len(L)//2)
            return(L[(len(L)//2)])
    # return(len(L)//2)
    # Construct list of block medians
    M = []
    for i in range(0,len(L),7):
        X = L[i:i+7]
        X.sort()

        if(hasDuplicates(L)):
            position+=(math.ceil(len(X)/2))
            M.append(X[math.ceil(len(X)/2)])
        else:
            position+=(len(X)//2)
            M.append(X[len(X)//2])    

    return(MoM(M))


arr=[44,9,31,12,15,98,48,45,13,75,23,6,35,74]
arr=[5, 4, 3, 1, 1, 4, 6, 1, 4, 1, 4, 3, 3, 3, 2, 5, 6, 3, 5, 4, 6, 5, 2, 4, 5, 6, 5, 4]
print(MoM7Pos(arr))
print(position)