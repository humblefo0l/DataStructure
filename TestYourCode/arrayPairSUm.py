def pair_sum(arr, k):
    if len(arr) < 2:
        return

    # Sets for tracking
    seen = set()
    output = set()

    # For every number in array
    for num in arr:
        print("num is " , num)
        # Set target difference
        target = k - num
        print("target is ", target)
        # Add it to set if target hasn't been seen

        if target not in seen:
            seen.add(num)

        else:
            # Add a tuple with the corresponding pair
            output.add((min(num, target), max(num, target)))

        print("seen is ", seen)
        print("output is ", output)
        print("#############")
    # FOR TESTING
    return len(output)
    # Nice one-liner for printing output
    # return '\n'.join(map(str,list(output)))


print(pair_sum([1,3,2,2],4))