import unittest
import random
from selectionSort import selectionSort
from  quickSort import quickSort

class TestSorted(unittest.TestCase):

    def isSorted(self,data)-> bool:
        if (data is None):
            return True
        lastElement = data[0]
        for i in range(1,len(data)):
            if lastElement > data[i]:
                return False
        return True

    def generateRandomSequence(self, length:int):
        """
        generates an array with random elements
        Time Complexity: O(n), n is length of array
        Space Complexity: O(n), n is length of array
        :param length: the desired length of the array
        :return: random unsorted array
        """
        unsortedArray:list[int] = list()
        for i in range(length):
            unsortedArray.append(random.randint(-100000, 200000000))
        return unsortedArray

    def testOrderSelectionSort(self):
        data = self.generateRandomSequence(5000)
        selectionSort(data)
        self.assertTrue(self.isSorted(data))

    def testOrderQuickSort(self):
        data = self.generateRandomSequence(5000)

        self.assertTrue(self.isSorted(quickSort(data)))


if __name__ == '__main__':
    unittest.main()




