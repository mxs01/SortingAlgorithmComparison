def selectionSort(arr):
        """
        Basic implementation of a selection Sort algorithm (in-place)
        Time Complexity: O(n^2), n is length of array
        Space Complexity: O(1), in-place
        :return:
        """
        sortedArray:list[int] = list()
        for i in range(len(arr)):
            minIndex = i
            for j in range(i+1,len(arr)):
                if (arr[j] < arr[minIndex]):
                    minIndex = j
            (arr[i], arr[minIndex]) = (arr[minIndex], arr[i])

if __name__ == '__main__':
    arr = [1,4,2,3]
    selectionSort(arr)
    print(arr)