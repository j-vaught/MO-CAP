def min_waste(pieces_to_cut, pieces_sold):
 
    # create a 2D table to store the difference between each element in list a and list b (aka reference table or R-Table)
    reference_Table=[[0 for _ in range(len(pieces_to_cut))] for _ in range(len(pieces_sold))]
    # create a 3D table to store the results of subproblems
    threedp = [[[0 for _ in range(len(pieces_to_cut))] for _ in range(len(pieces_sold))] for _ in range(len(pieces_to_cut))]
    # create a 4D table to store the results of subproblems
    dp = [[[[0 for _ in range(len(pieces_to_cut))] for _ in range(len(pieces_to_cut))] for _ in range(len(pieces_sold))] for _ in range(len(pieces_to_cut))]

    #fill in the reference table
    for i in range(len(pieces_sold)):
        for j in range(len(pieces_to_cut)):
            if(pieces_to_cut[j]<pieces_sold[i]):
                reference_Table[i][j] = pieces_sold[i]-pieces_to_cut[j]
            else:
                reference_Table[i][j] = -float('inf')

    #fill in the 3D table with the difference between each element in the reference table and list a
    for i in range(len(pieces_to_cut)):
        for j in range(len(pieces_sold)):
            for k in range(len(pieces_to_cut)):
                if(reference_Table[j][i]>pieces_to_cut[k]):
                    threedp[i][j][k] = reference_Table[j][i]-pieces_to_cut[k]
                else:
                    threedp[i][j][k] = -float('inf')

    #fill in the 4D table with the difference between each element in the 3D table and list a
    for i in range(len(pieces_to_cut)):
        for j in range(len(pieces_sold)):
            for k in range(len(pieces_to_cut)):
                for l in range(len(pieces_to_cut)):
                    if(threedp[i][j][k]>pieces_to_cut[l]):
                        dp[i][j][k][l] = threedp[i][j][k]-pieces_to_cut[l]
                    else:
                        dp[i][j][k][l] = -float('inf')
   
        #define a helper function to find the minimum value and its index in the reference table for a given column
    def searchmin2DTable(itemNumber):
            minimum = float('inf')
            minloc=float('inf')
            for j in range(len(pieces_sold)):
                if(reference_Table[j][itemNumber]<minimum and reference_Table[j][itemNumber]>=0):
                    minimum = min(minimum, reference_Table[j][itemNumber])
                    minloc=j
            return minimum, minloc
        #define a helper function to find the minimum value and its index in the 3D table for a given item index
   
    def searchmin3DTable(itemNumber, skipList):
            minimum = float('inf')
            minloc=float('inf')
            for j in range(len(pieces_sold)):
                for k in range(len(pieces_to_cut)):
                    if(k in skipList or k == itemNumber):# skip the element if it has already been processed or is same element as current element
                            continue
                    if(threedp[itemNumber][j][k]<minimum and threedp[itemNumber][j][k]>=0):
                        minimum = min(minimum, threedp[itemNumber][j][k])
                        minloc=[j,k]
            return minimum, minloc
       
    def searchmin4DTable(itemNumber, skipList):
            minimum = float('inf')
            minloc=float('inf')
            for j in range(len(pieces_sold)):
                for k in range(len(pieces_to_cut)):
                    if(k in skipList or k == itemNumber):# skip the element if it has already been processed or is same element as current element
                            continue
                    for l in range(len(pieces_to_cut)):
                        if(l in skipList or l == itemNumber or l==k):# skip the element if it has already been processed or is same element as current element
                            continue
                        if(dp[itemNumber][j][k][l]<minimum and dp[itemNumber][j][k][l]>=0):
                            minimum = min(minimum, dp[itemNumber][j][k][l])
                            minloc=[j,k,l]
            return minimum, minloc
   
  # initialize empty lists to store the results
    returnList = []
    WasteList = []
    skipList = []
    combinationList = []
   
    for itemNumber in range(len(pieces_to_cut)):
        if(itemNumber in skipList):# skip the element if it has already been processed
            continue
        if(len(pieces_to_cut)-len(skipList)==2):# if the length of list a is odd and is undivideable by 3, ...
                                        # ... set first element min to minimum using manufacturer smallest piece that will fit(2d Table)
            min2d=searchmin2DTable(itemNumber)
            min3d=searchmin3DTable(itemNumber, skipList)
            if(min2d[0]<=min3d[0]):
                returnList.append(min2d[1])
                WasteList.append(min2d[0])
                skipList.append(itemNumber)
                combinationList.append(1)
            else:
                returnList.append(min3d[1][0])
                WasteList.append(min3d[0])
                skipList.append(itemNumber)
                skipList.append(min3d[1][1])
                combinationList.append(2)
            continue
        elif(len(pieces_to_cut)-len(skipList)==1):# if available parts is equal to 1, set the element min to minimum using manufacturer smallest piece that will fit(2d Table)
            tempminimum,loca=searchmin2DTable(itemNumber)
            returnList.append(loca)
            WasteList.append(tempminimum)
            skipList.append(itemNumber)
            combinationList.append(1)
            continue

        min2d=searchmin2DTable(itemNumber)
        min3d=searchmin3DTable(itemNumber, skipList)
        min4d=searchmin4DTable(itemNumber, skipList)
        if(min2d[0]<=min3d[0] and min2d[0]<=min4d[0]):
            returnList.append(min2d[1])
            WasteList.append(min2d[0])
            skipList.append(itemNumber)
            combinationList.append(1)
        elif(min3d[0]<min2d[0] and min3d[0]<=min4d[0]):
            returnList.append(min3d[1][0])
            WasteList.append(min3d[0])
            skipList.append(itemNumber)
            skipList.append(min3d[1][1])
            combinationList.append(2)
        else:
            returnList.append(min4d[1][0])
            WasteList.append(min4d[0])
            skipList.append(itemNumber)
            skipList.append(min4d[1][1])
            skipList.append(min4d[1][2])
            combinationList.append(3)
   
    return returnList, WasteList, skipList, combinationList


# test the function
#####################################################################
#####################################################################
#6*61, 6*27, 6*17.88, 6*7.63, 2*62.95, 1*67.33
pieces = [61,61,61,61,61,61, 27,27,27,27,27,27, 17.88,17.88,17.88,17.88,17.88,17.88, 7.63,7.63,7.63,7.63,7.63,7.63, 62.95,62.95, 67.33]
lengths = [12, 24, 36, 48, 60, 72, 84, 96, 120]
ManufacturerPipeList, wasteList, pipes, pipeOrder = min_waste(pieces, lengths)

def count_like_numbers(lst):
  # create a dictionary to store the counts of the numbers in the first column
  counts = {}
  # iterate through the list and count the occurrences of each number
  for row in lst:
    if row in counts:
      counts[row] += 1
    else:
      counts[row] = 1
  return counts

# print the results
print("_______________________________________________________")
print("Pipe Input: ")
for number in range(len(pieces)):
    print("Pipe # "+str(number)+": " + str(pieces[number])+" in. ")
print("_______________________________________________________")
print("Order of Pipes: ")
for number in range(len(pipeOrder)):
  print(str(lengths[ManufacturerPipeList[number]])+" in. piece with pipes "+str(pipes[:pipeOrder[number]]))
  pipes=pipes[pipeOrder[number]:]

print("_______________________________________________________")
sumPipe=0
print("Pieces to Purchase: ")
for key, value in count_like_numbers(ManufacturerPipeList).items():
    sumPipe+=lengths[key]*value
    print(f'{lengths[key]} in: {value}')
print("_______________________________________________________")
print("Waste: "+str(sum(wasteList))+" in of pipe")
print("_______________________________________________________")
print("Total Pieces of Pipe: "+str(sum(count_like_numbers(ManufacturerPipeList).values()))+" pieces")
print("_______________________________________________________")
print("Total Pipe Length Calculated(including Waste): "+str(sumPipe)+" in")
print("_______________________________________________________")
print("Total Pipe Length Needed: "+str(sum(pieces))+" in")
print("_______________________________________________________")
