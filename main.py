from typing import List

def insertionSortDescending(data: List[int]) -> List[int]:
    for i in range(1, len(data)):
        element = data[i]
        
        j = i - 1
        while j >= 0 and element > data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = element

    return data

data  = [99, 57, 77, 47, 83, 1, 24, 19]
sortedData = insertionSortDescending(data)
print("Main :: insertionSortDescending :: sorting array into monotonically decreasing order :: ", sortedData)