# create by fanfan on 2018/3/9 0009
def select_sort(lists):
    n = len(lists)
    for i in range(0,n):
        min = i
        for j in range(i+1,n):
            if lists[j] < lists[min]:
                min = j
            lists[min],lists[i] = lists[i],lists[min]
    return lists

import random
if __name__ == '__main__':
    test_list = list(range(0,20))
    random.shuffle(test_list)
    print("before sort:")
    print(test_list)
    test_list = select_sort(test_list)
    print("after select sort:")
    print(test_list)