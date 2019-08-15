def bubbleSort(list,step=True):
        if step:
            print("\nInitil list is\n")
            print(*list,sep="-")
        for iter_num in range(len(list)-1,0,-1):
            if step:
                print("\nIteration number: ",len(list)-iter_num)
            for idx in range(iter_num):
                if step:
                    print("\n Comparing ", idx, "th element in list with ", idx + 1, "th element in list" )
                if list[idx]>list[idx+1]:
                    if step:
                        print("\n Swapping ",idx,"th element in list with ",idx+1,"th element in list as",list[idx],">",list[idx+1])
                    temp = list[idx]
                    list[idx] = list[idx+1]
                    list[idx+1] = temp
        if step:
            print("\nOutput is ",*list,"\nIf you do not want stepwise results,Please give False as last argument\n",sep="-")
        return list