# find unique element in array
def find_uniq(arr):def find_uniq(arr):
    mini = list(set(arr))
    return  mini[1] if mini[0] == arr[0] and mini[0] == arr[1] else mini[0]