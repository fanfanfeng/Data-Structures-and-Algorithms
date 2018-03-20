# create by fanfan on 2018/3/20 0020
def lengthOfLongestSubstring( s):
    """
    :type s: str
    :rtype: int
    """
    max_length = 0
    dict_visits = []
    current_lenth = 0
    for item in s:
        if item not in dict_visits:
            dict_visits.append(item)
            current_lenth += 1
        else:
            dict_visits.append(item)
            index = dict_visits.index(item)
            current_lenth -= index
            dict_visits = dict_visits[index+1:]

        if current_lenth >max_length:
            max_length = current_lenth
    return max_length

if __name__ == '__main__':
    print(lengthOfLongestSubstring("pwwkew"))


