def linear_search(arr,num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1

arr=[1,2,3,4,5,6,7,8,9,10]
num=5
print(linear_search(arr,num))