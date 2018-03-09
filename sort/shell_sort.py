# create by fanfan on 2018/3/9 0009
def shell_sort(lists):
    n = len(lists)
    gap = round(n/2)
    while gap > 0 :
        for i in range(gap,n):
            temp = lists[i]
            j = i
            while(j >= gap and lists[j - gap] >temp):
                lists[j] = lists[j - gap]
                j = j - gap
            lists[j] = temp

        gap = round(gap/2)
    return lists

import random
if __name__ == '__main__':
    test_list = list(range(0,20))
    random.shuffle(test_list)
    print("before sort:")
    print(test_list)
    test_list = shell_sort(test_list)
    print("after merget sort:")
    print(test_list)
