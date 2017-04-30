#!/bin/python3

def longest_word(str):
    """Finds longest word in string and returns count of letters"""
    wList = str.split(" ")
    mx = 0

    for w in wList:
        if len(w) > mx:
            mx = len(w)
    return mx

def test_longest_word():
    """ Tests longest word """
    assert longest_word("The quick brown fox jumped over the lazy dog") == 6
    assert longest_word("May the force be with you") == 5
    assert longest_word("Google do a barrel roll") == 6
    assert longest_word("What is the average airspeed velocity of an unladen swallow") == 8
    assert longest_word("What if we try a super-long word such as otorhinolaryngology") == 19

    # JS version:

# function findLongestWord(str) {
#   var wList = str.split(" ");
#   var max = 0;
#   wList.forEach(function(word) {
#     if (word.length > max) {
#       max = word.length;
#     }
#   });
#   return max;
# }

# findLongestWord("The quick brown fox jumped over the lazy dog");
