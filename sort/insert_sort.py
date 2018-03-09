# create by fanfan on 2018/3/9 0009
def insert_sort(lists):
    n = len(lists)
    for i in range(1,n):
        if lists[i] < lists[i-1]:
            temp = lists[i]
            j = i -1
            while j >= 0 and temp < lists[j]:
                lists[j + 1] = lists[j]
                j = j - 1
            lists[j+1] = temp
    return lists

import random
if __name__ == '__main__':
    test_list = list(range(0,20))
    random.shuffle(test_list)
    print("before sort:")
    print(test_list)
    test_list = insert_sort(test_list)
    print("after insert sort:")
    print(test_list)