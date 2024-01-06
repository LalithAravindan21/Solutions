def findLeaders(arr):
    leaders = []
    n = len(arr)
    max_right = float('-inf')
    for i in range(n - 1, -1, -1):
        if arr[i] > max_right:
            leaders.append(arr[i])
            max_right = arr[i]
    leaders.reverse()
    
    return leaders
arr = list(map(int, input("Enter the unsorted array elements separated by space: ").split()))

result = findLeaders(arr)
print("Leaders in the array:", result)
