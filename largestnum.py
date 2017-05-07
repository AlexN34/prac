def largestOfFour(arr):
    """Return an array consisting of the largest number from each provided sub-array. For simplicity, the provided array will contain exactly 4 sub-arrays."""
    final = []
    for sub in arr:
        cur = max(sub)
        final.append(cur)
    return final

def test_largestOfFour():
    """ Tests largestOfFour function"""
    assert largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]) == [5,27,39,1001]
    assert largestOfFour([[4, 9, 1, 3], [13, 35, 18, 26], [32, 35, 97, 39], [1000000, 1001, 857, 1]]) == [9, 35, 97, 1000000]
