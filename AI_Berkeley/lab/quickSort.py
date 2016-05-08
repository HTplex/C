def quicksort(lst):
    if len(lst) <= 1:
        return lst
    sml = [x for x in lst[1:] if x < lst[0]]
    lrg = [x for x in lst[1:] if x >= lst[0]]
    return quicksort(sml) + [lst[0]] + quicksort(lrg)

if __name__ == '__main__':
    lst = [4, 3, 5, 3, 4, 3, 4, 2, 4, 2, 1]
    print quicksort(lst)
