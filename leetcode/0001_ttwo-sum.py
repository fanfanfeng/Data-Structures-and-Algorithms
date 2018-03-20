# create by fanfan on 2018/3/20 0020

def twoSum( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    result = []
    for index, i in enumerate(nums[:-1]):
        other = target - i
        if other in nums[index+1:] :
            next_index = nums[index+1:].index(other) + (index+1)
            if index > next_index:
                result.append(next_index)
                result.append(index)
            elif next_index > index:
                result.append(index)
                result.append(next_index)
            break
    return result

def twoSum_1( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    map = {}
    for i, num in enumerate(nums):
        if (target - num) in map:
            return (map[target - num], i)
        else:
            map[num] = i

if __name__ == '__main__':
    test_cast=[([0,3,3,0],0),([2,3,3],6)]

    for test_item in test_cast:
        print(twoSum(*test_item))
        print(twoSum_1(*test_item))
        print('##################')