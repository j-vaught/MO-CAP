def min_waste(pieces_to_cut, pieces_produced):
  odd=False
  if(len(pieces_to_cut)%2!=0):
      odd=True
  # create a 3D table to store the results of subproblems
  dp = [[[0 for _ in range(len(pieces_to_cut))] for _ in range(len(pieces_produced))] for _ in range(len(pieces_to_cut))]
 
  # create a 2D table to store the difference between each element in list a and list b
  reference_Table=[[0 for _ in range(len(pieces_to_cut))] for _ in range(len(pieces_produced))]

  #fill in the reference table
  for i in range(len(pieces_produced)):
    for j in range(len(pieces_to_cut)):
        if(pieces_to_cut[j]<pieces_produced[i]):
            reference_Table[i][j] = pieces_produced[i]-pieces_to_cut[j]
        else:
            reference_Table[i][j] = pieces_produced[i]
#fill in the 3D table with the difference between each element in the reference table and list a
  for i in range(len(pieces_to_cut)):
    for j in range(len(pieces_produced)):
          for k in range(len(pieces_to_cut)):
            if(reference_Table[j][i]>pieces_to_cut[k]):
                dp[i][j][k] = reference_Table[j][i]-pieces_to_cut[k]
            else:
                dp[i][j][k] = reference_Table[j][i]
 
    #define a helper function to find the minimum value and its index in the reference table for a given column
  def searchminRefTable(column):
        minimum = float('inf')
        minloc=float('inf')
        for j in range(len(pieces_produced)):
            if(reference_Table[j][column]<minimum):
                minimum = min(minimum, reference_Table[j][column])
                minloc=j
        return minimum, minloc
 
  # initialize empty lists to store the results
  returnList = []
  WasteList = []
  skipList = []
  #iterate through the elements in list a and find the minimum waste
  for i in range(len(pieces_to_cut)):
    if(odd and i==0):# if the length of list a is odd, skip the first element
        mini,loca=searchminRefTable(i)
        returnList.append([loca,-1])
        WasteList.append(mini)
        skipList.append(i)
    if(i in skipList):# skip the element if it has already been processed
        continue
    minimum = float('inf')
    minloc=[]
    # iterate through all possible combinations of elements in list a and list b
    for j in range(len(pieces_produced)):
        for k in range(len(pieces_to_cut)):
            if(k in skipList):# skip the element if it has already been processed
                continue
            if(k!=i):# skip the current element
                if(dp[i][j][k]<minimum):
                    minimum = min(minimum, dp[i][j][k])
                    minloc=[j,k]
    minim,loc=searchminRefTable(i)      
    if(minimum<=minim):# if the minimum waste from the 3D table is less than or equal to the
        #minimum waste from the reference table, append the result from the 3D table
        #print(i, minimum, minloc)
        returnList.append(minloc)
        WasteList.append(minimum)
        skipList.append(minloc[1])
        skipList.append(i)
    else:
        #print(loc, minim)
        returnList.append(loc)
        WasteList.append(minim)
        skipList.append(i)

  return  returnList, WasteList, skipList

# test the function
#####################################################################
#####################################################################
#6*61, 6*27, 6*17.88, 6*7.63, 2*62.95, 1*67.33
pieces = [61,61,61,61,61,61, 27,27,27,27,27,27, 17.88,17.88,17.88,17.88,17.88,17.88, 7.63,7.63,7.63,7.63,7.63,7.63, 62.95,62.95, 67.33]
lengths = [12, 24, 36, 48, 60, 72, 84, 96, 120]
ManufacturerPipeList, wasteList, pipes=min_waste(pieces, lengths)

def count_like_numbers(lst):
  # create a dictionary to store the counts of the numbers in the first column
  counts = {}
 
  # iterate through the list and count the occurrences of each number
  for row in lst:
    if row[0] in counts:
      counts[row[0]] += 1
    else:
      counts[row[0]] = 1
 
  return counts

print("_______________________________________________________")
print("Pipe Input: ")
for number in range(len(pieces)):
    print("Pipe # "+str(number)+": " + str(pieces[number])+" in. ")
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