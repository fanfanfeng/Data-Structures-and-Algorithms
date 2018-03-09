# create by fanfan on 2018/3/9 0009
def bubble_sort(lists):
    n = len(lists)
    for i in range(n):
        for j in range(1,n-i):
            if lists[j-1] > lists[j]:
                lists[j-1],lists[j] = lists[j],lists[j-1]
    return lists

#优化1：某一趟遍历如果没有数据交换，则说明已经排好序了，因此不用再进行迭代了。
#用一个标记记录这个状态即可。
def bubble_sort2(lists):
    n = len(lists)
    for i in range(n):
        flag = 1
        for j in range(1,n-i):
            if lists[j-1] >lists[j]:
                lists[j-1],lists[j] = lists[j],lists[j-1]
                flag = 0

        if flag:
            break
    return lists

#优化2：记录某次遍历时最后发生数据交换的位置，这个位置之后的数据显然已经有序了。
# 因此通过记录最后发生数据交换的位置就可以确定下次循环的范围了。
def bubble_sort3(lists):
    n = len(lists)
    k = n
    for i in range(n):
        flag = 1
        for j in range(1,k):
            if lists[j-1] > lists[j]:
                lists[j-1],lists[j] = lists[j],lists[j-1]
                k = j
                flag = 0
        if flag:
            break
    return lists

import random
if __name__ == '__main__':
    test_list = list(range(0,20))
    random.shuffle(test_list)
    print("before sort:")
    print(test_list)
    test_list = bubble_sort(test_list)
    print("after bubble sort:")
    print(test_list)

    random.shuffle(test_list)
    print("before sort:")
    print(test_list)
    test_list = bubble_sort2(test_list)
    print("after bubble sort 2:")
    print(test_list)

    random.shuffle(test_list)
    print("before sort:")
    print(test_list)
    test_list = bubble_sort3(test_list)
    print("after bubble sort 3:")
    print(test_list)