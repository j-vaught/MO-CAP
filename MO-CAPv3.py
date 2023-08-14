def addDimension(n_List, lst):
    retArr=[]
    
    def subtract_list(lst, subtract_value):
        for i in range(len(lst)):
            if isinstance(lst[i], list):
                lst[i]=subtract_list(lst[i].copy(), subtract_value)
            else:
                lst[i]-=subtract_value
        return lst
    
    for i in n_List:
        duplicate_List=lst.copy()#create copy of list to modify in subtract function
        tempArr=subtract_list(duplicate_List, i)
        retArr.append(tempArr)
    return retArr

def createNdim(n, n_List, originalList):#returns a list of objects, in increasing dimsions, so list[0] will be 0 dimension, list[3] will be a 3 dimensional list
    retArr=[]
    if n<2:n=2#make sure we have a 2d list.
    for i in range(n):
        if i==0:retArr.append(n)#append n to position 0
        if i==1:retArr.append(originalList)#append original list
        if i>=2:
            retArr.append(addDimension(n_List, retArr[i-1].copy()))#access previous list to add another dimension to
    return retArr

def min_item_list(lst, skiplst):
    min=float('inf')
    location = []
    def recurse(sub_lst, index, skiplst):
        nonlocal min, location
        for i, element in enumerate(sub_lst):
            if i in skiplst and isinstance(element, list):
                continue
            current_index=index+[i]
            if isinstance(element, list):
                recurse(element, current_index, skiplst+[i])
            else:
                if element<min and element>=0:
                    min=element
                    location=current_index
                    if i == 12: print('lol')

    recurse(lst, [], skiplst)
    return min, location

def min_item(lst):
    skipList=[]
    depthList=[]
    wasteList=[]
    baseList=[]
    for item in range(len(lst[2])):
        if item in skipList:
            continue #skip if index already accounted for

        min=float('inf')
        location=[]
        for i in range(2, len(lst)):#goes through 2d table thorugh N-dimension
            tmin, tlocation = min_item_list(lst[i][item], (skipList+[item]))
            if tmin<min: 
                location=[item]+tlocation
                min=tmin

        skipList.extend(location[:-1])#need to append in 1D.
        depthList.append(len(location)-1)
        wasteList.append(min)
        baseList.append(location[-1])#last index correlates to the main list item

    return baseList, wasteList, skipList, depthList

def pipePrintFunction(pipes_usedList, wasteList, pipeOrderList, pipeOrder, manufacturerList):
    def count_like_numbers(lst):
    # create a dictionary to store the counts of the numbers in the first column
        counts = {}
        # iterate through the list and count the occurrences of each number
        for row in lst:
            if row in counts:counts[row] += 1
            else:counts[row] = 1
        return counts

    # print the results
    print("_______________________________________________________")
    print("Pipe Input: ")
    for number in range(len(pieces)):
        print("Pipe # "+str(number)+": " + str(pieces[number])+" in. ")
    print("_______________________________________________________")
    print("Order of Pipes: ")
    for number in range(len(pipeOrder)):
        print(str(manufacturerList[pipes_usedList[number]])+" in. piece with pipes "+str(pipeOrderList[:pipeOrder[number]]))
        pipeOrderList=pipeOrderList[pipeOrder[number]:]

    print("_______________________________________________________")
    sumPipe=0
    print("Pieces to Purchase: ")
    for key, value in count_like_numbers(pipes_usedList).items():
        sumPipe+=manufacturerList[key]*value
        print(f'{manufacturerList[key]} in: {value}')
    print("_______________________________________________________")
    print("Waste: "+str(sum(wasteList))+" in of pipe")
    print("_______________________________________________________")
    print("Total Pieces of Pipe: "+str(sum(count_like_numbers(pipes_usedList).values()))+" pieces")
    print("_______________________________________________________")
    print("Total Pipe Length Calculated(including Waste): "+str(sumPipe)+" in")
    print("_______________________________________________________")
    print("Total Pipe Length Needed: "+str(sum(pieces))+" in")
    print("_______________________________________________________")

def min_waste(n_list, lst, n=3):
    primaryList=createNdim(n, n_list, lst)
    pipes_usedList, wasteList, pipeOrderList, pipeOrder = min_item(primaryList)
    pipePrintFunction(pipes_usedList, wasteList, pipeOrderList, pipeOrder, lst)


# How To Use:
# create a list of pieces you need cut. In this example, I named mine pieces.
# Create a list of pieces the manufacturere creates. mine is named lengths
# determine how deep you want the search to go. Remembere that this is exponential, so this number affects the big O time
# Example: 6, means we have O(n^6) time, whereas 4 is O(n^4). 7 is the maximum my PC can handle. 3 is the minimum value to put in.
# 5 seems to get the best results in my experience, whereas the others hog up computational time. 
# enter your varibale in the min_waste function in th order shown using my var names: (pieces, lengths, depth)
##################################################################################################################

# Start the timer
import time
start_time = time.time()

pieces = [61,61,61,61,61,61, 27,27,27,27,27,27, 17.88,17.88,17.88,17.88,17.88,17.88, 7.63,7.63,7.63,7.63,7.63,7.63, 62.95,62.95, 67.33]
lengths = [12, 24, 36, 48, 60, 72, 84, 96, 120]
min_waste(pieces, lengths, 8)

# Stop the timer
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

print(f"The function took {elapsed_time} seconds to run.")