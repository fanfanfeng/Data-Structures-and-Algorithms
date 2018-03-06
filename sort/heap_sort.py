# create by fanfan on 2018/3/6 0006
def adjust_heap(lists,i,size):
    l_child = 2 * i + 1
    r_child = 2 * i + 2
    max = i
    if i < size/2:
        if l_child < size and lists[l_child] > lists[max]:
            max = l_child

        if r_child < size and lists[r_child] > lists[max]:
            max = r_child

        if max != i:
            lists[max],lists[i] = lists[i],lists[max]
            adjust_heap(lists,max,size)

def build_heap(lists,size):
    for i in list(range(0,int(size/2)))[::-1]:
        adjust_heap(lists,i,size)

def heap_sort(lists):
    size = len(lists)
    build_heap(lists,size)
    for i in list(range(0,size))[::-1]:
        lists[0],lists[i] = lists[i],lists[0]
        adjust_heap(lists,0,i)
import random
if __name__ == '__main__':
    test_list = list(range(0,20))
    random.shuffle(test_list)
    print("before sort:")
    print(test_list)
    heap_sort(test_list)
    print("after heap sort:")
    print(test_list)

# 时间复杂度：建堆过程 n + 堆调整  nlogn  总体 O(nlogn)
# 空间复杂度：O(1)