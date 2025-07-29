def getChunks(arr,size):
    return [arr[i:i+size] for i in range(0,len(arr), size)]


def MoM7Pos(arr):
    size=7
    allChunks = getChunks(arr,size)
    allSoterdChunks=[sorted(chunk) for chunk in allChunks] 
    return allSoterdChunks

arr=[44,9,31,12,15,98,48,45,13,75,23,6,35,74]
position = MoM7Pos(arr)


# def findMedian(arr):



# print(position)