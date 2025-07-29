def firstIndex(L,x):
    low, high = 0, len(L)-1
    start=None
    while low <= high:
        mid = (low + high)//2
        
        if L[mid] >= x:
            high = mid - 1
        else:
            low = mid + 1

        if L[mid] == x:
            start=mid
    return start

def lastIndex(L,x):
    (low, high)=(0, len(L)-1)
    end=None
    while low <= high:
        mid=(low+high)//2

        if L[mid] > x:
            high = mid - 1
        else:
            low = mid + 1

        if L[mid]==x:
            end=mid
    return end


def findOccOf(L,x):
    
    print(firstIndex(L,x))
    print(lastIndex(L,x))
    
L=[3, 3, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 9, 9, 9, 9, 10, 10, 11, 13, 14, 14, 14, 14, 14, 14]
x=5
findOccOf(L,x)