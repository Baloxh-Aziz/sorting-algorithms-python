def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection(arr):
    n = len(arr)
    for i in range(n):
        mini = i
        for j in range(i + 1, n):
            if arr[j] < arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]
    return arr

def insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def quick_sort(arr,low,high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot -1)
        quick_sort(arr, pivot+1 , high)
    return arr

def partition(arr, low, high):
    p=arr[low]
    i= low +1
    j = high
    
    while True:
        while i<=j and arr[i] <= p:
            i += 1
        while i<=j and arr[j] >= p:
            j -= 1        
        if i <=j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[low], arr[j] = arr[j], arr[low]
    return j


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) //2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    return merge(left_half, right_half)
# return arr

def merge(left, right):
    new = []
    i,j = 0,0

    while i < len(left) and j<len(right):
        if left[i] < right[j]:
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j += 1
        
    new.extend(left[i:])
    new.extend(right[j:])
    return new


def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val//exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

def counting_sort(arr, exp):
    n = len(arr)
    output = [0]*n
    count = [0]*10
    for i in range(n):
        index = (arr[i]//exp)
        count[int(index%10)] +=1
    for i in range(1,10):
        count[i] += count[i-1]
    i = n-1
    while i>=0:
        index = (arr[i]//exp)
        output[count[int(index%10)]-1] = arr[i]
        count[int(index%10)] -=1
        i -= 1
    i = 0
    for i in range(0,len(arr)):
        arr[i] = output[i]

        