# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".

#     Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def biggieSize(var):
    for x in range(len(var)):
        if(var[x] > 0):
            var[x] = "big"
    return var
print(biggieSize([1,-2,-5,6,-9,0]))

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).

#     Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
#     Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def countPositives(var):
    count = 0
    for x in range(len(var)):
        if(var[x] > 0):
            count += 1
        if(x == len(var) - 1):
            var[x] = count
    return var
print(countPositives([1,6,-4,-2,-7,2]))

# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.

#     Example: sum_total([1,2,3,4]) should return 10
#     Example: sum_total([6,3,-2]) should return 7

def sumTotal(var):
    sum = 0
    for x in range(len(var)):
        sum += var[x]
    return sum
print(sumTotal([1,2,3,4,5]))

# Average - Create a function that takes a list and returns the average of all the values.

#     Example: average([1,2,3,4]) should return 2.5

def average(var):
    sum = 0
    for x in range(len(var)):
        sum += var[x]
    return sum / len(var)
print(average([1,2,3,4]))

# Length - Create a function that takes a list and returns the length of the list.

#     Example: length([37,2,1,-9]) should return 4
#     Example: length([]) should return 0

def length(var):
    return len(var)
print(length([1,2,3,4]))

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.

#     Example: minimum([37,2,1,-9]) should return -9
#     Example: minimum([]) should return False

def minimum(var):
    if(len(var) == 0):
        return False
    minVal = var[0]
    for x in range(1, len(var)):
        if(minVal > var[x]):
            minVal = var[x]
    return minVal
print(minimum([37,2,1,-9]))

# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.

#     Example: maximum([37,2,1,-9]) should return 37
#     Example: maximum([]) should return False

def maximum(var):
    if(len(var) == 0):
        return False
    maxVal = var[0]
    for x in range(1, len(var)):
        if(maxVal < var[x]):
            maxVal = var[x]
    return maxVal
print(maximum([37,2,1,-9]))

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.

#     Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimateAnalysis(var):
    sum = 0
    avg = 0
    max = var[0]
    min = var[0]
    for x in range(len(var)):
        sum += var[x]
        if(min > var[x]):
            min = var[x]
        if(max < var[x]):
            max = var[x]
    dictionary = { 
        'sumTotal' : sum,
        'average' : sum / len(var),
        'minimum' : min,
        'maximum' : max,
        'length' : len(var)
        }
    return dictionary
print(ultimateAnalysis([37,2,1,-9]))

# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)

#     Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverseList(var):
    var = var[::-1]
    return var
print(reverseList([37,2,1,-9]))