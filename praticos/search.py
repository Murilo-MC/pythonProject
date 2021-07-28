def search(list, target, i, j):
    if i == j:
        return -1
    mid = (i+j)//2
    if list[mid] == target:
        return mid
    if target < list[mid]:
        return search(list, target, i, mid)
    else:
        return search(list, target, mid+i, j)
