
#find list of continious integres in given array
def getMaxContiniousIntegersCount(inputArray, N):
    if(N != len(inputArray)):
        N = len(inputArray)
    ans = 0;
    i = 0
    while(i < N-1):
        count = 1
        for j in range(i, N-1):
            #if j th element incremented should be equal to j+1 nth element in the given array to continue
               if(inputArray[j] + 1 == inputArray[j + 1]):
                   count += 1
               else:
                   break
        #if count of continious elements > previous streak, assign it with new streak
        ans = max(ans, count)
        i = j+1
    return ans