"""
Write a program to print all permutations of a given string
A permutation, also called an “arrangement number” or “order,” is a rearrangement of
the elements of an ordered list S into a one-to-one correspondence with S itself. A
string of length n has n! permutation.

Below are the permutations of string ABC.
ABC ACB BAC BCA CBA CAB

"""

def permute(s, l, r):
    if l == r:
        print("".join(s))
    else:

        for i in range(l, r):
            s[l], s[i] = s[i], s[l]
            permute(s, l + 1, r)
            s[l], s[i] = s[i], s[l]


def main():
    s = "ABC"
    s = [i for i in s]
    left = 0
    right = len(s)
    permute(s, left, right)


if __name__ == '__main__':
    main()
