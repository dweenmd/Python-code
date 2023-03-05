import math

def is_nice_array(n, arr):
    count = 0
    for i in range(n):
        if len(str(arr[i])) == 7:
            count += 1
    if count >= math.ceil(n/2):
        return "Beautiful"
    else:
        return "Ugly"

n = int(input())
arr = list(map(int, input().split()))

result = is_nice_array(n, arr)
print(result)
