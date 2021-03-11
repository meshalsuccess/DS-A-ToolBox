import unittest

'''The merge sort starts by slicing the array into smaller pieces by half till the array has onle 1 element
then we start sorting and merging from there 
in the helper method, I need to make sure that I am accounting for the cases where the left is done before the right and continoue the missing one'''

def mergeSort(array):
  #before that I need to check for the length of one or empty, this will also break the recursion
  if len(array) <= 1:
    return array
  #I need a middle index here then divide the array by that
  middleIdx = int(len(array)  / 2) #rounding down becuase we need an integer as an index value not a float, we can round up by adding 1 to len(array) then dividing by 2, Do not add 1 after division
  rightSide = array[: middleIdx]
  leftSide = array[middleIdx :]
  rightSideDivision = mergeSort(rightSide) #keeps on dividing the array to smaller ones
  leftSideDivision = mergeSort(leftSide) #keeps on dividing the array to smaller ones
  return mergeHelper(rightSideDivision, leftSideDivision) #calling for a helper method to help merge sort

def mergeHelper(rightSide, leftSide):
  """This helper will sort the array for us"""
  fullySortedArray = [0] * (len(rightSide)+ len(leftSide)) #creating zero array

  i,j,k = 0,0,0 #starting with zero because the first element of any array in python is zero, this should be incremented according to logic implementation below

  #logic starts here, i and j should not exceed the len of arrays, the smaller comes first and start incrementing
  while i < len(rightSide) and j < len(leftSide):
    #first logic check, keeps on checking till one of the indecies is over
    if rightSide[i] < leftSide[j]:
      fullySortedArray[k] = rightSide[i]
      i+=1
    else:
      fullySortedArray[k] = leftSide[j]
      j+=1
    k +=1
    #this while loop ends here and others will start after

  #second logic check, takes care of what was missing, above we needed both i and j to be less than length of thier arrays, so if one of them was not true, the while loop will break or stop working
  #below, we continoue to solve for that
  while i < len(rightSide):
    fullySortedArray[k] = rightSide[i]
    i+=1
    k+=1

  while j < len(leftSide):
    fullySortedArray[k] = leftSide[j]
    j+=1
    k+=1

  #when all are done, now our array is sorted and we can return it
  return fullySortedArray

"""Feel free to add more test cases below, I added 5, to have the best outcome, make sure to have uniquly named methods so change the methods names while coping and pasting"""

class TestProgram(unittest.TestCase):
    def test_1(self):
        self.assertEqual(mergeSort([8, 5, 2, 9, 5, 6, 3]), [2, 3, 5, 5, 6, 8, 9])

    def test_2(self):
        self.assertEqual(mergeSort([1,2,10,56,20,15,36]), [1,2,10,15,20,36,56])
    
    def test_3(self):
        self.assertEqual(mergeSort([5, 10, -5, -10, 100, -100, 20, -200]), [-200, -100, -10, -5, 5, 10, 20, 100])

    def test_4(self):
        self.assertEqual(mergeSort([]), [])

    def test_5(self):
        self.assertEqual(mergeSort([1]), [1])

#DO NOT CHANGE THAT,
if __name__ == '__main__':
  unittest.main()