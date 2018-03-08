# create by fanfan on 2018/3/8 0008
def quick_sort(lists,left,right):
    if left >= right:
        return  lists
    key = lists[left]
    low = left
    hight = right
    while left < right:
        while left< right and lists[right] >= key:
            right -= 1

        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]

    lists[right] = key
    quick_sort(lists,low,left -1)
    quick_sort(lists,left+1,hight)
    return lists


def insert_sort(lists):
    for i in range(1,len(lists)):
        tmp = lists[i]
        j = i -1
        while j >=0 and  tmp < lists[j] :
            list[j+1] = lists[j]
            j = j -1
        lists[j+1] = tmp

def quick_sork_improve(lists,left,right,length_to_quick = 8):
    if left >= right:
        return  lists
    key = lists[left]
    low = left
    hight = right
    if right - left > length_to_quick :
        while left < right:
            while left< right and lists[right] >= key:
                right -= 1

            lists[left] = lists[right]
            while left < right and lists[left] <= key:
                left += 1
            lists[right] = lists[left]

        lists[right] = key
        quick_sork_improve(lists,low,left -1)
        quick_sork_improve(lists,left+1,hight)
    return lists

def new_quick_sot(lists):
    quick_sork_improve(lists, 0, len(test_list) -1)
    insert_sort(lists)


import random
if __name__ == '__main__':
    test_list = list(range(0,20))
    random.shuffle(test_list)
    print("before sort:")
    print(test_list)
    quick_sort(test_list,0,len(test_list)-1)
    print("after quick sort:")
    print(test_list)

    random.shuffle(test_list)
    print("before sort:")
    print(test_list)
    quick_sort(test_list, 0, len(test_list) - 1)
    print("after improve quick sort:")
    print(test_list)
