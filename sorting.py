import random
import time
'''
Objective is to code different sorting algorithms in the empty functions below. You will need to know how lists, for loops, and if statements work.


References
selectionSort: https://www.youtube.com/watch?v=xWBP4lzkoyM      https://en.wikipedia.org/wiki/Selection_sort
insertionSort: https://www.youtube.com/watch?v=OGzPmgsI-pQ      https://en.wikipedia.org/wiki/Insertion_sort
bubbleSort: https://www.youtube.com/watch?v=nmhjrI-aW5o         https://en.wikipedia.org/wiki/Bubble_sort
mergeSort: https://www.youtube.com/watch?v=JSceec-wEyw          https://en.wikipedia.org/wiki/Merge_sort
'''
### Code to generate randomly sorted lists, DO NOT MODIFY
lowerBound = 0
upperBound = 1000
sampleCount = random.randint(10,20)

def createRandomList(lowerBound, upperBound, listLength):
    return random.sample(range(lowerBound, upperBound), sampleCount)


print(createRandomList(0, 50, 10))

randomList = createRandomList(lowerBound, upperBound, sampleCount)


### Code to check sorting functionality
def checkSortingFunction(function):
    testCount = 10000
    itemCount = 20
    testingUpper = 10000
    testingLower = 0
    testingSet = []
    startTime = time.time()
    for i in range(testCount):
        testingList = createRandomList(testingLower, testingUpper, itemCount)
        sortObserved = function(list(testingList))
        testingList.sort()
        if (not testingList == sortObserved):
            print(testingList)
            print(sortObserved)
            print("Sorting does not work for ", function.__code__.co_name)
            break
        if i == testCount - 1:
            print("Sorting works for", function.__code__.co_name)
            print("Ran in", time.time() - startTime, "Seconds\n")
        
    
###

print("Original list is", randomList, "\n")

###Code selection sort

'''
General Idea

There are two parts of the list, the unsorted and sorted portion.

Find the smallest number in the unsorted list and put it at the end
of the sorted portion.

Keep doing this until there are no more unsorted values.
'''


def selectionSort(toSort):
    sortedList = toSort
    return sortedList

print("Selection Sort gives:", selectionSort(randomList), "\n")



###Code insertion sort
'''
General Idea

There are two parts of the list, the unsorted and sorted portion.

Take the first number in the unsorted portion and place it in the
correct position in the sorted portion.

Keep doing this until there are no more unsorted values.
'''


def insertionSort(toSort):
    sortedList = toSort
    return sortedList
print("Insertion Sort gives:", insertionSort(randomList), "\n")




###Code bubble sort
'''
General Idea

There are two parts of the list, the unsorted and sorted portion

Keep comparing adjacent values in the list and swap them if the
second value is less than the first. Then the value that ends up
in the last position of the list ends up being the maximum value
of the unsorted section and is added, without doing anything
, to the beginning of the sorted portion, and the unsorted
section becomes slightly more sorted from swapping.

Keep doing this until there are no more unsorted values.

Example List = [15, 6, 3, 7, 8]

Step 1: Compare 15 and 6. Swap them. New List = [6, 15, 3, 7, 8]

Step 2: Compare 15 and 3. Swap them. New List = [6, 3, 15, 7, 8]

Step 3: Compare 15 and 7. Swap them. New List = [6, 3, 7, 15, 8]

Step 4: Compare 15 and 8. Swap them. New List = [6, 3, 7, 8, 15]
15 is now in the sorted portion as one full pass over the list has been done. It is also the maximum value of the list

Step 5: Compare 6 and 3. Swap them. New List = [3, 6, 7, 8, 15]
Notice how the list is now sorted, but we keep going as we can only add one value to the sorted portion at each pass.
Of course, we can alter the algorithm such that if no swaps have been done we can exit the looping


Step 6: Compare 6 and 7. We do not need to swap them as 6 < 7. New List = [3, 6, 7, 8, 15]


Step 7: Compare 7 and 8. We do not need to swap them as 7 < 8. New List = [3, 6, 7, 8, 15]
8 is now in the sorted portion as another full pass over the list has been done. It is also the maximum of the unsorted portion of the list

This keeps going until there are no more values left in the unsorted portion of the list
'''


def bubbleSort(toSort):
    sortedList = toSort
    return sortedList

print("Bubble Sort gives:", bubbleSort(randomList), "\n")


'''
General Idea

Splits the unsorted list into two, and then calls merge sort on each half.
Then it combines the sorted halves into one full life.

'''


###Code merge sort

def mergeSort(toSort):
    sortedList = toSort
    return sortedList


print("Merge Sort gives:", mergeSort(randomList), "\n")



###Already implemented quicksort section

def quickSort(toSort):
    pivot = toSort[random.randint(0, len(toSort) - 1)]
    leftList, rightList = partition3(toSort, pivot)
    
    #leftList = toSort[0: splitIndex]
    #rightList = toSort[splitIndex : len(toSort)]
    if len(leftList) > 2:
        leftList = quickSort(leftList)
    elif len(leftList) == 2:
        if (leftList[0] > leftList[1]):
            leftList = [leftList[1], leftList[0]]
    if len(rightList) > 2:
        rightList = quickSort(rightList)
    elif len(rightList) == 2:
        if (rightList[0] > rightList[1]):
            rightList = [rightList[1], rightList[0]]
    return leftList + rightList

def partition3(toPartition, pivot):
    leftList = []
    rightList = []
    for i in range(len(toPartition)):
        if toPartition[i] < pivot:
            leftList.append(toPartition[i])
        else:
            rightList.append(toPartition[i])
    return leftList, rightList

def swap(fromIndex, toIndex, arr):  
    toValue = arr[toIndex]
    arr[toIndex] = arr[fromIndex]
    arr[fromIndex] = toValue
    return arr

#print("Quick Sort gives:", quickSort(randomList))
###
'''
checkSortingFunction(insertionSort)
checkSortingFunction(selectionSort)
checkSortingFunction(bubbleSort)
checkSortingFunction(mergeSort)
'''

#partition2([131, 118, 301, 287, 428], 169)

checkSortingFunction(quickSort)

