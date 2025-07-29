def no_overlap(L):
    sorted_on_Finish_Time = [x for x in L]
    sorted_on_Finish_Time.sort(key=lambda x:(x[2],x[1]))
    print(sorted_on_Finish_Time)
    final_list=[]
    count=0
    for timeSlot in sorted_on_Finish_Time:
        if(final_list==[]):
            # id,start,end=timeSlot[0],timeSlot[1],timeSlot[2]
            final_list.append(timeSlot)
        else:
            if(final_list[-1][2]<timeSlot[1]):
                final_list.append(timeSlot)
    return [x[0] for x in final_list]

    # print(final_list)




L=[(0,1,2),(1,1,3),(2,1,5),(3,3,4),(4,4,5),(5,5,8),(6,7,9),(7,10,13),(8,11,12)]


print(L)
print(no_overlap(L))