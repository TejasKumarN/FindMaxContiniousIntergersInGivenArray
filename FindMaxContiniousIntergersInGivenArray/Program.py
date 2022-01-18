import FindLongestContiniousIntegersLength as utility

if __name__ == '__main__':

    #accept input array from user
    #conver input to int array
    arr = [int(x) for x in input("Input array values: ").split()]
    n = len(arr);

    #method call to do the job
    print(utility.getMaxContiniousIntegersCount(arr, len(arr)));