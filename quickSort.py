import random

def quickSort(array:list[int]):

    if (len(array) > 1):

        pivot:int = findPivotElement(array)

        aMinus :list[int]= [x for x in array if x < pivot]
        aEquals :list[int]= [x for x in array if x == pivot]
        aPlus :list[int]= [x for x in array if x > pivot]
        return quickSort(aMinus) + aEquals + quickSort(aPlus)

    else:
        return array



def findPivotElement(arr) -> int:
    """
    generates random pivot element
    :param arr: int array which needs to be sorted
    :return: pivot element
    """
    length = len(arr)
    index = 0
    if length > 0:
        index = random.randrange(0,length-1,1)
    return arr[index]

if __name__ == '__main__':
    arr = [1,4,2,3,7,-5,5]
    erg = quickSort(arr)
    print(erg)




