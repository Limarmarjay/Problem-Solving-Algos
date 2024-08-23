# TWO SUM ALGORITHM
def twoSum(nums, target):
    myDict = {}
    for index, value in enumerate(nums):
        result = target - value
        if result in myDict:
            return [index, myDict[result]]
        else:
            myDict[value] = index