# create by fanfan on 2018/3/9 0009
def merge_sort(lists):
    if len(lists) <=1:
        return lists
    num = int(len(lists)/2)
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return merge(left,right)

def merge(left,right):
    l,r = 0,0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r +=1
    result += left[l:]
    result += right[r:]
    return result

import random
if __name__ == '__main__':
    test_list = list(range(0,20))
    random.shuffle(test_list)
    print("before sort:")
    print(test_list)
    test_list = merge_sort(test_list)
    print("after merget sort:")
    print(test_list)

