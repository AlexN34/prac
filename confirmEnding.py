
def confirmEnding(str, target):
    result = str.find(target)
    # print("Print returned: %d, comparing to val at index: %d" % ( result, len(str)-1))
    return bool(result == len(str)-1)

def test_confirmEnding():
    assert confirmEnding("Bastian", "n") == True
