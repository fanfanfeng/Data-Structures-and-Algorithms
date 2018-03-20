# create by fanfan on 2018/3/20 0020
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

def init_Node_from_list(l1):
    out = None
    tmp = None
    for item in l1:
        if out == None:
            out = ListNode(item)
            tmp = out
        else:
            newNode = ListNode(item)
            tmp.next = newNode
            tmp = newNode

    return out

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        out_list = None
        temp_node = None

        next_add = 0
        while l1 and l2:
            value = l1.val + l2.val + next_add
            l1 = l1.next
            l2 = l2.next

            if value >=10:
                value_real = value % 10
                next_add = int(value/10)
            else:
                next_add = 0
                value_real = value

            if out_list == None:
                out_list = ListNode(value_real)
                temp_node = out_list
            else:
                new_node = ListNode(value_real)
                temp_node.next = new_node
                temp_node = new_node

        while l1:
            value = l1.val  + next_add
            l1 = l1.next
            if value >= 10:
                value_real = value % 10
                next_add = int(value / 10)
            else:
                next_add = 0
                value_real = value

            if out_list == None:
                out_list = ListNode(value_real)
                temp_node = out_list
            else:
                new_node = ListNode(value_real)
                temp_node.next = new_node
                temp_node = new_node

        while l2:
            value = l2.val  + next_add
            l2 = l2.next
            if value >= 10:
                value_real = value % 10
                next_add = int(value / 10)
            else:
                next_add = 0
                value_real = value

            if out_list == None:
                out_list = ListNode(value_real)
                temp_node = out_list
            else:
                new_node = ListNode(value_real)
                temp_node.next = new_node
                temp_node = new_node

        if next_add > 0:
            new_node = ListNode(next_add)
            temp_node.next = new_node
            temp_node = new_node


        return out_list


if __name__ == '__main__':
    l1 = init_Node_from_list([5])
    l2 = init_Node_from_list([5])
    so = Solution()
    l3 = so.addTwoNumbers(l1,l2)
    print(l3)






