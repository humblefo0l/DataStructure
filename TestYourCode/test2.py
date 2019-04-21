

def max_in_neighbours(nums):
    # Write your code here
    n = 0
    for i in range( 1, len(nums) -1):
        if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
            n = i
            return n

    if nums[-1] > nums[-2]:
        return len(nums) -1






#
# print(max_in_neighbours([12,23,35,17]))
# print(max_in_neighbours([1,2,3,4]))




def compact_array(nums):
    start = 0
    end = 0
    string = ""
    ls = []

    for i in range(len(nums)-1):

        if nums[i] == nums[i+1] - 1:
            end = i+1
        else:
            if end < start:
                s = ("{}".format(nums[start]))
            else:
                s = ("{} to {}".format(nums[start], nums[end]))

            ls.append(s)
            start = i+1

    if end < start:
        s = ("{}".format(nums[start]))
    else:
        s = ("{} to {}".format(nums[start], nums[end]))

    ls.append(s)
    return ls

compact_array([1,
2,
3,
6,
7,
8,
10,
15])



def rollTheString(s, roll):
    a = [0 for x in s]

    for r in roll:
        for i in range(r):
            a[i] = a[i] + 1#do_i oll_char(s[i]) + s[:i+1]

    a = [x%26 for x in a ]

    s = [x for x in s]
    for i in range(len(a)):
        s[i] = chr(ord(s[i]) + a[i])

    print(s)


rollTheString('abz', [1,3])




def do_roll_char(c, n):
    return chr(ord(c) + n)

