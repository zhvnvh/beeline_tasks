def sort_array(arr):
    sorted = []
    while len(arr) > 0:
        min = arr[0]
        index = 0
        for i in range(1, len(arr)):
            if arr[i] < min: 
                min = arr[i]
                index = i
        sorted.append(min)
        arr.pop(index)
    return sorted

if __name__ == "__main__":
    arr = [10, 8, 4, 2, -1, -10, -100]
    print(sort_array(arr))